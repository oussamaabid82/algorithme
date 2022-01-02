
BUDGET = 500
ACTIONS = [
{"Action": "Action-1", "prix":20, "taux": 0.05},
{"Action": "Action-2", "prix":30, "taux": 0.10},
{"Action": "Action-3", "prix":50, "taux": 0.15},
{"Action": "Action-4", "prix":70, "taux": 0.20},
{"Action": "Action-5", "prix":60, "taux": 0.17},
{"Action": "Action-6", "prix":80, "taux": 0.25},
{"Action": "Action-7", "prix":22, "taux": 0.07},
{"Action": "Action-8", "prix":26, "taux": 0.11},
{"Action": "Action-9", "prix":48, "taux": 0.13},
{"Action": "Action-10", "prix":34, "taux": 0.27},
{"Action": "Action-11", "prix":42, "taux": 0.17},
{"Action": "Action-12", "prix":110, "taux": 0.09},
{"Action": "Action-13", "prix":38, "taux": 0.23},
{"Action": "Action-14", "prix":14, "taux": 0.01},
{"Action": "Action-15", "prix":18, "taux": 0.03},
{"Action": "Action-16", "prix":8, "taux": 0.08},
{"Action": "Action-17", "prix":4, "taux": 0.12},
{"Action": "Action-18", "prix":10, "taux": 0.14},
{"Action": "Action-19", "prix":24, "taux": 0.21},
{"Action": "Action-20","prix":114, "taux": 0.18}
]

def calcule_benifice(actions):
    liste_des_benifices = []    
    for i in range(len(actions)):       
        benifice = actions[i]["prix"] * actions[i]["taux"]
        liste_des_benifices.append(benifice)
    return liste_des_benifices

def ajout_benifice_dict(actions, benifices):
    for i, benifice in zip(range(len(benifices)), benifices):
        action = actions[i]
        action["benifice"] = benifice


def force_brut(budget, actions):
    liste_model = [[0 for x in range(budget + 1)] for x in range(len(actions) + 1)]
    for i in range(1, len(actions) + 1):
        for j in range(1, budget + 1):
            if actions[i-1]["prix"] <= j:
                liste_model[i][j] = max(actions[i-1]["benifice"] + liste_model[i-1][j-actions[i-1]["prix"]], liste_model[i-1][j])
            else:
                liste_model[i][j] = liste_model[i-1][j]
	
    # Retrouver les éléments en fonction de la somme
    n = len(actions)
    actions_selection = []

    while budget >= 0 and n >= 0:
        action = actions[n-1]
        if liste_model[n][budget] == liste_model[n-1][budget-action["prix"]] + action["benifice"]:
            actions_selection.append(action)
            budget -= action["prix"]
        n -= 1

    return liste_model[-1][-1], actions_selection

def affichage(force_brute):
    prix = []
    for i in (force_brute[1]):
        prix.append(i["prix"])
        print("Vous devez acheté l'" + " " + i["Action"] + " " + "d'une valeur de" + " " + str(i["prix"])
        + " " + "euro et qui degage un benifice de" + " " + str(round(i["benifice"], 2)) + " " + "euro")
    print(" * Vous avez achete des actions pour la somme total de" + " " + str(sum(prix))+ " " + "euro")
    print(" * Vous avez une marge total de" + " " + str(round(force_brute[0], 2)) + " " + "euro")

if __name__ == "__main__":
    LISTE_DES_MARGES_PAR_ACTION = calcule_benifice(ACTIONS)
    ajout_benifice_dict(ACTIONS, LISTE_DES_MARGES_PAR_ACTION)	
    force = force_brut(BUDGET, ACTIONS)
    affichage(force)