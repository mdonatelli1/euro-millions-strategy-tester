# EuroMillions Strategy Tester

Ce projet permet de comparer objectivement différentes stratégies de prédiction pour l'EuroMillions, en les backtestant sur l'historique réel des tirages. Il met en évidence, chiffres à l'appui, que l'EuroMillions est un jeu de pur hasard.

## Fonctionnalités principales

-   Chargement de l'historique des tirages depuis un fichier CSV
-   Implémentation et comparaison de multiples stratégies (fréquence, retard, jamais sortis, etc.)
-   Backtest rigoureux sans fuite de données
-   Affichage comparatif des performances de chaque stratégie
-   Prédiction de la prochaine combinaison selon chaque stratégie

## Structure du projet

```
EuroMillions/
│
├── main.py                  # Point d'entrée, comparatif des stratégies
├── requirements.txt         # Dépendances Python
├── README.md                # Ce fichier
│
├── data/
│   └── euromillions_history.csv   # Historique des tirages
│
├── core/
│   ├── data_loader.py       # Chargement des données
│   ├── backtester.py        # Backtest des stratégies
│   ├── evaluator.py         # Évaluation des performances
│   ├── predictor.py         # Prédiction du prochain tirage
│   └── utils.py             # Fonctions utilitaires
│
├── strategies/
│   ├── base.py              # Classe de base pour les stratégies
│   ├── random_strategy.py   # Stratégie aléatoire (baseline)
│   ├── hot_numbers_strategy.py      # Numéros les plus fréquents
│   ├── cold_numbers_strategy.py     # Numéros les moins fréquents
│   ├── overdue_numbers_strategy.py  # Numéros en retard
│   ├── never_drawn_strategy.py      # Combinaison jamais sortie
│   ├── mix_hot_cold_strategy.py     # Mix hot/cold
│   └── even_odd_strategy.py         # Pairs/impairs fréquents
```

## Stratégies implémentées

-   **RandomStrategy** : 5 numéros et 2 étoiles tirés au hasard
-   **HotNumbersStrategy** : 5 numéros et 2 étoiles les plus fréquents
-   **ColdNumbersStrategy** : 5 numéros et 2 étoiles les moins fréquents
-   **OverdueNumbersStrategy** : 5 numéros et 2 étoiles en retard
-   **NeverDrawnStrategy** : combinaison jamais sortie dans l'historique
-   **MixHotColdStrategy** : 3 hot + 2 cold (numéros), 1 hot + 1 cold (étoiles)
-   **EvenOddStrategy** : 3 pairs + 2 impairs (numéros), 1 paire + 1 impaire (étoiles)

## Exemple de résultat

```
=== Comparatif des stratégies ===
Stratégie                 | Main hits  | Star hits  | Prédiction prochaine
----------------------------------------------------------------------------------------------------
RandomStrategy            | 0.50       | 0.31       | Numéros: [8, 23, 27, 41, 46], Étoiles: [2, 3]
HotNumbersStrategy        | 0.51       | 0.34       | Numéros: [21, 29, 34, 35, 42], Étoiles: [3, 6]
ColdNumbersStrategy       | 0.45       | 0.33       | Numéros: [1, 4, 22, 31, 43], Étoiles: [4, 5]
OverdueNumbersStrategy    | 0.48       | 0.33       | Numéros: [2, 6, 13, 28, 31], Étoiles: [7, 8]
NeverDrawnStrategy        | 0.51       | 0.30       | Numéros: [5, 6, 8, 33, 41], Étoiles: [1, 10]
MixHotColdStrategy        | 0.49       | 0.31       | Numéros: [1, 21, 22, 34, 35], Étoiles: [3, 4]
EvenOddStrategy           | 0.50       | 0.33       | Numéros: [16, 21, 34, 35, 42], Étoiles: [3, 6]
```

## Installation

1. Clonez le repo
2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```
3. Placez un fichier d'historique EuroMillions dans `data/euromillions_history.csv` (format FDJ)

## Utilisation

```bash
python main.py
```

## Limites et conclusion

-   **Aucune stratégie ne bat le hasard** sur le long terme, comme le montre le comparatif.
-   Ce projet prouve, par l'expérimentation, la nature aléatoire de l'EuroMillions.
-   Il reste un excellent outil pédagogique et un support pour tester toute nouvelle idée de stratégie.

---

**Auteur :** Mattéo Donatelli — 2025
