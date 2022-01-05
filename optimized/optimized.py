import csv

BUDGET = 500

def recup_csv():
    liste_actions = []
    with open("actions.csv", mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            liste_actions.append(row)

    return liste_actions

def calcule_benifice(actions):
    liste_des_benifices = []    
    for i in range(len(actions)):      
        benifice = float(actions[i]["prix"]) * float(actions[i]["taux"])
        liste_des_benifices.append(benifice)
    return liste_des_benifices

def ajout_benifice_dict(actions, benifices):
    for i, benifice in zip(range(len(benifices)), benifices):
        action = actions[i]
        action["benifice"] = float(benifice)

def force_brut(budget, actions):
    liste_model = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]
    for i in range(1, len(actions) + 1):
        for j in range(1, budget + 1):
            if int(actions[i-1]["prix"]) <= j:
                liste_model[i][j] = max((actions[i-1]["benifice"]) + liste_model[i-1][j-int(actions[i-1]["prix"])], liste_model[i-1][j])
            else:
                liste_model[i][j] = liste_model[i-1][j]
	
    # Retrouver les éléments en fonction de la somme
    n = len(actions)
    actions_selection = []

    while budget >= 0 and n >= 0:
        action = actions[n-1]
        if liste_model[n][budget] == liste_model[n-1][budget-int(action["prix"])] + (action["benifice"]):
            actions_selection.append(action)
            budget -= int(action["prix"])
        n -= 1
    return liste_model[-1][-1], actions_selection

def affichage(force_brute):
    prix = []
    for i in (force_brute[1]):
        prix.append(int(i["prix"]))
        print("Vous devez acheté l'" + " " + i["Action"] + " " + "d'une valeur de" + " " + str(i["prix"])
        + " " + "euro et qui degage un benifice de" + " " + str(round(i["benifice"], 2)) + " " + "euro")
    print(" * Vous avez achete des actions pour la somme total de" + " " + str(sum(prix))+ " " + "euro")
    print(" * Vous avez une marge total de" + " " + str(round(force_brute[0], 2)) + " " + "euro")
   
if __name__ == "__main__":
    liste_actions = recup_csv()
    LISTE_DES_MARGES_PAR_ACTION = calcule_benifice(liste_actions)
    ajout_benifice_dict(liste_actions, LISTE_DES_MARGES_PAR_ACTION)	
    force_brute = force_brut(BUDGET, liste_actions)
   
    affichage(force_brute)