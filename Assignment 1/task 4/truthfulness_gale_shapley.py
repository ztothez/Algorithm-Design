"""
Truthfulness in Gale–Shapley for Algorithm Design Assignment 1, Question 4.

Counterexample: a woman on the receiving side improves her true outcome
by swapping two low-ranked men on her reported preference list.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gale_shapley import engagements_to_man_woman, format_matching, gale_shapley


def main():
    men_prefs = {
        "Albus": ["Xena", "Yvonne", "Zoe"],
        "Brian": ["Xena", "Zoe", "Yvonne"],
        "Conan": ["Yvonne", "Xena", "Zoe"],
    }
    women_true = {
        "Xena": ["Conan", "Albus", "Brian"],
        "Yvonne": ["Albus", "Conan", "Brian"],
        "Zoe": ["Albus", "Brian", "Conan"],
    }
    women_lie = {
        **women_true,
        "Xena": ["Conan", "Brian", "Albus"],
    }

    truthful = engagements_to_man_woman(
        gale_shapley(men_prefs, women_true), proposers_are_men=True
    )
    lying = engagements_to_man_woman(
        gale_shapley(men_prefs, women_lie), proposers_are_men=True
    )

    xena_truth = next(m for m, w in truthful.items() if w == "Xena")
    xena_lie = next(m for m, w in lying.items() if w == "Xena")

    print("--- Question 4 Results ---")
    print("Setup: men propose. Xena is the only liar.")
    print("True prefs for Xena:  Conan ≻ Albus ≻ Brian  (m'' ≻ m ≻ m')")
    print("False prefs for Xena: Conan ≻ Brian ≻ Albus  (swap m and m')")
    print()
    print(f"Truthful G-S matching: {format_matching(truthful)}")
    print(f"  → Xena matched with: {xena_truth}")
    print(f"Lying G-S matching:    {format_matching(lying)}")
    print(f"  → Xena matched with: {xena_lie}")
    print("-" * 30)

    true_rank = women_true["Xena"]
    if true_rank.index(xena_lie) < true_rank.index(xena_truth):
        print(
            "Conclusion: Lying improved Xena's partner in her TRUE preferences "
            f"({xena_truth} → {xena_lie})."
        )
        print(f"She truly prefers {xena_lie} over both Albus and Brian.")
    else:
        print("Conclusion: Lying did not improve Xena's true outcome.")
    print()


if __name__ == "__main__":
    main()
