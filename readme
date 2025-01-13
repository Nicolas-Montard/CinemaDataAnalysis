# Analyse de l'impact cinématographiques sur les entrées annuelles dans les cinémas français

## Description du projet

Ce projet cherche a évaluer l'impact cinématographiques sur les entrées annuelles dans les cinémas français.

Il est séparer en quatre partie:

### Partie 1 : Nettoyage et exploration des données

Le fichier CSV est charger et nettoyer en enlevant les lignes auquel il manque des données et en ne gardant que les données pertinantes.
Après ça il affiche dans le terminal les premières lignes du dataset et donne des statistique descriptive des fauteil, écrans et entrées annuelles (Les entrées annuelles ont été faite avec la moyenne de l'année 2021 et 2022).

### Partie 2 : Analyse des données

Un calcul des entrées moyenne par fauteuil a été faite et les unités urbaines ayant les 3 meilleurs et pires moyenne s'affiche dans le terminal (Puisque le champs des région a la même valeur pour toute les données, j'ai décidé d'utiliser les unité urbaine à la place).
Un graphique à bar s'affiche représentant les entrées moyennes par fauteuil pour les unités urbaine.

### Partie 3 : Corrélation entre infrastructures et fréquentation

Un calcul de la correlation entre le nombre d'écrans et les entrées annuelles en 2022 et le nombre de fauteuils et les entrées annuelles en 2022 est afficher dans le terminal, puis un nuage à point est fait à partir de ces données.

### Partie 4 : Modèle prédictif des entrées annuelles

Un modèle de regression linéaire est créer, il sert à prédire les entrées annuelles des cinémas fonction de plusieurs variables (écrans, fauteuils, population de la commune).

Premièrement il divise les données en ensembles d'entraînement (80%) et de test (20%).
Ensuite il entraine un modèle de régression linéaire avec les données d'entraînement.
Les performances du modèle sont ensuite évaluer et coefficient de détermination (R2) et l’erreur moyenne absolue (MAE) sont afficher dans le terminal.

## installation

### Étape 1 : Cloner le dépôt

### Étape 2 : Configurer l'environnement virtuel

<u>Créer un environement virtuel :</u>
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