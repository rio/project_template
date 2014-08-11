#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

if sys.version_info.major < 3:
    sys.exit("This program requires Python 3, exiting now.")

import logging
import signal

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QCommandLineParser
from PyQt5.QtCore import QCommandLineOption

# Setup the default logging format
MESSAGE_FORMAT = "{asctime} | {levelname:^8} | {name:^8} {lineno}: {message}"

# Terminate on CTRL+C. Usually this just works but with the Qt event loop it doesn't.
signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    app = QCoreApplication(sys.argv)

    # Set some application details.
    app.setApplicationName("MyApp")
    app.setApplicationVersion("0.1.0")
    app.setOrganizationName("My Organization")
    app.setOrganizationDomain("www.my-organization.org")

    # Create a verbosity command line option.
    verbose_option = QCommandLineOption("verbose", "Verbose mode. Print out debug messages.")

    # Setup the commandline parser.
    command_parser = QCommandLineParser()
    command_parser.addHelpOption()
    command_parser.addVersionOption()

    # Add the commandline options.
    command_parser.addOption(verbose_option)

    # Process the command line.
    command_parser.process(app)

    # Set the basic logger mnessage format and verbosity level.
    logger = logging.getLogger()

    # This dictates how the messages are formatted.
    formatter = logging.Formatter(fmt=MESSAGE_FORMAT, style='{')

    # This handler sends everything to stdout.
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # Add the handler to the logger.
    logger.addHandler(handler)

    # Check if the verbosity flag is set and set the log level to debug if it is.
    if command_parser.isSet(verbose_option):
        logger.setLevel(logging.DEBUG)
        logger.debug("Setting loglevel to debug.")

    else:
        logger.setLevel(logging.ERROR)

    # Start the event loop.
    sys.exit(app.exec())
# end main
