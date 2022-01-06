

import csv

BUDGET = 500

def recup_csv():
    actions_list = []
    with open("dataset1.csv", mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            actions_list.append(row)
    return actions_list

def change_type_profit(actions):
    for i in range(len(actions)):
        action = actions[i]
        action["price"] = action["price"].replace("-", "")
        action["profit"] = float(action["profit"])
        action["price"] = float(action["price"])

def calculat_best_profit_optimize(budget, actions):
    model_list = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]
    for i in range(1, len(actions) + 1):
        for (j) in range(1, budget + 1):
            if (actions[i-1]["price"]) <= j and (actions[i-1]["price"]) > 0:
                model_list[i][j] = max((actions[i-1]["profit"]) + model_list[i-1]
                                        [j-int(actions[i-1]["price"])], model_list[i-1][j])
            else:
                model_list[i][j] = model_list[i-1][j]

    # Retrouver les éléments en fonction de la somme
    n = len(actions)
    selected_actions = []

    while budget >= 0 and n >= 0:
        action = actions[n-1]
        if model_list[n][budget] == model_list[n-1][budget-int(action["price"])] + (action["profit"]):
            selected_actions.append(action)
            budget -= int(action["price"])
        n -= 1
    return model_list[-1][-1], selected_actions

def display(optimized):
    price = []
    for i in (optimized[1]):
        price.append(int(i["price"]))
        print("Vous devez acheté l'" + " " + i["name"] + " " + "d'une valeur de" + " " + str(i["price"])
              + " " + "euro et qui degage un profit de" + " " + str(round(i["profit"], 2)) + " " + "euro")

    print(" * Vous avez achete des actions pour la somme total de" + " " + str(sum(price))+ " " + "euro")
    print(" * Vous avez une marge total de" + " " + str(round(optimized[0], 2)) + " " + "euro")


if __name__ == "__main__":
    liste_actions = recup_csv()
    change_type_profit(liste_actions)
    optimized = calculat_best_profit_optimize(BUDGET, liste_actions)
    display(optimized)
