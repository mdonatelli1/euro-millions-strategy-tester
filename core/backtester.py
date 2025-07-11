class Backtester:
    def __init__(self, strategy, history):
        self.strategy = strategy
        self.history = history
        self.results = []

    def run(self):
        """
        Applique la stratégie sur l'historique, en simulant une prédiction à chaque tirage (en n'utilisant que le passé).
        Stocke les résultats (prédiction, vrai tirage).
        """
        for i in range(1, len(self.history)):
            past = self.history[:i]
            true_draw = self.history[i]
            prediction = self.strategy.predict(past)
            self.results.append(
                {"index": i, "prediction": prediction, "true_draw": true_draw}
            )
        return self.results
