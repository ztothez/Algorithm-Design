"""
Gale–Shapley Helpers - Assignment 1
Algorithm Design by Jon Kleinberg and Éva Tardos

Shared deferred-acceptance implementation for tasks 2 and 4.
"""


def gale_shapley(proposers_prefs, acceptors_prefs):
    """Return acceptor -> proposer engagements."""
    free_proposers = list(proposers_prefs.keys())
    engagements = {}
    proposal_index = {p: 0 for p in proposers_prefs}

    while free_proposers:
        proposer = free_proposers.pop(0)
        prefs = proposers_prefs[proposer]
        idx = proposal_index[proposer]

        if idx >= len(prefs):
            continue

        acceptor = prefs[idx]
        proposal_index[proposer] += 1

        if acceptor not in engagements:
            engagements[acceptor] = proposer
        else:
            current_partner = engagements[acceptor]
            acceptor_pref_list = acceptors_prefs[acceptor]

            if acceptor_pref_list.index(proposer) < acceptor_pref_list.index(current_partner):
                engagements[acceptor] = proposer
                free_proposers.append(current_partner)
            else:
                free_proposers.append(proposer)

    return engagements


def engagements_to_man_woman(engagements, proposers_are_men):
    """Convert acceptor->proposer map to man->woman pairs."""
    if proposers_are_men:
        return {m: w for w, m in engagements.items()}
    return {m: w for m, w in engagements.items()}


def format_matching(matching):
    parts = []
    for man, woman in sorted(matching.items()):
        if isinstance(man, str):
            parts.append(f"{man}-{woman}")
        else:
            parts.append(f"M{man + 1}-W{woman + 1}")
    return ", ".join(parts)


def is_stable(matching, men_prefs, women_prefs):
    men = list(men_prefs.keys())
    women = list(women_prefs.keys())
    for m in men:
        wm = matching[m]
        for w in women:
            if w == wm:
                continue
            partner = next(mm for mm, ww in matching.items() if ww == w)
            if (
                men_prefs[m].index(w) < men_prefs[m].index(wm)
                and women_prefs[w].index(m) < women_prefs[w].index(partner)
            ):
                return False
    return True
