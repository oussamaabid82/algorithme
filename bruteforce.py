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


def liste_des_prix(actions):
    liste_des_prix = []
    for i in range(len(actions)):
        prix = actions[i]["prix"]
        liste_des_prix.append(prix)
    return liste_des_prix 

def calcule_benifice(actions):
    liste_des_benifices = []    
    for i in range(len(actions)):       
        benifice = actions[i]["prix"] * actions[i]["taux"]
        liste_des_benifices.append(benifice)
    return liste_des_benifices

def ajout_benifice_dict(actions, benifices):
    for i, benifice in zip(range(len(benifices)), benifices):
        act = actions[i]
        act["benifice"] = benifice

def force_brute(budget, actions, actions_selection = []):
    if actions:
        val1, lstVal1 = force_brute(budget, actions[1:], actions_selection)
        val = actions[0]
        
        if val["prix"] <= budget:
            val2, lstVal2 = force_brute(budget - val["prix"], actions[1:], actions_selection + [val])
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return sum([i["benifice"] for i in actions_selection]),[i for i in actions_selection] 

def affichage(force_brute):
    for i in (force_brute[1]):
        print("Vous devez acheté l'" + " " + i["Action"] + " " + "de la valeur" + str(i["prix"]) 
        + " " + "euro et qui degage un benifice de" + " " + str(i["benifice"] ) + " " + "euro")
    print("Pour une marge total de" + " " + str(force_brute[0]) + " " + "euro")

if __name__ == "__main__":

    LISTES_DES_PRIX_PAR_ACTION = liste_des_prix(ACTIONS)
    LISTE_DES_MARGES_PAR_ACTION = calcule_benifice(ACTIONS)
    ajout_benifice_dict(ACTIONS, LISTE_DES_MARGES_PAR_ACTION)
    force_brute = force_brute(BUDGET, ACTIONS)
    affichage(force_brute)



