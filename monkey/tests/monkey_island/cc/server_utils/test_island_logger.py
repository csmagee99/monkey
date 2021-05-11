import logging
import os

import pytest

from monkey_island.cc.server_utils.island_logger import setup_logging


def test_expanduser_filename_log_level_debug(tmpdir):
    DATA_DIR = tmpdir
    INFO_LOG = os.path.join(DATA_DIR, "monkey_island.log")
    LOG_LEVEL = logging.DEBUG
    TEST_STRING = "Hello, Monkey! (Log level: debug)"

    setup_logging(DATA_DIR, LOG_LEVEL)

    logger = logging.getLogger("TestLogger")
    logger.debug(TEST_STRING)

    assert os.path.isfile(INFO_LOG)
    with open(INFO_LOG, "r") as f:
        line = f.readline()
        assert TEST_STRING in line


def test_expanduser_filename_log_level_info(tmpdir):
    DATA_DIR = tmpdir
    INFO_LOG = os.path.join(DATA_DIR, "monkey_island.log")
    LOG_LEVEL = "INFO"
    TEST_STRING = "Hello, Monkey! (Log level: info)"

    setup_logging(DATA_DIR, LOG_LEVEL)

    logger = logging.getLogger("TestLogger")
    logger.debug(TEST_STRING)

    assert os.path.isfile(INFO_LOG)
    with open(INFO_LOG, "r") as f:
        line = f.readline()
        assert TEST_STRING not in line
