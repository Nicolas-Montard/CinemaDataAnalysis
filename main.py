import pandas as pd
import matplotlib.pyplot as plt

cinemas_data =  pd.read_csv("./csv/cinemas.csv", sep=";")

# J'ai gardé les données permettant de connaitre l'emplacement des cinémas en évitant les données difficilement exploitables telles que la longitude ou celles ayant toutes les mêmes valeurs telles que les régions
# J'ai également gardé toutes les données en lien avec la taille des cinémas, leurs équipements et le type de contenu qu'ils proposent et leurs entrées
cinemas_columns = [
    "entrées 2022",
    "entrées 2021",
    "écrans",
    "fauteuils",
    "semaines d'activité",
    "zone de la commune",
    "nombre de films programmés",
    "nombre de films inédits",
    "nombre de films en semaine 1",
    "population de la commune",
    "commune",
    "multiplexe",
    "évolution entrées",
    "unité urbaine"
]
cleaned_cinemas_data = cinemas_data[cinemas_columns]

# Je supprime les lignes dans lesquelles il manque des données, puisqu'il y a peu de données manquantes, ça n'aura pas un gros impact sur la validité des données
cleaned_cinemas_data = cleaned_cinemas_data.dropna()

# puisque le champ entrées annuelles n'existe pas, je le crée en faisant une moyenne de entrées 2021 et entrées 2022
cleaned_cinemas_data["entrées annuelles"] = cleaned_cinemas_data[["entrées 2021", "entrées 2022"]].mean(axis=1)

print(cleaned_cinemas_data.head())

pd.options.display.float_format = '{:.2f}'.format
print(cleaned_cinemas_data[["fauteuils", "écrans", "entrées annuelles"]].describe())

# ********************************************************************
# puisque tout les champs contiennes la même région, je vais utiliser les unité urbaine à la place
cleaned_cinemas_data["chair_per_entrance"] = cleaned_cinemas_data["entrées 2022"] / cleaned_cinemas_data["fauteuils"]
average_chair_by_urban_unit = cleaned_cinemas_data.groupby("unité urbaine")["chair_per_entrance"].mean()
print("les 3 unité urbaine ayant eu le moins de personnes par siège au cours de l'années 2022 sont :")
print(average_chair_by_urban_unit.sort_values().head(3))
print("les 3 unité urbaine ayant eu le plus de personnes par siège au cours de l'années 2022 sont :")
print(average_chair_by_urban_unit.sort_values().tail(3))
# ********************************************************************

def get_average_chair_by_urban_unit_digram(df):
    plt.bar(df.index, df)
    plt.title('Entrées moyennes par fauteuil par unité urbaine en 2022')
    plt.ylabel('Entrées moyennes par fauteuil')
    plt.xlabel('Unité urbaine')
    plt.xticks(rotation=90)
    plt.grid(axis='y')
    plt.tight_layout()
    plt.show()

get_average_chair_by_urban_unit_digram(average_chair_by_urban_unit)