import random
from typing import Dict, List


def gs_algorithm(preferences_men, preferences_women):
    matching: Dict[str, str] = {}

    # All men and women are free: fact that women are free ain't relevant,
    # fact that no man hadn't propose any woman is relevant
    free_men: List[str] = []
    proposals: Dict[str, int] = {}
    for man in preferences_men.keys():
        free_men.append(man)
        proposals[man] = 0       # Index of the first woman to propose

    first_man = list(preferences_men.keys())[0]
    out_of_range_index = len(preferences_men[first_man])
    iterations_counter = 1       # Not necessary, useful for tracking actions in each iteration of while loop
    not_propose_to_all_women = all(proposals[man] < out_of_range_index for man in free_men)
    while free_men and not_propose_to_all_women:
        potential_fiance = random.choice(free_men)
        woman_index = proposals[potential_fiance]
        proposals[potential_fiance] += 1
        potential_fiance_preferences = preferences_men[potential_fiance]
        woman_to_propose = potential_fiance_preferences[woman_index]

        if woman_to_propose not in matching.values():
            matching[potential_fiance] = woman_to_propose
            free_men.remove(potential_fiance)
        else:
            current_fiance = list(matching.keys())[list(
                matching.values()).index(woman_to_propose)]
            woman_to_propose_pref = preferences_women[woman_to_propose]
            current_fiance_index = woman_to_propose_pref.index(current_fiance)
            potential_fiance_index = woman_to_propose_pref.index(potential_fiance)

            if current_fiance_index < potential_fiance_index:
                pass
            else:
                matching.pop(current_fiance)
                matching[potential_fiance] = woman_to_propose
                free_men.remove(potential_fiance)
                free_men.append(current_fiance)

        iterations_counter += 1
        not_propose_to_all_women = all(proposals[men] <
                                       out_of_range_index for men in free_men)

    return matching


# Input data: men, women and their preferences;
# structure: dictionary (unordered and changeable)

# Stable matching problem from the thesis, Example 2.2.8.
# Output stored in gs_example_1.txt
men_first: Dict[str, List[str]] = {
    'm1': ['w1', 'w3', 'w2', 'w4'],
    'm2': ['w3', 'w4', 'w1', 'w2'],
    'm3': ['w4', 'w2', 'w3', 'w1'],
    'm4': ['w4', 'w2', 'w1', 'w3']
}

women_first: Dict[str, List[str]] = {
    'w1': ['m2', 'm4', 'm3', 'm1'],
    'w2': ['m4', 'm3', 'm1', 'm2'],
    'w3': ['m1', 'm4', 'm2', 'm3'],
    'w4': ['m4', 'm1', 'm2', 'm3']
}

"""matching = gs_algorithm(men_first, women_first)
for i in sorted(matching.keys()):
    print(f"\t({i}, {matching[i]})")"""


# Stable matching problem from the article The Stable Matching Problem, D.G. McVitie and L.B. Wilson
# Reference [6] in the thesis
# Output stored in gs_example_2.txt
men_second: Dict[str, List[str]] = {
    'm1': ['w5', 'w7', 'w1', 'w2', 'w6', 'w8', 'w4', 'w3'],
    'm2': ['w2', 'w3', 'w7', 'w5', 'w4', 'w1', 'w8', 'w6'],
    'm3': ['w8', 'w5', 'w1', 'w4', 'w6', 'w2', 'w3', 'w7'],
    'm4': ['w3', 'w2', 'w7', 'w4', 'w1', 'w6', 'w8', 'w5'],
    'm5': ['w7', 'w2', 'w5', 'w1', 'w3', 'w6', 'w8', 'w4'],
    'm6': ['w1', 'w6', 'w7', 'w5', 'w8', 'w4', 'w2', 'w3'],
    'm7': ['w2', 'w5', 'w7', 'w6', 'w3', 'w4', 'w8', 'w1'],
    'm8': ['w3', 'w8', 'w4', 'w5', 'w7', 'w2', 'w6', 'w1']
}

women_second: Dict[str, List[str]] = {
    'w1': ['m5', 'm3', 'm7', 'm6', 'm1', 'm2', 'm8', 'm4'],
    'w2': ['m8', 'm6', 'm3', 'm5', 'm7', 'm2', 'm1', 'm4'],
    'w3': ['m1', 'm5', 'm6', 'm2', 'm4', 'm8', 'm7', 'm3'],
    'w4': ['m8', 'm7', 'm3', 'm2', 'm4', 'm1', 'm5', 'm6'],
    'w5': ['m6', 'm4', 'm7', 'm3', 'm8', 'm1', 'm2', 'm5'],
    'w6': ['m2', 'm8', 'm5', 'm4', 'm6', 'm3', 'm7', 'm1'],
    'w7': ['m7', 'm5', 'm2', 'm1', 'm8', 'm6', 'm4', 'm3'],
    'w8': ['m7', 'm4', 'm1', 'm5', 'm2', 'm3', 'm6', 'm8']
}

"""matching = gs_algorithm(men_second, women_second)
for i in sorted(matching.keys()):
    print(f"\t({i}, {matching[i]})")"""
