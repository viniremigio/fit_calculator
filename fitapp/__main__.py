import sys
import logging
from .app import FitCalculator

if __name__ == '__main__':

    logging.getLogger().setLevel(logging.INFO)

    weight = float(sys.argv[1])
    height = float(sys.argv[2])
    age = float(sys.argv[3])
    goal = sys.argv[4]

    logging.info("Input: Weight = {}kg | Height = {}cm | Age = {} | Goal = {}".format(weight, height, age, goal))

    FitCalculator.run(weight, height, age, goal)
