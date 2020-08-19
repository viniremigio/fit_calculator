from .goal_factory import GoalFactory


class ComputeDailyDiet:
    """
    Contains functions to compute daily macros and calories
    Activity Level:
    
    - Sedentary = BMR x 1.2 (little or no exercise, desk job)
    - Lightly active = BMR x 1.375 (light exercise/ sports 1-3 days/week)
    - Moderately active = BMR x 1.55 (moderate exercise/ sports 6-7 days/week)
    - Very active = BMR x 1.725 (hard exercise every day, or exercising 2 xs/day)
    - Extra active = BMR x 1.9 (hard exercise 2 or more times per day, or training for
    marathon, or triathlon, etc
    - Article: https://www.k-state.edu/paccats/Contents/PA/PDF/Physical%20Activity%20and%20Controlling%20Weight.pdf
    """

    def compute_tmb(self, weight, height, age, goal, activity_level, gender):
        """
        TODO Refactor to Strategy pattern
        Homens: TMB = 66 + (13,8 x peso em kg.) + (5 x altura em cm) - (6,8 x idade em anos). 
        Mulheres: TMB = 655 + (9,6 x peso em kg.) + (1,8 x altura em cm) - (4,7 x idade em anos)
        Homens_2: tmb = round((10 * weight) + (6.25 * height) - (5 * age) + 5, 0)
        https://www.superprof.com.br/blog/por-que-alguns-necessitam-de-mais-energia-que-outros/
        """
        if gender == "male":
            tmb = round(66.0 + (13.8 * weight) + (5 * height) - (6.8 * age), 0)
        elif gender == "female":
            tmb = round(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age), 0)

        total_cal_day = round(tmb * activity_level, 0)

        goal = GoalFactory().get_instance(goal)

        total_cal_day_goal = goal.get_kcal_goal(total_cal_day)
        print(
            "\nOutput:\nTMB = {} kcal\nTotalCalPerDay = {} kcal\nTotalMaintenance_{} = {} kcal".format(
                tmb, total_cal_day, goal, total_cal_day_goal
            )
        )

        return goal, tmb, total_cal_day, total_cal_day_goal

    def compute_calories(self, weight, goal, total_cal_day, protein_rate, fat_rate):
        """

        :param weight:
        :param goal:
        :param total_cal_day:
        :return:
        """
        protein_kcal = protein_rate * weight * 4
        fat_kcal = round(fat_rate * weight * 9, 1)
        carbo_kcal = round(
            (goal.get_kcal_goal(total_cal_day) - (protein_kcal + fat_kcal)), 1
        )

        print(
            "Calories: Protein = {} kcal | Fat = {} | Carbo = {} kcal".format(
                protein_kcal, fat_kcal, carbo_kcal
            )
        )

        return protein_kcal, fat_kcal, carbo_kcal

    def compute_macros(self, protein_kcal, fat_kcal, carbo_kcal):
        """
        Compute daily macros
        :param protein_kcal:
        :param fat_kcal:
        :param carbo_kcal:
        :return:
        """
        protein_g = round(protein_kcal / 4, 0)
        fat_g = round(fat_kcal / 9, 0)
        carbo_g = round(carbo_kcal / 4, 0)

        print(
            "Protein = {} g\nFat = {} g\nCarbohydrates = {} g".format(
                protein_g, fat_g, carbo_g
            )
        )

        return protein_g, fat_g, carbo_g
