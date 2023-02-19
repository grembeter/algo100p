#!/usr/bin/env python3

"""
Test solution
"""

import json
import ctypes
import logging

LOGGER = logging.getLogger(__name__)


class PairStruct(ctypes.Structure):  # pylint: disable=too-few-public-methods
    """Describe struct pair"""

    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]


def test_hello() -> None:
    """Satity test"""

    LOGGER.debug("hello")
    assert True


def test_solution(libfile: str, datafile: str) -> None:
    """Test solution using C shared library"""

    with open(datafile, "rb") as fil:
        testcase = json.loads(fil.read())

    assert "sum" in testcase
    assert "arr" in testcase
    assert "nelem" in testcase

    arr = (ctypes.c_int * len(testcase["arr"]))()

    for i, val in enumerate(testcase["arr"]):
        arr[i] = val

    LOGGER.debug("testcase = %s", json.dumps(testcase, indent=2))
    LOGGER.debug("lib = %s", libfile)

    c_lib = ctypes.CDLL(libfile)

    # struct pair *find_2sum(int sum, int *arr, size_t nelems);

    c_lib.find_2sum.restype = ctypes.c_void_p

    c_lib.find_2sum.argtypes = [
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_int),
        ctypes.c_size_t,
    ]

    LOGGER.debug(
        "call find_2sum with args: sum=%s, arr=%s, nelem=%d",
        testcase["sum"],
        list(arr),
        testcase["nelem"],
    )

    pair = c_lib.find_2sum(testcase["sum"], arr, testcase["nelem"])
    pair = PairStruct.from_address(pair)

    LOGGER.debug("returned pair=%d,%d (%s)", pair.x, pair.y, type(pair))

    assert pair.x + pair.y == testcase["sum"], "pair sum does not match given sum"

    assert pair.x in testcase["arr"], "pair.x is not in arr"

    assert pair.y in testcase["arr"], "pair.y is not in arr"
