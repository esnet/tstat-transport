"""
Utility code for tstat_transport package and client programs.
"""

import logging
import time
import signal
import socket


class GracefulInterruptHandler(object):  # pylint: disable=too-few-public-methods
    """
    Context manager to handle sigint.

    snippet courtesy of gist: https://gist.github.com/nonZero/2907502
    """

    # pylint: disable=attribute-defined-outside-init, unused-argument,
    # pylint: disable=missing-docstring, invalid-name, redefined-builtin
    def __init__(self, sig=signal.SIGINT):
        self.sig = sig

    def __enter__(self):
        self.interrupted = False
        self.released = False

        self.original_handler = signal.getsignal(self.sig)

        def handler(signum, frame):
            self.release()
            self.interrupted = True

        signal.signal(self.sig, handler)

        return self

    def __exit__(self, type, value, tb):
        self.release()

    def release(self):
        if self.released:
            return False

        signal.signal(self.sig, self.original_handler)

        self.released = True

        return True


def setup_log(log_path=None):
    """
    Usage:
    _log('main.start', 'happy simple log event')
    _log('launch', 'more={0}, complex={1} log=event'.format(100, 200))
    """
    # pylint: disable=redefined-variable-type
    from loguru import logger
    if log_path is not None:
        logger.add('{0}/tstat_transport.log'.format(log_path))
    logger.level("INFO")
    return logger


log = setup_log()  # pylint: disable=invalid-name


def _log(event, msg, modern=False):
    log.info(msg)


def valid_hostname(hostname):
    """Validate a hostname."""
    try:
        socket.gethostbyname(hostname)
        return True
    except socket.gaierror:
        return False
