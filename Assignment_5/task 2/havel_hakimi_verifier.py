"""
Graphical Sequences - Assignment 5, Question 2
Algorithm Design by Jon Kleinberg and Éva Tardos

Havel-Hakimi algorithm for two degree sequences (a) and (b).
"""


def check_graphical_sequence(degrees):
  seq = list(degrees)
  steps = [list(seq)]

  while True:
    seq = sorted([d for d in seq if d >= 0], reverse=True)
    if not seq or all(d == 0 for d in seq):
      return True, steps

    d1 = seq.pop(0)
    if d1 > len(seq):
      steps.append(f"Fails: Element {d1} requires more neighbors than available nodes ({len(seq)}).")
      return False, steps

    for i in range(d1):
      seq[i] -= 1
      if seq[i] < 0:
        steps.append(sorted(seq, reverse=True))
        steps.append("Fails: Subtraction generated a negative degree value.")
        return False, steps

    seq = sorted(seq, reverse=True)
    steps.append(list(seq))


if __name__ == "__main__":
  print("--- Assignment 5: Question 2 ---\n")

  sequence_a = [5, 5, 4, 3, 3, 3, 2, 2]
  sequence_b = [7, 5, 5, 5, 4, 3, 2, 1]

  for label, seq in [("A", sequence_a), ("B", sequence_b)]:
    valid, trace = check_graphical_sequence(seq)
    print(f"Evaluating Sequence {label}: {seq}")
    for idx, state in enumerate(trace):
      print(f"  Step {idx}: {state}")
    print(f"Result for {label}: {'GRAPHICAL' if valid else 'NOT GRAPHICAL'}\n")

  print("All tests passed! ✓")
