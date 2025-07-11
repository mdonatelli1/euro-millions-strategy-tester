from collections import Counter

from .base import BaseStrategy


class HotNumbersStrategy(BaseStrategy):
    def predict(self, history):
        """
        Prédit les 5 numéros et 2 étoiles les plus fréquents dans l'historique.
        """
        if not history:
            # Si pas d'historique, on fait du random (ou on retourne une combinaison vide)
            return [], []
        all_numbers = []
        all_stars = []
        for nums, stars in history:
            all_numbers.extend(nums)
            all_stars.extend(stars)
        most_common_numbers = [n for n, _ in Counter(all_numbers).most_common(5)]
        most_common_stars = [s for s, _ in Counter(all_stars).most_common(2)]
        return sorted(most_common_numbers), sorted(most_common_stars)
