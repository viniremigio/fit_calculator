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

print("Weight={}kg, Height={}cm, Age={}, Goal={}".format(peso, altura, idade, objetivo))
print("TMB = {}, TotalCalPerDay={}, TotalMaintenance_{} = {}".format(tmb, total_cal_day, objetivo, total_cal_goal))


proteina_kcal = 2.5 * peso * 4
gordura_kcal = round(0.8 * peso * 9, 1)
carbo_kcal = (total_cal_goal - (proteina_kcal+gordura_kcal))

print("Macros: protein_kcal = {}, fat_kcal = {}, carbo_kcal = {}".format(proteina_kcal, gordura_kcal, carbo_kcal))

print("Macros: protein_g = {}, fat_g = {}, carbo_g = {}".format(proteina_kcal/4, gordura_kcal/9, carbo_kcal/4))


