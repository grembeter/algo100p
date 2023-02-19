import pytest


@pytest.fixture()
def libfile(request):
    return request.config.getoption("--lib")


@pytest.fixture()
def datafile(request):
    return request.config.getoption("--data")


def pytest_addoption(parser):
    parser.addoption(
        "--lib",
        action="store",
        default="libsolution.so",
        help="path to solution shared library",
    )
    parser.addoption(
        "--data",
        action="store",
        default="testcase.json",
        help="path to test case data file",
    )
