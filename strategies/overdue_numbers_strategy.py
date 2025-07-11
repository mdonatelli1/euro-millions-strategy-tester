from .base import BaseStrategy


class OverdueNumbersStrategy(BaseStrategy):
    def predict(self, history):
        """
        Prédit les 5 numéros et 2 étoiles qui ne sont pas sortis depuis le plus longtemps.
        """
        if not history:
            return [], []
        all_numbers = set(range(1, 51))
        all_stars = set(range(1, 13))
        last_seen = {n: -1 for n in all_numbers}
        last_seen_star = {s: -1 for s in all_stars}
        for idx, (nums, stars) in enumerate(history):
            for n in nums:
                last_seen[n] = idx
            for s in stars:
                last_seen_star[s] = idx
        # Les plus "en retard" sont ceux dont last_seen est le plus petit
        overdue_numbers = sorted(all_numbers, key=lambda n: last_seen[n])[:5]
        overdue_stars = sorted(all_stars, key=lambda s: last_seen_star[s])[:2]
        return sorted(overdue_numbers), sorted(overdue_stars)
