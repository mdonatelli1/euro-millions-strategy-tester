import os

import pandas as pd


def load_history(csv_path=None):
    """
    Charge l'historique des tirages EuroMillions depuis un fichier CSV.
    :param csv_path: Chemin du fichier CSV
    :return: DataFrame pandas
    """
    if csv_path is None:
        csv_path = os.path.join(
            os.path.dirname(__file__), "../data/euromillions_history.csv"
        )
    df = pd.read_csv(csv_path, sep=";")
    return df
