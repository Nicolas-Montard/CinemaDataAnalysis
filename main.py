import pandas as pd

cinemas_data =  pd.read_csv("./csv/cinemas.csv", sep=";")

# J'ai gardé les données permettant de connaitre l'emplacement des cinémas en évitant les données difficilement exploitables telles que la longitude ou celles ayant toutes les mêmes valeurs telles que les régions.
# J'ai également gardé toutes les données en lien avec la taille des cinémas, leurs équipements et le type de contenu qu'ils proposent et leurs entrées.
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

# Je supprime les lignes dans lesquelles il manque des données, puisqu'il y a peu de données manquantes, ça n'aura pas un gros impact sur la validité des données.
cleaned_cinemas_data = cleaned_cinemas_data.dropna()

# puisque le champ entrées annuelles n'existe pas, je le crée en faisant une moyenne de entrées 2021 et entrées 2022
cleaned_cinemas_data["entrées annuelles"] = cleaned_cinemas_data[["entrées 2021", "entrées 2022"]].mean(axis=1)

print(cleaned_cinemas_data.head())

pd.options.display.float_format = '{:.2f}'.format

print(cleaned_cinemas_data[["fauteuils", "écrans", "entrées annuelles"]].describe())
print(cleaned_cinemas_data["unité urbaine"].nunique())
