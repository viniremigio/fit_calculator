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
    parser.add_argument('--activity', type=float, required=True, help="accepted values: [1.2, 1.375, 1.55, 1.75, 1.9]")
    parser.add_argument('--protein-rate', type=float, required=True, help="i. e. 2g/kg")
    parser.add_argument('--fat-rate', type=float, required=True, help="i. e. 1g/kg")

    args = parser.parse_args()

    weight = args.weight
    height = args.height
    age = args.age
    goal = args.goal
    activity = args.activity
    protein_rate = args.protein_rate
    fat_rate = args.fat_rate

    logging.info("Input: Weight = {}kg | Height = {}cm | Age = {} | Goal = {} | Activity = {} | Protein Rate = {} | Fat Rate = {}".format(weight, height, age, goal, activity, protein_rate, fat_rate))

    fit = FitCalculator()
    fit.run(weight, height, age, goal, activity, protein_rate, fat_rate)
