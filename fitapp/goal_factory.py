class GoalFactory:
    """
    FactoryMethod to choose between gain, lose or maintain weight
    """
    @staticmethod
    def get_instance(goal):
        if goal == 'lose':
            return GoalLose()
        elif goal == 'gain':
            return GoalGain()
        elif goal == 'maintain':
            return GoalMaintain()


class GoalGain:
    """
    Class defines attributes to gain weight
    """
    def __init__(self):
        self.gain_cal = 400

    def get_kcal_goal(self, total_kcal):
        return total_kcal + self.gain_cal

    def __str__(self):
        return "Gain"


class GoalLose:
    """
    Class defines attributes to lose weight
    """
    def __init__(self):
        self.lose_cal_percentage = 0.8

    def get_kcal_goal(self, total_kcal):
        return total_kcal * self.lose_cal_percentage

    def __str__(self):
        return "Lose"


class GoalMaintain:
    """
    Class defines attributes to maintain current weight
    """
    def get_kcal_goal(self, total_kcal):
        return total_kcal

    def __str__(self):
        return "Maintain"
