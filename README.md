# 🏈 Super Bowl LX — Monte Carlo Simulation

A Python simulation that uses the **Monte Carlo method** to predict the outcome of Super Bowl LX between the **Seattle Seahawks** and the **New England Patriots**. By running 100,000 randomized game simulations based on real playoff statistics, the model generates win probabilities, expected scores, and margin of victory distributions.

---

## What is a Monte Carlo Simulation?

A Monte Carlo simulation is a computational technique that runs thousands of random "what if" scenarios to determine the range of possible outcomes for an uncertain event. Rather than predicting a single result, it maps out the full landscape of possibilities — giving us a probability distribution instead of just one answer.

In the context of this project, instead of saying "Seattle will win by X points," we simulate 100,000 complete games, each with slightly different random outcomes, and ask: *across all of those games, who wins more often, and by how much?*

---

## How It Works

Each simulated game works as follows:

1. **Expected score** for each team is calculated by blending their offensive output (average points scored in the playoffs) with the opponent's defensive strength (average points allowed).
2. **Randomness is added** by sampling from a normal distribution centered on that expected score — mimicking the natural variance of real NFL games.
3. **A winner is determined** for each simulation. Tied games go to overtime, decided by a coin flip (field goal).
4. This repeats **100,000 times**, and the results are aggregated to produce win probabilities, average scores, and scoring margins.

---

## Stats Used

| Team | Avg Points Scored | Avg Points Allowed | Playoff Results |
|---|---|---|---|
| Seattle Seahawks | 36.0 | 16.5 | W 41–6, W 31–27 |
| New England Patriots | 18.0 | 8.7 | W 16–3, W 28–16, W 10–7 |


## Customization

Want to simulate a different matchup? Just update the `teams` dictionary at the top of the script with any two teams' average points scored and allowed, adjust the `std_dev` to reflect how consistent each team is, and re-run.
