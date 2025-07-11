def predict_next(strategy, history):
    """
    Utilise la stratégie pour prédire le prochain tirage à partir de tout l'historique.
    :param strategy: instance de BaseStrategy
    :param history: liste des tirages passés
    :return: (numéros, étoiles)
    """
    return strategy.predict(history)
