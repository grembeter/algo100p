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

    assert "matrix" in testcase
    assert "size" in testcase
    assert "result" in testcase

    matrix = (ctypes.c_int * len(testcase["matrix"]))()

    for i, val in enumerate(testcase["matrix"]):
        matrix[i] = val

    LOGGER.debug("testcase = %s", json.dumps(testcase, indent=2))
    LOGGER.debug("lib = %s", libfile)

    c_lib = ctypes.CDLL(libfile)

    # int count_islands(int *matrix, size_t nrows, size_t ncols);

    c_lib.count_islands.argtypes = [
        ctypes.POINTER(ctypes.c_int),
        ctypes.c_size_t,
        ctypes.c_size_t,
    ]

    LOGGER.debug(
        "call count_islands with args: matrix=%s, nrows=%d, ncols=%d",
        list(matrix),
        testcase["size"],
        testcase["size"],
    )

    islands = c_lib.count_islands(matrix, testcase["size"], testcase["size"])

    LOGGER.debug("returned islands=%d", islands)

    assert (
        islands == testcase["result"]
    ), f"Got {islands}, but expected {testcase['result']}"
