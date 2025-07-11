from collections import Counter

from .base import BaseStrategy


class MixHotColdStrategy(BaseStrategy):
    def predict(self, history):
        """
        Prédit une combinaison mixant hot et cold :
        - 3 numéros les plus fréquents + 2 les moins fréquents
        - 1 étoile la plus fréquente + 1 la moins fréquente
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
        all_possible_numbers = set(range(1, 51))
        all_possible_stars = set(range(1, 13))
        for n in all_possible_numbers:
            if n not in num_counts:
                num_counts[n] = 0
        for s in all_possible_stars:
            if s not in star_counts:
                star_counts[s] = 0
        hot_numbers = [n for n, _ in num_counts.most_common(3)]
        cold_numbers = [
            n for n, _ in sorted(num_counts.items(), key=lambda x: (x[1], x[0]))[:2]
        ]
        hot_stars = [s for s, _ in star_counts.most_common(1)]
        cold_stars = [
            s for s, _ in sorted(star_counts.items(), key=lambda x: (x[1], x[0]))[:1]
        ]
        return sorted(hot_numbers + cold_numbers), sorted(hot_stars + cold_stars)
