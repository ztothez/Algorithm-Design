'''
Question 2

a) The G-S algorithm favoring men's preferences is executed resulting in a man-optimal matching $M$. The same algorithm is executed again for the same instance but now favoring the women's preferences resulting in a woman-optimal matching $M'$. Show that if $M = M'$, then this matching is the only possible stable matching.

b) How many stable matchings there are for the given preference lists? Provide your solution with an explanation.

Preference Tables

Men's Preferences
| $M_1$ | $M_2$ | $M_3$ | $M_4$ |
| --- | --- | --- | --- |
| $W_1$ | $W_1$ | $W_2$ | $W_4$ |
| $W_2$ | $W_3$ | $W_1$ | $W_3$ |
| $W_3$ | $W_2$ | $W_3$ | $W_1$ |
| $W_4$ | $W_4$ | $W_4$ | $W_2$ |

Women's Preferences
| $W_1$ | $W_2$ | $W_3$ | $W_4$ |
| --- | --- | --- | --- |
| $M_4$ | $M_3$ | $M_3$ | $M_2$ |
| $M_3$ | $M_4$ | $M_1$ | $M_1$ |
| $M_1$ | $M_1$ | $M_4$ | $M_3$ |
| $M_2$ | $M_2$ | $M_2$ | $M_4$ |
'''

#solve A and B using pythonTo solve the problem, we can implement the Gale-Shapley algorithm

def gale_shapley(proposers_prefs, acceptors_prefs):
    """
    Generic Gale-Shapley implementation.
    proposers_prefs: dict where key is proposer ID, value is list of acceptor IDs in order of preference.
    acceptors_prefs: dict where key is acceptor ID, value is list of proposer IDs in order of preference.
    """
    # Initialize all proposers as free
    free_proposers = list(proposers_prefs.keys())
    
    # Track current engagements: acceptor -> proposer
    engagements = {}
    
    # Track the next preference index to propose to for each proposer
    proposal_index = {p: 0 for p in proposers_prefs}
    
    while free_proposers:
        proposer = free_proposers.pop(0)
        
        # Get the next preferred acceptor
        prefs = proposers_prefs[proposer]
        idx = proposal_index[proposer]
        
        if idx >= len(prefs):
            continue # No more options left for this proposer (shouldn't happen in standard NxN matching)
            
        acceptor = prefs[idx]
        proposal_index[proposer] += 1
        
        # Check if acceptor is free
        if acceptor not in engagements:
            engagements[acceptor] = proposer
        else:
            current_partner = engagements[acceptor]
            acceptor_pref_list = acceptors_prefs[acceptor]
            
            # Lower index means higher preference
            if acceptor_pref_list.index(proposer) < acceptor_pref_list.index(current_partner):
                engagements[acceptor] = proposer
                free_proposers.append(current_partner)
            else:
                free_proposers.append(proposer)
                
    return engagements

# --- Define the Preference Matrices from the Image ---
# Let M1=0, M2=1, M3=2, M4=3
# Let W1=0, W2=1, W3=2, W4=3

men_prefs = {
    0: [0, 1, 2, 3], # M1: W1, W2, W3, W4
    1: [0, 2, 1, 3], # M2: W1, W3, W2, W4
    2: [1, 0, 2, 3], # M3: W2, W1, W3, W4
    3: [3, 2, 0, 1]  # M4: W4, W3, W1, W2
}

women_prefs = {
    0: [3, 2, 0, 1], # W1: M4, M3, M1, M2
    1: [2, 3, 0, 1], # W2: M3, M4, M1, M2
    2: [2, 0, 3, 1], # W3: M3, M1, M4, M2
    3: [1, 0, 2, 3]  # W4: M2, M1, M3, M4
}

# 1. Men Propose (Man-Optimal Matching M)
m_optimal_raw = gale_shapley(men_prefs, women_prefs)
# Format to standard (Man -> Woman) pairs
m_optimal = {m: w for w, m in sorted(m_optimal_raw.items())}

# 2. Women Propose (Woman-Optimal Matching M')
w_optimal_raw = gale_shapley(women_prefs, men_prefs)
# Already man -> woman when women propose (acceptor = man, proposer = woman)
w_optimal = dict(w_optimal_raw)

# Format outputs nicely for readability (converting back to 1-indexed string format)
def format_matching(matching):
    return ", ".join([f"M{m+1}-W{w+1}" for m, w in sorted(matching.items())])

print("--- Results ---")
print(f"Man-optimal matching (M):    {format_matching(m_optimal)}")
print(f"Woman-optimal matching (M'):  {format_matching(w_optimal)}")
print("-" * 15)

if m_optimal == w_optimal:
    print("Conclusion for b): Since the man-optimal and woman-optimal matchings are identical,")
    print("there is exactly 1 stable matching for these preference lists.")
else:
    print("Conclusion for b): The matchings are different, implying multiple stable matchings exist.")