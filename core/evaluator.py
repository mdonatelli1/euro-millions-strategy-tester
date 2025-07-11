def evaluate(backtest_results):
    """
    Calcule les statistiques de performance d'une stratégie à partir des résultats du backtest.
    :param backtest_results: Liste de dicts avec 'prediction' et 'true_draw'
    :return: dict de stats
    """
    total = len(backtest_results)
    total_main_hits = 0
    total_star_hits = 0
    for res in backtest_results:
        pred_main, pred_stars = res["prediction"]
        true_main, true_stars = res["true_draw"]
        main_hits = len(set(pred_main) & set(true_main))
        star_hits = len(set(pred_stars) & set(true_stars))
        total_main_hits += main_hits
        total_star_hits += star_hits
    return {
        "total_draws": total,
        "avg_main_hits": total_main_hits / total if total else 0,
        "avg_star_hits": total_star_hits / total if total else 0,
    }
