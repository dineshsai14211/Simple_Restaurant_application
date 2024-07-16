"""
These program contains the logging logic to log the logged messages
"""
import logging as log

log.basicConfig(filename="../logs/app.log", filemode="a", level=log.DEBUG,
                format="%(asctime)s - %(levelname)s - %(message)s")
