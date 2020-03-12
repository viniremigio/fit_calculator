from .tmb import ComputeDailyDiet


class FitCalculator:

    @staticmethod
    def run(weight, height, age, goal):

        calc = ComputeDailyDiet()

        goal, kcal = calc.compute_tmb(weight, height, age, goal)
        protein_kcal, fat_kcal, carbo_kcal = calc.compute_calories(weight, goal, kcal)
        calc.compute_macros(protein_kcal, fat_kcal, carbo_kcal)
