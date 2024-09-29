import sys
from src.core import Major
from src.utils import mrh, log

if __name__ == "__main__":
    while True:
        try:
            major = Major()
            major.main()
        except KeyboardInterrupt:
            log(mrh + f"Interrupted by users, exiting..")
            sys.exit()