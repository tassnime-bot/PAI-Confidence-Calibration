from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results" / "calibration_bins.csv"
OUT = ROOT / "calibration_comparison.png"

df = pd.read_csv(DATA)

fig, ax = plt.subplots(figsize=(8.5, 6.0))
ax.plot([0, 1], [0, 1], linestyle="--", label="Perfect calibration")

for dataset, marker in [("Development (150)", "o"), ("Locked test (50)", "s")]:
    sub = df[df["dataset"] == dataset].copy()
    sub = sub.dropna(subset=["mean_confidence_percent", "accuracy_percent"])
    x = sub["mean_confidence_percent"] / 100
    y = sub["accuracy_percent"] / 100
    ax.plot(x, y, marker=marker, linewidth=2, label=dataset)

ax.set_xlim(0.50, 1.00)
ax.set_ylim(0.00, 1.05)
ax.set_xlabel("Mean reported confidence")
ax.set_ylabel("Observed accuracy")
ax.set_title("AI Confidence Calibration")
ax.grid(True, alpha=0.25)
ax.legend()
fig.tight_layout()
fig.savefig(OUT, dpi=220)
plt.close(fig)
print(f"Saved {OUT}")
