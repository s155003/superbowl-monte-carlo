import numpy as np
import matplotlib.pyplot as plt

teams = {
    "Seattle Seahawks": {
        "avg_points_scored": 36.0,
        "avg_points_allowed": 16.5,
        "std_dev": 9.0,
        "color": "#002244"
    },
    "New England Patriots": {
        "avg_points_scored": 18.0,
        "avg_points_allowed": 8.7,
        "std_dev": 7.5,
        "color": "#C60C30"
    }
}

def simulate_game(team_a_stats, team_b_stats):
    expected_a = (team_a_stats["avg_points_scored"] + team_b_stats["avg_points_allowed"]) / 2
    expected_b = (team_b_stats["avg_points_scored"] + team_a_stats["avg_points_allowed"]) / 2
    score_a = max(0, np.random.normal(expected_a, team_a_stats["std_dev"]))
    score_b = max(0, np.random.normal(expected_b, team_b_stats["std_dev"]))
    if round(score_a) == round(score_b):
        if np.random.random() > 0.5:
            score_a += 3
        else:
            score_b += 3
    return score_a, score_b

NUM_SIMULATIONS = 100_000

sea_stats = teams["Seattle Seahawks"]
ne_stats  = teams["New England Patriots"]

sea_wins   = 0
ne_wins    = 0
sea_scores = []
ne_scores  = []
margins    = []

print(f"Running {NUM_SIMULATIONS:,} simulated Super Bowls...")

for _ in range(NUM_SIMULATIONS):
    sea_score, ne_score = simulate_game(sea_stats, ne_stats)
    sea_scores.append(sea_score)
    ne_scores.append(ne_score)
    margins.append(sea_score - ne_score)
    if sea_score > ne_score:
        sea_wins += 1
    else:
        ne_wins += 1

sea_win_pct = sea_wins / NUM_SIMULATIONS * 100
ne_win_pct  = ne_wins  / NUM_SIMULATIONS * 100

print(f"\n{'='*45}")
print(f"  SUPER BOWL LX SIMULATION RESULTS")
print(f"{'='*45}")
print(f"  Seattle Seahawks:     {sea_win_pct:.1f}% win probability")
print(f"  New England Patriots: {ne_win_pct:.1f}% win probability")
print(f"\n  Avg simulated score:")
print(f"  SEA {np.mean(sea_scores):.1f}  -  NE {np.mean(ne_scores):.1f}")
print(f"\n  Actual result: SEA 29  -  NE 13")
print(f"{'='*45}")

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("Super Bowl LX — Monte Carlo Simulation (100,000 games)", fontsize=14)

ax1 = axes[0]
wedges, texts, autotexts = ax1.pie(
    [sea_win_pct, ne_win_pct],
    labels=["Seattle\nSeahawks", "New England\nPatriots"],
    autopct='%1.1f%%',
    colors=[sea_stats["color"], ne_stats["color"]],
    startangle=90,
    textprops={"color": "white", "fontsize": 11}
)
for text in texts:
    text.set_color("black")
ax1.set_title("Win Probability", fontsize=13)

ax2 = axes[1]
ax2.hist(sea_scores, bins=50, alpha=0.6, color=sea_stats["color"], label="Seattle Seahawks", density=True)
ax2.hist(ne_scores,  bins=50, alpha=0.6, color=ne_stats["color"],  label="New England Patriots", density=True)
ax2.axvline(29, color=sea_stats["color"], linestyle="--", linewidth=2, label="Actual SEA score (29)")
ax2.axvline(13, color=ne_stats["color"],  linestyle="--", linewidth=2, label="Actual NE score (13)")
ax2.set_xlabel("Points Scored")
ax2.set_ylabel("Frequency")
ax2.set_title("Score Distribution")
ax2.legend(fontsize=8)

ax3 = axes[2]
ax3.hist(margins, bins=60, color="#888888", alpha=0.7, density=True)
ax3.axvline(0,  color="black", linewidth=2, linestyle="-",  label="Even game")
ax3.axvline(16, color=sea_stats["color"], linewidth=2, linestyle="--", label="Actual margin (+16 SEA)")
ax3.axvline(np.mean(margins), color="orange", linewidth=2, linestyle="--", label=f"Avg margin ({np.mean(margins):.1f})")
ax3.set_xlabel("Score Margin (positive = SEA wins)")
ax3.set_ylabel("Frequency")
ax3.set_title("Margin of Victory")
ax3.legend(fontsize=8)

plt.tight_layout()
plt.show()

print(f"\nExtra Stats from {NUM_SIMULATIONS:,} simulations:")
print(f"  Closest simulated game:  SEA margin of {min(margins):.1f} pts")
print(f"  Biggest SEA blowout:     +{max(margins):.1f} pts")
print(f"  Games within 7 pts:      {sum(abs(m) < 7 for m in margins)/NUM_SIMULATIONS*100:.1f}%")
print(f"  SEA wins by 10+:         {sum(m > 10 for m in margins)/NUM_SIMULATIONS*100:.1f}%")
print(f"  Actual result (SEA +16) was in the {sum(m < 16 for m in margins)/NUM_SIMULATIONS*100:.1f}th percentile")
