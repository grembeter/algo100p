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

    assert "arr" in testcase
    assert "sum" in testcase

    arr = (ctypes.c_int * len(testcase["arr"]))()

    for i, val in enumerate(testcase["arr"]):
        arr[i] = val

    LOGGER.debug("testcase = %s", json.dumps(testcase, indent=2))
    LOGGER.debug("lib = %s", libfile)

    c_lib = ctypes.CDLL(libfile)

    c_lib.max_subarray.restype = ctypes.c_int

    c_lib.max_subarray.argtypes = [
        ctypes.POINTER(ctypes.c_int),
        ctypes.c_size_t,
    ]

    LOGGER.debug(
        "call max_subarray with args: arr=%s, len=%d",
        list(arr),
        len(arr),
    )

    total = c_lib.max_subarray(arr, len(arr))

    LOGGER.debug("returned total=%d", total)

    assert total == testcase["sum"], f"Got {total}, but expected {testcase['sum']}"
