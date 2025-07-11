from collections import Counter

from .base import BaseStrategy


class ColdNumbersStrategy(BaseStrategy):
    def predict(self, history):
        """
        Prédit les 5 numéros et 2 étoiles les moins fréquents dans l'historique.
        """
        if not history:
            return [], []
        all_numbers = []
        all_stars = []
        for nums, stars in history:
            all_numbers.extend(nums)
            all_stars.extend(stars)
        # On compte les fréquences, puis on prend les moins fréquents
        num_counts = Counter(all_numbers)
        star_counts = Counter(all_stars)
        # On complète avec les numéros/étoiles jamais sortis
        all_possible_numbers = set(range(1, 51))
        all_possible_stars = set(range(1, 13))
        for n in all_possible_numbers:
            if n not in num_counts:
                num_counts[n] = 0
        for s in all_possible_stars:
            if s not in star_counts:
                star_counts[s] = 0
        cold_numbers = [
            n for n, _ in sorted(num_counts.items(), key=lambda x: (x[1], x[0]))[:5]
        ]
        cold_stars = [
            s for s, _ in sorted(star_counts.items(), key=lambda x: (x[1], x[0]))[:2]
        ]
        return sorted(cold_numbers), sorted(cold_stars)
