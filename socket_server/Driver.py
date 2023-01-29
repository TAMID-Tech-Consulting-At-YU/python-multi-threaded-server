import Configuration
import logging
import Server
import os


def main():
    config = get_config()
    serv = Server.Server(config)


def get_config():
    return Configuration.Configuration("127.0.0.1", 65534)


if __name__ == "__main__":
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "DEBUG"))
    main()
