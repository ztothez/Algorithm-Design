"""
Gale–Shapley Algorithm - Assignment 1, Question 2
Algorithm Design by Jon Kleinberg and Éva Tardos

Man-optimal vs woman-optimal matchings; count all stable matchings for the instance.
"""

import sys
from itertools import permutations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gale_shapley import (
    engagements_to_man_woman,
    format_matching,
    gale_shapley,
    is_stable,
)


def main():
    men_prefs = {
        0: [0, 1, 2, 3],
        1: [0, 2, 1, 3],
        2: [1, 0, 2, 3],
        3: [3, 2, 0, 1],
    }
    women_prefs = {
        0: [3, 2, 0, 1],
        1: [2, 3, 0, 1],
        2: [2, 0, 3, 1],
        3: [1, 0, 2, 3],
    }

    m_optimal = engagements_to_man_woman(
        gale_shapley(men_prefs, women_prefs), proposers_are_men=True
    )
    w_optimal = engagements_to_man_woman(
        gale_shapley(women_prefs, men_prefs), proposers_are_men=False
    )

    print("--- Question 2 Results ---")
    print(f"Man-optimal matching (M):    {format_matching(m_optimal)}")
    print(f"Woman-optimal matching (M'): {format_matching(w_optimal)}")
    print("-" * 30)

    if m_optimal == w_optimal:
        print("Conclusion for b): M = M′ → exactly 1 stable matching.")
    else:
        print("Conclusion for b): M ≠ M′ → multiple stable matchings exist.")

    stable_matchings = []
    for perm in permutations(range(4)):
        match = {m: perm[m] for m in range(4)}
        if is_stable(match, men_prefs, women_prefs):
            stable_matchings.append(match)

    print(f"\nTotal stable matchings: {len(stable_matchings)}")
    for i, s in enumerate(stable_matchings, 1):
        print(f"  {i}. {format_matching(s)}")
    print()


if __name__ == "__main__":
    main()
