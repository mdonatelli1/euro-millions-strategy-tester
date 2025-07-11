import random

from .base import BaseStrategy


class NeverDrawnStrategy(BaseStrategy):
    def predict(self, history):
        """
        Prédit une combinaison (numéros + étoiles) jamais sortie dans l'historique.
        Si toutes les combinaisons ont déjà été tirées, retourne une combinaison aléatoire.
        """
        if not history:
            return [], []
        seen = set(
            (tuple(sorted(nums)), tuple(sorted(stars))) for nums, stars in history
        )
        # Générer jusqu'à 1000 essais pour trouver une combinaison jamais sortie
        for _ in range(1000):
            nums = tuple(sorted(random.sample(range(1, 51), 5)))
            stars = tuple(sorted(random.sample(range(1, 13), 2)))
            if (nums, stars) not in seen:
                return list(nums), list(stars)
        # Si toutes les combinaisons ont déjà été tirées, retourne une aléatoire
        return list(nums), list(stars)
