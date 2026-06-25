def gale_shapley(proposers_prefs, acceptors_prefs):
    free_proposers = list(proposers_prefs.keys())
    engagements = {} # acceptor -> proposer
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

# --- Define preferences where M and M' will definitely be different ---
# 3 Men (0,1,2), 3 Women (0,1,2)
men_prefs = {
    0: [0, 1, 2],
    1: [1, 2, 0],
    2: [2, 0, 1]
}
women_prefs = {
    0: [1, 2, 0],
    1: [2, 0, 1],
    2: [0, 1, 2]
}

# Matching M (Man Proposes)
m_raw = gale_shapley(men_prefs, women_prefs)
M = {m: w for w, m in m_raw.items()} # Man -> Woman

# Matching M' (Woman Proposes)
m_prime_raw = gale_shapley(women_prefs, men_prefs)
M_prime = {m: w for m, w in m_prime_raw.items()} # Man -> Woman

print("Matching M  (Man-optimal): ", M)
print("Matching M' (Woman-optimal):", M_prime)
print("-" * 50)

# Verify the property: pick man 0 and woman 0 (partners in M, but not in M')
m, w = 0, 0
partner_in_M = M[m]         # Woman 0
partner_in_M_prime = M_prime[m]   # Woman 1

print(f"In Matching M, Man {m} is with Woman {M[m]}")
print(f"In Matching M', Man {m} is with Woman {M_prime[m]}")

# Check Man 0's preference hierarchy (lower index = prefers more)
man_pref_M = men_prefs[m].index(M[m])
man_pref_M_prime = men_prefs[m].index(M_prime[m])

# Check Woman 0's preference hierarchy 
# In M her partner is Man 0. In M' her partner is found by reversing M_prime dict:
w_partner_M_prime = [k for k, v in M_prime.items() if v == w][0]
woman_pref_M = women_prefs[w].index(m)
woman_pref_M_prime = women_prefs[w].index(w_partner_M_prime)

print("\n--- Preference Verification ---")
if man_pref_M < man_pref_M_prime:
    print(f"-> Man {m} prefers Matching M over M'")
else:
    print(f"-> Man {m} prefers Matching M' over M")

if woman_pref_M < woman_pref_M_prime:
    print(f"-> Woman {w} prefers Matching M over M'")
else:
    print(f"-> Woman {w} prefers Matching M' over M")