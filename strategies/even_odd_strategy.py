from collections import Counter

from .base import BaseStrategy


class EvenOddStrategy(BaseStrategy):
    def predict(self, history):
        """
        Prédit 3 numéros pairs les plus fréquents et 2 impairs les plus fréquents,
        1 étoile paire la plus fréquente et 1 impaire la plus fréquente.
        """
        if not history:
            return [], []
        all_numbers = []
        all_stars = []
        for nums, stars in history:
            all_numbers.extend(nums)
            all_stars.extend(stars)
        num_counts = Counter(all_numbers)
        star_counts = Counter(all_stars)
        even_numbers = [n for n in range(1, 51) if n % 2 == 0]
        odd_numbers = [n for n in range(1, 51) if n % 2 == 1]
        even_stars = [s for s in range(1, 13) if s % 2 == 0]
        odd_stars = [s for s in range(1, 13) if s % 2 == 1]
        top_even = [n for n, _ in num_counts.most_common() if n in even_numbers][:3]
        top_odd = [n for n, _ in num_counts.most_common() if n in odd_numbers][:2]
        top_even_stars = [s for s, _ in star_counts.most_common() if s in even_stars][
            :1
        ]
        top_odd_stars = [s for s, _ in star_counts.most_common() if s in odd_stars][:1]
        return sorted(top_even + top_odd), sorted(top_even_stars + top_odd_stars)
