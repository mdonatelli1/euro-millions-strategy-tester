import random

from .base import BaseStrategy


class RandomStrategy(BaseStrategy):
    def predict(self, history):
        """
        Prédit une combinaison aléatoire valide pour l'EuroMillions.
        :param history: Liste des tirages précédents (non utilisé ici)
        :return: (numéros, étoiles)
        """
        numbers = random.sample(range(1, 51), 5)  # 5 numéros entre 1 et 50
        stars = random.sample(range(1, 13), 2)  # 2 étoiles entre 1 et 12
        return sorted(numbers), sorted(stars)
