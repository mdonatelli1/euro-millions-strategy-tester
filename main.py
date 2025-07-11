from core.backtester import Backtester
from core.data_loader import load_history
from core.evaluator import evaluate
from core.predictor import predict_next
from strategies.cold_numbers_strategy import ColdNumbersStrategy
from strategies.even_odd_strategy import EvenOddStrategy
from strategies.hot_numbers_strategy import HotNumbersStrategy
from strategies.mix_hot_cold_strategy import MixHotColdStrategy
from strategies.never_drawn_strategy import NeverDrawnStrategy
from strategies.overdue_numbers_strategy import OverdueNumbersStrategy
from strategies.random_strategy import RandomStrategy


def parse_draws(df):
    draws = []
    for _, row in df.iterrows():
        nums = [int(row[f"boule_{i}"]) for i in range(1, 6)]
        stars = [int(row[f"etoile_{i}"]) for i in range(1, 3)]
        draws.append((nums, stars))
    return draws


def main():
    df = load_history()
    draws = parse_draws(df)
    strategies = [
        RandomStrategy(),
        HotNumbersStrategy(),
        ColdNumbersStrategy(),
        OverdueNumbersStrategy(),
        NeverDrawnStrategy(),
        MixHotColdStrategy(),
        EvenOddStrategy(),
    ]
    results = []
    for strat in strategies:
        backtester = Backtester(strat, draws)
        res = backtester.run()
        stats = evaluate(res)
        prediction = predict_next(strat, draws)
        results.append(
            {"strategy": str(strat), "stats": stats, "prediction": prediction}
        )
    # Affichage comparatif
    print("\n=== Comparatif des stratégies ===\n")
    print(
        f"{'Stratégie':<25} | {'Main hits':<10} | {'Star hits':<10} | Prédiction prochaine"
    )
    print("-" * 100)
    for r in results:
        s = r["strategy"]
        main_hits = f"{r['stats']['avg_main_hits']:.2f}"
        star_hits = f"{r['stats']['avg_star_hits']:.2f}"
        pred = f"Numéros: {r['prediction'][0]}, Étoiles: {r['prediction'][1]}"
        print(f"{s:<25} | {main_hits:<10} | {star_hits:<10} | {pred}")
    print("")


if __name__ == "__main__":
    main()
