

import csv

BUDGET = 500

def recup_csv():
    liste_actions = []
    with open("actions.csv", mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            liste_actions.append(row)

    return liste_actions

def calculate_profit(actions):
    profit_list = []    
    for i in range(len(actions)):      
        profit = float(actions[i]["prix"]) * float(actions[i]["taux"])
        profit_list.append(profit)
    return profit_list

def added_profit_in_dict(actions, profits):
    for i, profit in zip(range(len(profits)), profits):
        action = actions[i]
        action["benefice"] = float(profit)

def calculat_best_profit(budget, actions):
    model_list = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]
    for i in range(1, len(actions) + 1):
        for j in range(1, budget + 1):
            if int(actions[i-1]["prix"]) <= j:
                model_list[i][j] = max((actions[i-1]["benefice"]) + model_list[i-1][j-int(actions[i-1]["prix"])], model_list[i-1][j])
            else:
                model_list[i][j] = model_list[i-1][j]

    # Retrouver les éléments en fonction de la somme
    n = len(actions)
    actions_selection = []

    while budget >= 0 and n >= 0:
        action = actions[n-1]
        if model_list[n][budget] == model_list[n-1][budget-int(action["prix"])] + (action["benefice"]):
            actions_selection.append(action)
            budget -= int(action["prix"])
        n -= 1
    return model_list[-1][-1], actions_selection

def display(force_brute):
    prix = []
    for i in (force_brute[1]):
        prix.append(int(i["prix"]))
        print("Vous devez acheté l'" + " " + i["Action"] + " " + "d'une valeur de" + " " + str(i["prix"])
        + " " + "euro et qui degage un benefice de" + " " + str(round(i["benefice"], 2)) + " " + "euro")
    print(" * Vous avez achete des actions pour la somme total de" + " " + str(sum(prix))+ " " + "euro")
    print(" * Vous avez une marge total de" + " " + str(round(force_brute[0], 2)) + " " + "euro")


if __name__ == "__main__":
    liste_actions = recup_csv()
    list_profit_per_action = calculate_profit(liste_actions)
    added_profit_in_dict(liste_actions, list_profit_per_action)	
    force_brute = calculat_best_profit(BUDGET, liste_actions)
    display(force_brute)
