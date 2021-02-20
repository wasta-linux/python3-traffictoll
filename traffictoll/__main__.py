import sys

import logging as logger

from .cli import get_argument_parser, main as cli_main
from .exceptions import ConfigError, MissingDependencyError


def main() -> None:
    parser = get_argument_parser()
    arguments = parser.parse_args()

    # noinspection PyBroadException
    try:
        logger.basicConfig(format='%(levelname)s:%(message)s', level=logger.INFO)
        logger.info(f"args: {arguments}")
        cli_main(arguments)
    except KeyboardInterrupt:
        logger.info("Aborted")
    except ConfigError as error:
        logger.error("Invalid configuration: {}", error)
    except MissingDependencyError as error:
        logger.error("Missing dependency: {}", error)
    except Exception as e:
        print(e)
        logger.exception("Unexpected error occurred: ")


if __name__ == "__main__":
    main()
