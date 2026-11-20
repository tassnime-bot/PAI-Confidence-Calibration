
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

# Project paths
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results" / "calibration_bins.csv"
OUT = ROOT / "calibration_comparison.png"

if not DATA.exists():
    raise FileNotFoundError(f"Could not find: {DATA}")

df = pd.read_csv(DATA)

# Validate the actual CSV schema
required_columns = {
    "dataset",
    "confidence_band",
    "n",
    "mean_confidence_percent",
    "observed_accuracy_percent",
}

missing = required_columns - set(df.columns)
if missing:
    raise ValueError(
        f"Missing CSV columns: {sorted(missing)}\n"
        f"Available columns: {list(df.columns)}"
    )

# Convert numeric columns safely
for column in [
    "n",
    "mean_confidence_percent",
    "observed_accuracy_percent",
]:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# Match the dataset names actually stored in the CSV
datasets = [
    ("Development", "Development (150)", "o"),
    ("Locked holdout", "Locked test (50)", "s"),
]

fig, ax = plt.subplots(figsize=(9, 6.5))

# Perfect calibration reference
ax.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    linewidth=1.8,
    label="Perfect calibration"
)

for source_name, display_name, marker in datasets:
    subset = df[df["dataset"] == source_name].copy()

    subset = subset.dropna(
        subset=[
            "mean_confidence_percent",
            "observed_accuracy_percent",
            "n",
        ]
    )

    subset = subset[subset["n"] > 0]

    if subset.empty:
        raise ValueError(
            f"No valid calibration bins found for {source_name}"
        )

    x = subset["mean_confidence_percent"] / 100
    y = subset["observed_accuracy_percent"] / 100

    ax.plot(
        x,
        y,
        marker=marker,
        markersize=7,
        linewidth=2,
        label=display_name,
    )

    # Add sample counts beside each point
    for x_value, y_value, count in zip(x, y, subset["n"]):
        ax.annotate(
            f"n={int(count)}",
            (x_value, y_value),
            xytext=(5, 7),
            textcoords="offset points",
            fontsize=8,
        )

ax.set_xlim(0.50, 1.01)
ax.set_ylim(0.00, 1.05)

ax.xaxis.set_major_formatter(PercentFormatter(1))
ax.yaxis.set_major_formatter(PercentFormatter(1))

ax.set_xlabel("Mean reported confidence")
ax.set_ylabel("Observed accuracy")

ax.set_title("Does AI Confidence Behave Like Probability?")

ax.grid(True, alpha=0.25)
ax.legend(loc="lower right")

fig.tight_layout()
fig.savefig(OUT, dpi=250, bbox_inches="tight")
plt.close(fig)

print("SUCCESS!")
print("Chart saved to:", OUT)
print("Datasets plotted: Development and Locked holdout")
