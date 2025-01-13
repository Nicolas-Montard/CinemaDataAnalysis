import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

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
print("\nles 3 unité urbaine ayant eu le moins de personnes par siège au cours de l'années 2022 sont :")
print(average_chair_by_urban_unit.sort_values().head(3))
print("\nles 3 unité urbaine ayant eu le plus de personnes par siège au cours de l'années 2022 sont :")
print(average_chair_by_urban_unit.sort_values().tail(3))

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

# ********************************************************************

data_filtered_2022 = cleaned_cinemas_data[["écrans", "fauteuils", "entrées 2022"]].dropna()
correlation_chair_entrees = data_filtered_2022["fauteuils"].corr(data_filtered_2022["entrées 2022"])
correlation_screen_entrees = data_filtered_2022["écrans"].corr(data_filtered_2022["entrées 2022"])
print(f"\nLa correlation entre les fauteils et les entrées annuelles sont de : {correlation_chair_entrees:.2f}")
print(f"La correlation entre les écrans et les entrées annuelles sont de : {correlation_screen_entrees:.2f}")

def scatter_diagram(data, col1, col2, title, x_label, y_label, data2 = None):
    sns.regplot(x=col1, y=col2, data=data, line_kws={'color':'blue'})
    if(data2 is not None and len(data2) > 0):
        data2_df = pd.DataFrame({col1: data[col1], col2: data2})
        sns.regplot(x=col1, y=col2, data=data2_df, color='green', line_kws={'color':'green'}, marker="x")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

scatter_diagram(
    data=data_filtered_2022,
    col1="fauteuils",
    col2="entrées 2022",
    title="Corrélation entre le nombre de fauteuils et les entrées annuelles",
    x_label="Nombre de fauteuils",
    y_label="Entrées annuelles"
)
scatter_diagram(
    data=data_filtered_2022,
    col1="écrans",
    col2="entrées 2022",
    title="Corrélation entre le nombre d'écrans et les entrées annuelles",
    x_label="Nombre de fauteuils",
    y_label="Entrées annuelles"
)

# ********************************************************************

explanatory_variable = cleaned_cinemas_data[["écrans", "fauteuils", "population de la commune"]]
target_variable = cleaned_cinemas_data["entrées 2021"]

X_train, X_test, y_train, y_test = train_test_split(explanatory_variable, target_variable, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Performance du modèle")
print(f"R² : {r2:.2f}")
print(f"MAE : {mae:.2f}")

explanatory_variable = cleaned_cinemas_data[["écrans", "fauteuils", "population de la commune"]]
target_variable = cleaned_cinemas_data["entrées 2022"]

y_2022_prediction = model.predict(explanatory_variable)

scatter_diagram(
    data=data_filtered_2022,
    col1="écrans",
    col2="entrées 2022",
    title="Corrélation entre le nombre d'écrans et les entrées annuelles",
    x_label="Nombre de fauteuils",
    y_label="Entrées annuelles",
    data2=y_2022_prediction
)