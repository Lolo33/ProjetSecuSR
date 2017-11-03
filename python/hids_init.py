import tkinter as tk
from tkinter.filedialog import askopenfilenames

# fichier init en lecture et ecriture
fichier_init = open("init", 'a')
fichier_init_read = open("init", 'r')

# Vérifie si le nom du site est valide (n'existe pas dans le fichier init)
def name_valid(name):
    for ligne in fichier_init_read.readlines():
        if (name == ligne.split(",")[0].split(":")[1]):
            return False
    return True

# SAISIE DES PARAMETRES DINITIALISATION
name = input("Saisissez le nom de votre site\n")
# Vérifie que le nom est bien unique
while (name_valid(name) == False):
    print("Ce nom de site existe déja")
    name = input("Saisissez le nom de votre site\n")
url = input("Saisissez l'url de votre site\n")
interval = input("Saisissez l'intervalle de temps entre lequel la vérification sera lancée\n")
type = input("Saisissez le type de votre site [wp, joo, other]\n")

# ECRITURE DES PARAMETRES D'INITIALISATION DANS LE FICHIER INIT
fichier_init.write("\nname:" + name + ",url:" + url + ",interval:" + interval + ",type:" + type)
fichier_init.close()

# Ouvre une interface permettant de sélectionner les fichiers à surveiller et écrit les chemins de ces derniers dans le fichier list_%name%
root = tk.Tk()
files = askopenfilenames()
fichier_list = open("list_" + name, "w+")
for file in files:
    fichier_list.write(file + "\n")
fichier_list.close()


'''for ligne in lignes:
    info_tab = ligne.split(",")
    name = info_tab[0].split(":")[1]
    url = info_tab[1].split(":")[1]
    interval = info_tab[2].split(":")[1]
    type = info_tab[3].split(":")[3]
    if (type == "wp"):'''

