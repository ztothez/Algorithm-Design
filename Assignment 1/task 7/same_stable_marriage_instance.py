def gale_shapley(proposers_prefs, acceptors_prefs):
    """Classic Gale-Shapley algorithm implementation."""
    free_proposers = list(proposers_prefs.keys())
    engagements = {}  # acceptor -> proposer
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

def check_stability(matching, men_prefs, women_prefs):
    """Returns True if the matching contains no blocking pairs."""
    # Reverse lookup for women to find their assigned man
    women_partners = {w: m for m, w in matching.items()}
    
    for m in men_prefs:
        m_curr_w = matching[m]
        m_pref_list = men_prefs[m]
        
        # Check all women this man prefers over his current partner
        for w in m_pref_list:
            if w == m_curr_w:
                break  # Reached current partner; everything past this is worse
                
            w_curr_m = women_partners[w]
            w_pref_list = women_prefs[w]
            
            # If the preferred woman also prefers this man over her current partner...
            if w_pref_list.index(m) < w_pref_list.index(w_curr_m):
                print(f"  > Instability found: Man {m} and Woman {w} prefer each other!")
                return False
    return True

# 1. Define preference arrays matching your specific task layout
men_prefs = {
    0: [0, 1, 2, 3],
    1: [0, 2, 1, 3],
    2: [1, 0, 2, 3],
    3: [3, 2, 0, 1]
}

women_prefs = {
    0: [3, 2, 0, 1],
    1: [2, 3, 0, 1],
    2: [2, 0, 3, 1],
    3: [1, 0, 2, 3]
}

# 2. Compute M (Man-optimal matching)
m_raw = gale_shapley(men_prefs, women_prefs)
M = {m: w for w, m in m_raw.items()}

# 3. Compute M' (Woman-optimal matching)
m_prime_raw = gale_shapley(women_prefs, men_prefs)
M_prime = {m: w for m, w in m_prime_raw.items()}

print("Matching M  (Man-optimal): ", M)
print("Matching M' (Woman-optimal):", M_prime)
print("-" * 60)

# 4. Construct M'' (Every man gets his preferred choice between M and M')
M_double_prime = {}
for m in men_prefs:
    w_in_M = M[m]
    w_in_M_prime = M_prime[m]
    
    # Check which woman has a better index position (lower is better)
    if men_prefs[m].index(w_in_M) <= men_prefs[m].index(w_in_M_prime):
        M_double_prime[m] = w_in_M
    else:
        M_double_prime[m] = w_in_M_prime

print("Constructed Matching M'':   ", M_double_prime)

# 5. Programmatic Verification
# Check 1: Is it a valid matching? (Every woman must appear exactly once)
matched_women = list(M_double_prime.values())
is_valid_matching = len(matched_women) == len(set(matched_women))

# Check 2: Is it mathematically stable?
is_stable = check_stability(M_double_prime, men_prefs, women_prefs)

print("\n--- Formal Proof Verification Results ---")
print(f"Is M'' a valid matching? (No overlapping partners): {is_valid_matching}")
print(f"Is M'' mathematically stable?                       : {is_stable}")