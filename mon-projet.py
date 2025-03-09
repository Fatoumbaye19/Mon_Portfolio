import pandas as pd


def charger_donnees(fichier):

  colonnes_utiles = ['HStart', 'HEnd']
  donnees = pd.read_csv(fichier, usecols=colonnes_utiles, sep=",")
  return donnees


def calcul_duree_totale(donnees):
  
  donnees['HStart'] = pd.to_datetime(donnees['HStart'])
  donnees['HEnd'] = pd.to_datetime(donnees['HEnd'])

  
  donnees['Duree'] = (donnees['HEnd'] -
                      donnees['HStart']).dt.total_seconds() / 3600

  
  duree_totale = donnees['Duree'].sum()

  
  print("Charge totale d'heures d'enseignement :", duree_totale)


fichier_csv = r'ade.csv'

donnees = charger_donnees(fichier_csv)
calcul_duree_totale(donnees)
