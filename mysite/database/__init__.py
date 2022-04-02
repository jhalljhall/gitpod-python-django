from os.path import abspath
from sys import path

path.insert(0, abspath(__file__).rsplit('/', 2)[0])

# do not comment out
import config.load_django

