"""Main module for running cli."""
from src.config import Config
from src.utils import process_command


def main():
    """Run main loop."""
    config: Config = Config()
    while True:
        if config.hunter is None:
            api_key: str = input("Please, enter your api key for 'Hunter' service.\n")
            config.set_hunter(api_key)
        else:
            command: str = input("Please, enter command.\n")
            process_command(command)


if __name__ == "__main__":
    main()
