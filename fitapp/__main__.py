import logging
import argparse
from .app import FitCalculator

if __name__ == '__main__':

    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('--weight', type=float, required=True)
    parser.add_argument('--height', type=int, required=True)
    parser.add_argument('--age', type=int, required=True)
    parser.add_argument('--goal', type=str, required=True, help="lose|gain|maintain")

    args = parser.parse_args()

    weight = args.weight
    height = args.height
    age = args.age
    goal = args.goal

    logging.info("Input: Weight = {}kg | Height = {}cm | Age = {} | Goal = {}".format(weight, height, age, goal))

    fit = FitCalculator()
    fit.run(weight, height, age, goal)
