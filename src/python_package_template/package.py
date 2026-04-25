from __future__ import annotations

import logging

import colorlog

LOGGER = logging.getLogger(__name__)


def configure_logging(level: int = logging.INFO) -> None:
    """Configure readable colored logging for applications using this package."""
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)-8s%(reset)s %(name)s - %(message)s",
        ),
    )

    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.addHandler(handler)
    root_logger.setLevel(level)


def hello() -> str:
    """Return a small greeting from the template package."""
    LOGGER.info("Starting python-package-template")
    return "hello from python-package-template"
