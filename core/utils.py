from collections import Counter


def count_frequencies(history):
    """
    Retourne les fréquences d'apparition des numéros et étoiles dans l'historique.
    :return: (Counter numéros, Counter étoiles)
    """
    all_numbers = []
    all_stars = []
    for nums, stars in history:
        all_numbers.extend(nums)
        all_stars.extend(stars)
    return Counter(all_numbers), Counter(all_stars)


def compute_overdue(history, number_range=range(1, 51), star_range=range(1, 13)):
    """
    Retourne le nombre de tirages depuis la dernière sortie de chaque numéro/étoile.
    :return: (dict numéro->retard, dict étoile->retard)
    """
    last_seen = {n: -1 for n in number_range}
    last_seen_star = {s: -1 for s in star_range}
    for idx, (nums, stars) in enumerate(history):
        for n in nums:
            last_seen[n] = idx
        for s in stars:
            last_seen_star[s] = idx
    overdue_numbers = {n: len(history) - last_seen[n] - 1 for n in number_range}
    overdue_stars = {s: len(history) - last_seen_star[s] - 1 for s in star_range}
    return overdue_numbers, overdue_stars
