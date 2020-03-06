import sys

peso = float(sys.argv[1])
altura = float(sys.argv[2])
idade = float(sys.argv[3])
objetivo = sys.argv[4]

# Moderate
nivel_atividade = 1.55

tmb = round((10 * peso) + (6.25 * altura) - (5 * idade) + 5, 0)
total_cal_day = round(tmb*nivel_atividade, 0)

if objetivo == 'lose':
    total_cal_goal = total_cal_day * 0.8
elif objetivo == 'gain':
    total_cal_goal = total_cal_day + 400

print("\n\n=== Input ===")
print("Weight = {}kg\nHeight = {}cm\nAge = {}\nGoal = {}\n".format(peso, altura, idade, objetivo))

print("\n=== Output ===")
print("TMB = {} kcal\nTotalCalPerDay = {} kcal\nTotalMaintenance_{} = {} kcal\n"
      .format(tmb, total_cal_day, objetivo, total_cal_goal))

proteina_kcal = 2.5 * peso * 4
gordura_kcal = round(0.8 * peso * 9, 1)
carbo_kcal = (total_cal_goal - (proteina_kcal+gordura_kcal))

print("\n=== Macros ===")
print("Protein = {} kcal\nFat = {} \nCarbo = {} kcal\n".format(proteina_kcal, gordura_kcal, carbo_kcal))
print("Protein = {} g\nFat = {} g\nCarbo = {} g\n\n"
      .format(round(proteina_kcal/4, 0), round(gordura_kcal/9, 0), round(carbo_kcal/4, 0)))
