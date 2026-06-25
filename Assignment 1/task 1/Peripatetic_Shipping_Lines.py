"""
Peripatetic Shipping Lines Problem - Exercise 1-6
Algorithm Design by Jon Kleinberg and Éva Tardos

Reduce to stable matching (ships ↔ stopping ports), then run Gale-Shapley.
"""

def build_preferences(ships_schedules):
    """Build ship and port preference lists for the stable matching instance."""
    n = len(ships_schedules)

    # ship_visits[i] = [(day, port), ...] in chronological order
    ship_visits = []
    for schedule in ships_schedules:
        visits = [(day, loc) for day, loc in enumerate(schedule) if loc != "at sea"]
        ship_visits.append(visits)

    # Each ship ranks ports in chronological visit order.
    ship_prefs = [[port for _, port in visits] for visits in ship_visits]

    # Each port ranks ships in reverse chronological visit order.
    port_visits = {}
    for ship_idx, visits in enumerate(ship_visits):
        for day, port in visits:
            port_visits.setdefault(port, []).append((day, ship_idx))

    port_prefs = {
        port: [ship for _, ship in sorted(visits, key=lambda x: x[0], reverse=True)]
        for port, visits in port_visits.items()
    }

    # day when ship i visits port p
    visit_day = {}
    for ship_idx, visits in enumerate(ship_visits):
        for day, port in visits:
            visit_day[(ship_idx, port)] = day

    return ship_prefs, port_prefs, visit_day, n


def gale_shapley(ship_prefs, port_prefs):
    """Gale-Shapley with ships proposing. Returns ship_idx -> matched port."""
    n = len(ship_prefs)
    free_ships = list(range(n))
    ship_match = {}
    port_match = {}
    next_proposal = [0] * n

    while free_ships:
        ship = free_ships.pop(0)
        port = ship_prefs[ship][next_proposal[ship]]
        next_proposal[ship] += 1

        if port not in port_match:
            ship_match[ship] = port
            port_match[port] = ship
            continue

        current = port_match[port]
        if port_prefs[port].index(ship) < port_prefs[port].index(current):
            ship_match[ship] = port
            port_match[port] = ship
            del ship_match[current]
            free_ships.append(current)
        else:
            free_ships.append(ship)

    return ship_match

def truncate_from_matching(ships_schedules, ship_match, visit_day):
    """Truncate each ship on the day it visits its matched stopping port."""
    m = len(ships_schedules[0])
    truncated_schedules = []

    for ship_idx, schedule in enumerate(ships_schedules):
        port = ship_match[ship_idx]
        day = visit_day[(ship_idx, port)]
        truncated = schedule[: day + 1] + [port] * (m - day - 1)
        truncated_schedules.append(truncated)

    return truncated_schedules


def truncate_ship_schedules(ships_schedules):
    """
    Find valid truncations via stable matching + Gale-Shapley.

    Time: O(nm) to build preferences, O(n^2) for Gale-Shapley.
    """
    ship_prefs, port_prefs, visit_day, _ = build_preferences(ships_schedules)
    ship_match = gale_shapley(ship_prefs, port_prefs)
    return truncate_from_matching(ships_schedules, ship_match, visit_day)


def truncate_ship_schedules_backtrack(ships_schedules):
    """Exhaustive search — exponential, used only to validate small instances."""
    n = len(ships_schedules)
    m = len(ships_schedules[0])
    truncation_days = [None] * n

    def is_valid_truncation(candidate):
        truncated = []
        for i, schedule in enumerate(ships_schedules):
            day = candidate[i]
            port = schedule[day]
            truncated.append(schedule[: day + 1] + [port] * (m - day - 1))

        for day in range(m):
            ports_today = set()
            for schedule in truncated:
                port = schedule[day]
                if port != "at sea":
                    if port in ports_today:
                        return False
                    ports_today.add(port)
        return True

    def backtrack(ship_idx):
        if ship_idx == n:
            return is_valid_truncation(truncation_days)

        for day, port in enumerate(ships_schedules[ship_idx]):
            if port == "at sea":
                continue
            truncation_days[ship_idx] = day
            if backtrack(ship_idx + 1):
                return True
            truncation_days[ship_idx] = None
        return False

    if not backtrack(0):
        raise ValueError("No valid truncation exists")

    return truncate_from_matching(
        ships_schedules,
        {
            i: ships_schedules[i][truncation_days[i]]
            for i in range(n)
        },
        {
            (i, ships_schedules[i][truncation_days[i]]): truncation_days[i]
            for i in range(n)
        },
    )


def print_schedules(original, truncated, label=""):
    if label:
        print(f"\n{label}")
    print("=" * 70)
    for i, (orig, trunc) in enumerate(zip(original, truncated)):
        print(f"Ship {i + 1}:")
        print(f"  Original:  {orig}")
        print(f"  Truncated: {trunc}")


def verify_no_conflicts(truncated_schedules):
    m = len(truncated_schedules[0])

    for day in range(m):
        ports_today = {}
        for ship_idx, schedule in enumerate(truncated_schedules):
            port = schedule[day]
            if port != "at sea":
                if port in ports_today:
                    print(
                        f"ERROR: Day {day}, Port {port} occupied by both "
                        f"Ship {ports_today[port] + 1} and Ship {ship_idx + 1}"
                    )
                    return False
                ports_today[port] = ship_idx

    print("✓ Valid: No conflicts. Each port has at most one ship per day.")
    return True


def run_test(name, ships):
    print(f"\n{name}")
    print("-" * 70)
    print("Original schedules:")
    for i, sched in enumerate(ships):
        print(f"  Ship {i + 1}: {sched}")

    result = truncate_ship_schedules(ships)
    print_schedules(ships, result, "Solution (Gale-Shapley / Stable Matching):")
    if not verify_no_conflicts(result):
        raise AssertionError(f"{name} failed conflict check")

    # Independent validator on small inputs
    backtrack_result = truncate_ship_schedules_backtrack(ships)
    if not verify_no_conflicts(backtrack_result):
        raise AssertionError(f"{name} backtracking validator failed")


if __name__ == "__main__":
    print("PERIPATETIC SHIPPING LINES - Problem 1-6")
    print("=" * 70)

    run_test(
        "TEST 1: Textbook Example (2 ships, 2 ports, 4 days)",
        [
            ["P1", "at sea", "P2", "at sea"],
            ["at sea", "P1", "at sea", "P2"],
        ],
    )

    run_test(
        "TEST 2: Three Ships, Three Ports, Five Days",
        [
            ["P1", "at sea", "P2", "at sea", "P3"],
            ["P2", "at sea", "P3", "at sea", "P1"],
            ["at sea", "P3", "at sea", "P1", "P2"],
        ],
    )

    run_test(
        "TEST 3: Minimal Case (2 ships, 2 ports, 2 days)",
        [
            ["P1", "P2"],
            ["P2", "P1"],
        ],
    )

    print("\n" + "=" * 70)
    print("All tests passed! ✓\n")
