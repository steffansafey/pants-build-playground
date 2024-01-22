from . import webserver


def main():
    """Entry point for the server."""
    print("Starting up!")
    webserver.run_server()


if __name__ == "__main__":
    main()
