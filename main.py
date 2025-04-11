from dotenv import load_dotenv
from dishka import make_container

from agent_reviewer.di import ReviewerProvider
from di import RootProvider


def main():
    load_dotenv()

    make_container(RootProvider(), ReviewerProvider())


if __name__ == "__main__":
    main()
