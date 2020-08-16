import os
import csv
from .tmb import ComputeDailyDiet


class FitCalculator:

    def __init__(self):
        self.db = 'data/database.csv'

    def run(self, weight, height, age, goal, activity, protein_rate, fat_rate):

        calc = ComputeDailyDiet()

        goal, tmb, kcal, kcal_goal = calc.compute_tmb(weight, height, age, goal, activity)
        protein_kcal, fat_kcal, carbo_kcal = calc.compute_calories(weight, goal, kcal, protein_rate, fat_rate)
        protein_g, fat_g, carbo_g = calc.compute_macros(protein_kcal, fat_kcal, carbo_kcal)

        with open(self.db, 'a') as f:
            fieldnames = ['height', 'goal', 'weight', 'age', 'tmb', 'kcal_day',
                          'kcal_goal', 'pkcal', 'fkcal', 'ckcal', 'pg', 'fg', 'cg']

            row = csv.DictWriter(f, fieldnames=fieldnames)

            if os.stat(self.db).st_size == 0:
                row.writeheader()

            row.writerow({'height': height, 'goal':goal, 'weight': weight,
                          'age': age, 'tmb': tmb, 'kcal_day': kcal, 'kcal_goal': kcal_goal,
                          'pkcal': protein_kcal, 'fkcal': fat_kcal,
                          'ckcal': carbo_kcal, 'pg': protein_g, 'fg': fat_g, 'cg': carbo_g })
