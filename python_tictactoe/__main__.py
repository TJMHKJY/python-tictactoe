import sys
from python_tictactoe.app.app_main import App

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    App().run()


if __name__ == "__main__":
    main()