def compute_final_score(metrics: dict):
    # expects metrics from analyze_answer
    # scale final_estimate (0-10) to 0-100
    v = metrics.get('final_estimate',0)
    return round(v*10,2)
