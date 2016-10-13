import pytest


def pytest_addoption(parser):
    parser.addoption("--env")
