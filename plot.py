import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def load_scores(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f]

def plot_grouped_scores(data, title, save_path):
    descriptions = [d["business_description"] for d in data]
    relevance = [d["relevance"] for d in data]
    brandability = [d["brandability"] for d in data]
    appropriateness = [d["appropriateness"] for d in data]

    x = np.arange(len(descriptions))
    width = 0.25

    plt.figure(figsize=(14, 6))
    plt.bar(x - width, relevance, width, label='Relevance')
    plt.bar(x, brandability, width, label='Brandability')
    plt.bar(x + width, appropriateness, width, label='Appropriateness')

    plt.xlabel("Business Description")
    plt.ylabel("Score (0.0 - 1.0)")
    plt.title(title)
    plt.xticks(ticks=x, labels=descriptions, rotation=45, ha="right")
    plt.ylim(0, 1.05)
    plt.legend()
    plt.tight_layout()

    Path("outputs").mkdir(exist_ok=True)
    plt.savefig(save_path)
    print(f"Saved plot: {save_path}")
    plt.show()

def filter_top_scoring(data, top_n=10):
    return sorted(data, key=lambda d: d["final_score"], reverse=True)[:top_n]

def filter_blocked(data):
    return [d for d in data if d["final_score"] == 0.0]

if __name__ == "__main__":
    data = load_scores("data/eval_scores_v1.jsonl")

    # Plot 1: Top scoring prompts
    top_data = filter_top_scoring(data)
    plot_grouped_scores(
        top_data,
        title="Top 10 Valid Business Prompts (LLM Score Breakdown)",
        save_path="outputs/top_scores_plot.png"
    )

    # Plot 2: Blocked edge cases
    blocked_data = filter_blocked(data)
    if blocked_data:
        plot_grouped_scores(
            blocked_data,
            title="Blocked Prompts – Inappropriate or Unsafe Content",
            save_path="outputs/blocked_scores_plot.png"
        )
    else:
        print("No blocked prompts found.")
