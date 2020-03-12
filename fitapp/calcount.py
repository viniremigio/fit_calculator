import sys

peso = float(sys.argv[1])

proteina_g = 2 * peso
gordura_g = 1 * peso
carbo_g = 2 * peso

total_cal = (proteina_g * 4) + (gordura_g * 9) + (carbo_g * 4)

print("Total cal = {}".format(total_cal))
print("Proteina = {}g, Gordura = {}g, Carbo = {}g".format(proteina_g, gordura_g, carbo_g))
