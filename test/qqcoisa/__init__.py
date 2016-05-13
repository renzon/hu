import unittest
import sys
import os

PROJECT_PATH = os.path.sep.join(os.path.abspath(__file__).split(os.path.sep)[:-3])
ROOT_PATH = os.path.dirname(__file__)


def main():
    path_setup()
    tests = unittest.TestLoader().discover(ROOT_PATH, "*.py")
    result = unittest.TextTestRunner().run(tests)
    if not result.wasSuccessful():
        sys.exit(1)


def path_setup():
    print(PROJECT_PATH)
    sys.path.append(PROJECT_PATH)

print(PROJECT_PATH)
path_setup()