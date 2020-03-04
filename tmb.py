import sys

peso = float(sys.argv[1])
altura = float(sys.argv[2])
idade = float(sys.argv[3])
objetivo = sys.argv[4]

nivel_atividade = 1.55 # moderado

tmb = round((10*peso) + (6.25*altura) - (5*idade) + 5,0)
total_cal_day = round(tmb*nivel_atividade,0)

if(objetivo == 'perda'):
    total_cal_goal = total_cal_day * 0.8
elif(objetivo == 'ganho'):
    total_cal_goal = total_cal_day + 400

print("Peso={}, Altura={}, Idade={}, Objetivo = {}".format(peso, altura, idade, objetivo))
print("TMB = {}, TotalCalPerDay={}, TotalMaintenance_{} = {}".format(tmb, total_cal_day, objetivo, total_cal_goal))


proteina_kcal = 2.5 * peso * 4
gordura_kcal = round(0.8 * peso * 9,1)
carbo_kcal = (total_cal_goal - (proteina_kcal+gordura_kcal))

print("Macros: proteina_kcal = {}, gordura_kcal = {}, carbo_kcal = {}".format(proteina_kcal, gordura_kcal, carbo_kcal))

print("Macros: proteina_g = {}, gordura_g = {}, carbo_g = {}".format(proteina_kcal/4, gordura_kcal/9, carbo_kcal/4))


