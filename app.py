from default_logging import setup_logging
import logging

if __name__ == "__main__":
    setup_logging()
    logging.getLogger(__name__).info("Logging is set up with UTC timestamps.")