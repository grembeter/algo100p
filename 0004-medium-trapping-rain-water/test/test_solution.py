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
    assert "total" in testcase

    arr = (ctypes.c_int * len(testcase["arr"]))()

    for i, val in enumerate(testcase["arr"]):
        arr[i] = val

    LOGGER.debug("testcase = %s", json.dumps(testcase, indent=2))
    LOGGER.debug("lib = %s", libfile)

    c_lib = ctypes.CDLL(libfile)

    # int trap_rain(int *buf, size_t len);

    c_lib.trap_rain.restype = ctypes.c_int

    c_lib.trap_rain.argtypes = [
        ctypes.POINTER(ctypes.c_int),
        ctypes.c_size_t,
    ]

    LOGGER.debug(
        "call trap_rain with args: arr=%s, len=%d",
        list(arr),
        len(arr),
    )

    total = c_lib.trap_rain(arr, len(arr))

    LOGGER.debug("returned total=%d", total)

    assert total == testcase["total"], f"Got {total}, but expected {testcase['total']}"
