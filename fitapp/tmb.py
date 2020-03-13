import logging
from .goal_factory import GoalFactory


class ComputeDailyDiet:
    """
    Contains functions to compute daily macros and calories
    """
    logging.getLogger().setLevel(logging.INFO)

    def compute_tmb(self, weight, height, age, goal, activity_level=1.55):
        """
        TODO Refactor to Strategy pattern
        :param weight:
        :param height:
        :param age:
        :param goal:
        :param activity_level:
        :return:
        """
        tmb = round((10 * weight) + (6.25 * height) - (5 * age) + 5, 0)
        total_cal_day = round(tmb * activity_level, 0)

        goal = GoalFactory().get_instance(goal)

        total_cal_day_goal = goal.get_kcal_goal(total_cal_day)
        logging.info("Output: TMB = {} kcal | TotalCalPerDay = {} kcal | TotalMaintenance_{} = {} kcal"
                     .format(tmb, total_cal_day, goal, total_cal_day_goal))

        return goal, tmb, total_cal_day, total_cal_day_goal

    def compute_calories(self, weight, goal, total_cal_day):
        """

        :param weight:
        :param goal:
        :param total_cal_day:
        :return:
        """
        protein_kcal = 2.5 * weight * 4
        fat_kcal = round(0.8 * weight * 9, 1)
        carbo_kcal = round((goal.get_kcal_goal(total_cal_day) - (protein_kcal+fat_kcal)), 1)

        logging.info("Calories: Protein = {} kcal | Fat = {} | Carbo = {} kcal"
                     .format(protein_kcal, fat_kcal, carbo_kcal))

        return protein_kcal, fat_kcal, carbo_kcal

    def compute_macros(self, protein_kcal, fat_kcal, carbo_kcal):
        """
        Compute daily macros
        :param protein_kcal:
        :param fat_kcal:
        :param carbo_kcal:
        :return:
        """
        protein_g = round(protein_kcal/4, 0)
        fat_g = round(fat_kcal/9, 0)
        carbo_g = round(carbo_kcal/4, 0)

        logging.info("Protein = {} g | Fat = {} g | Carbo = {} g".format(protein_g, fat_g, carbo_g))

        return protein_g, fat_g, carbo_g
