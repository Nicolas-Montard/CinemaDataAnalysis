# Analyse de l'impact cinématographiques sur les entrées annuelles dans les cinémas français

## Description du projet

Ce projet cherche à évaluer l'impact cinématographique sur les entrées annuelles dans les cinémas français.

Il est séparé en quatre parties:

### Partie 1 : Nettoyage et exploration des données

Le fichier CSV est chargé et nettoyé en enlevant les lignes auxquelles il manque des données et en ne gardant que les données pertinentes.

Après ça il affiche dans le terminal les premières lignes du dataset et donne des statistiques descriptives des fauteils, écrans et entrées annuelles (Les entrées annuelles ont été faites avec la moyenne de l'année 2021 et 2022).

### Partie 2 : Analyse des données

Un calcul des entrées moyennes par fauteuil a été fait et les unités urbaines ayant les 3 meilleurs et pires moyennes s'affichent dans le terminal. (Puisque le champ des régions a la même valeur pour toutes les données, j'ai décidé d'utiliser les unités urbaines à la place).
Un graphique à barres s'affiche représentant les entrées moyennes par fauteuil pour les unités urbaine.

### Partie 3 : Corrélation entre infrastructures et fréquentation

Un calcul de la corrélation entre le nombre d'écrans et les entrées annuelles en 2022 et le nombre de fauteuils et les entrées annuelles en 2022 est affiché dans le terminal, puis un nuage à point est fait à partir de ces données.

### Partie 4 : Modèle prédictif des entrées annuelles

Un modèle de régression linéaire est créé, il sert à prédire les entrées annuelles des cinémas en fonction de plusieurs variables (écrans, fauteuils, population de la commune).

Premièrement, il divise les données en ensembles d'entraînement (80%) et de test (20%).

Ensuite, il entraîne un modèle de régression linéaire avec les données d'entraînement.

Les performances du modèle sont ensuite évaluées et le coefficient de détermination (R2) et l’erreur moyenne absolue (MAE) sont affichés dans le terminal.

Le modèle est ensuite utilisé pour prédire les entrées en 2022 et le résultat est comparé à l'aide d'un graphique superposant les résultats réels de 2022 et ceux prédits par le modèle.

## Installation

### Étape 1 : Cloner le dépôt

### Étape 2 : Configurer l'environnement virtuel

<u>Créer un environnement virtuel :</u>
python3 -m venv venv

<u>Lancer l'environnement :</u>
**Sur windows:** venv\Scripts\activate
**Sur Mac/Linux:** source venv/bin/activate

### Étape 3 : Installer les dépendances

pip install -r requirements.txt

ou

pip install pandas

pip install matplotlib

pip install seaborn

pip install scikit-learn

### Étape 4 : Lancer le fichier

python3 main.py

## Réponse au question de cours :

**Question de l'exercice 3 :** Les graphiques montre que le nombre d'écrans a un impact très légérement plus fort sur les entrées annuelles que le nombre de fauteuils, ce qui se voit par le fait que la ligne créer par la régression linéaire superposée va un peu plus vers le haut pour les écrans que pour les fauteils.

**Question de l'exercice 4 :** Le nombre d'écrans et de fauteils sont un bon prédicteur des entrées, ce qui se vois par le coefficient de determination élevé.