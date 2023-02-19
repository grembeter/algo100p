#!/usr/bin/env python3

"""
Test solution
"""

import json
import ctypes
import logging

LOGGER = logging.getLogger(__name__)


def test_hello() -> None:
    """Satity test"""

    LOGGER.debug("hello")
    assert True


def test_solution(libfile: str, datafile: str) -> None:
    """Test solution using C shared library"""

    with open(datafile, "rb") as fil:
        testcase = json.loads(fil.read())

    assert "inarr" in testcase
    assert "outarr" in testcase
    assert "ninput" in testcase
    assert "ntotal" in testcase

    arr = (ctypes.c_int * len(testcase["outarr"]))()

    for i, val in enumerate(testcase["inarr"]):
        arr[i] = val

    LOGGER.debug("testcase = %s", json.dumps(testcase, indent=2))
    LOGGER.debug("lib = %s", libfile)

    c_lib = ctypes.CDLL(libfile)

    # void replace_even(int *buf, size_t ninput, size_t ntotal);

    c_lib.replace_even.restype = None

    c_lib.replace_even.argtypes = [
        ctypes.POINTER(ctypes.c_int),
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]

    LOGGER.debug(
        "call replace_even with args: arr=%s, ninput=%d, ntotal=%d",
        list(arr),
        testcase["ninput"],
        testcase["ntotal"],
    )

    c_lib.replace_even(arr, testcase["ninput"], testcase["ntotal"])

    LOGGER.debug("returned arr=%s", list(arr))

    assert (
        list(arr) == testcase["outarr"]
    ), f"Got {json.dumps(list(arr))}, expected {testcase['outarr']}"
