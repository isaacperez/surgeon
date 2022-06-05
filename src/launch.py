"""

This is the entry point for the app.

"""

import sys

from classes.app import SurgeonApp


def main():
    r"""Launch the main window.
    """
    app = SurgeonApp(sys.argv)

    # Launch GUI and start event loop
    app.gui()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
