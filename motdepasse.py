import hashlib
import json
def password():
    mot_de_passe = input("choisissez un mot de passe : ")
    pas_majuscule = mot_de_passe.islower()
    pas_miniscule = mot_de_passe.isupper()
    pas_chiffre = not any( char.isdigit() for char in mot_de_passe )
    caractere =  "!, @, #, $, %, ^, &, *" 
    def caractere_spec(): 
        for i in mot_de_passe:
            for n in caractere:
                if n == i:
                    return True
        return False
    if len(mot_de_passe) < 8:
        print("erreur")
        return password()
    elif pas_majuscule:
        print("erreur2")
        return password()
    elif pas_miniscule:
        print("erreur3")
        return password()
    elif pas_chiffre:
        print("erreur4")
        return password()
    elif caractere_spec() == False:
        print("erreur5")
        return password()
    else:
        return mot_de_passe
def hasher(str):
    hach = hashlib.sha256(str.encode(encoding='utf-8')).hexdigest()
    return hach
mdp = hasher(password())
new_mdp = {"mdp":mdp}
mot_depasse={"mdp":mdp}
with open("database.json","r+")as write:
    donnee = json.load(write)
    if new_mdp in donnee["motdepasse"]: 
        print("mot de passe deja rentre") 
    else:
        donnee["motdepasse"].append(mot_depasse)
        write.seek(0)
        json.dump(donnee, write,indent=4) 
    




