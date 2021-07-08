import copy
from typing import Dict, List
import gale_shapley_algorithm


def sp_algorithm(original_schedules):
    # Creating a list of preferences for each ship
    ships_preferences = copy.deepcopy(original_schedules)    # Copy of the dictionary, independent of the original
    for ship in ships_preferences.keys():                    # Removing marks for sailing ('--') from the schedules
        while '--' in ships_preferences[ship]:               # Ships might sail more than one day
            ships_preferences[ship].remove('--')

    # Creating a list of preferences for each port
    one_ship = list(ships_preferences.keys())[0]        # Fetching ship from the index 0 - certainly exists
    ports_fetched = ships_preferences[one_ship]         # Ships list of preferences contains names of the ports only
    ports_preferences: Dict[str, List[str]] = {}
    for port in ports_fetched:                          # Fetching names of the ports
        ports_preferences[port]: List[str] = []         # Ports list of preferences initialized as an empty lists

    # Marks m and n match to the task;
    # m represents number of days during the ships journey, according to original schedules;
    # n represents number of ships and ports
    original_schedule = original_schedules[one_ship]
    m = len(original_schedule)
    shortened_schedule = ships_preferences[one_ship]
    n = len(shortened_schedule)
    for port in ports_preferences.keys():
        for i in reversed(range(m)):                       # No two ships can be in the same port on the same day
            if len(ports_preferences[port]) == n:
                break
            for ship in ships_preferences.keys():
                if original_schedules[ship][i] == port:
                    ports_preferences[port].append(ship)
                    break

    # Using the Gale-Shapley algorithm on created lists of preferences
    matching = gale_shapley_algorithm.gs_algorithm(ships_preferences, ports_preferences)

    # Creating shortened schedules of ships by using matching
    shortened_schedules: Dict[str, List[str]] = {}
    for ship in matching:
        port = matching[ship]
        port_index = original_schedules[ship].index(port)
        shortened_schedule = original_schedules[ship][:port_index + 1]
        shortened_schedules[ship] = shortened_schedule

    return shortened_schedules


def comparison(original_schedules, shortened_schedules):
    # Sorted print of original schedules
    print('- original schedules:')
    for j in sorted(original_schedules.keys()):
        print(f"\tship {j}: {original_schedules[j]}")

    # Sorted print of shortened schedules
    print('\n- shortened schedules:')
    for k in sorted(shortened_schedules.keys()):
        print(f"\tship {k}: {shortened_schedules[k]}")


# Input data: original schedules of the ships
# Structure: dictionary
# Problem from the thesis, Example 4.1.2.
# Output stored in sp_example_1.txt
original_ships_schedules: Dict[str, List[str]] = {
    's1': ['p1', '--', 'p2', 'p3'],
    's2': ['p2', 'p3', '--', 'p1'],
    's3': ['--', 'p1', 'p3', 'p2']
}

# Ship-Port algorithm
#shortened_ships_schedules = sp_algorithm(original_ships_schedules)
# Comparing original schedules and shortened
#comparison(original_ships_schedules, shortened_ships_schedules)


# Problem from the book Introduction to Algorithms, J. Kleinberg and E.Tardos
# Reference [5] in the thesis
# Output stored in sp_example_2.txt
original_ships_schedules_task_example: Dict[str, List[str]] = {
     's1': ['p1', '--', 'p2', '--'],
     's2': ['--', 'p1', '--', 'p2']
}
# shortened_ships_schedules = sp_algorithm(original_ships_schedules_task_example)
# comparison(original_ships_schedules_task_example, shortened_ships_schedules)

# Problem
# Output stored in sp_example_3.txt
original_ships_schedules_example: Dict[str, List[str]] = {
    's1': ['--', 'p1', '--', 'p2', 'p3', 'p4', 'p6', 'p5'],
    's2': ['p2', 'p3', '--', 'p1', 'p6', 'p5', 'p4', '--'],
    's3': ['p3', 'p4', 'p6', 'p5', '--', '--', 'p1', 'p2'],
    's4': ['p5', 'p6', 'p2', 'p3', '--', 'p1', '--', 'p4'],
    's5': ['--', '--', 'p1', 'p4', 'p5', 'p6', 'p2', 'p3'],
    's6': ['p6', '--', 'p3', '--', 'p4', 'p2', 'p5', 'p1']
}
# shortened_ships_schedules = sp_algorithm(original_ships_schedules_example)
# comparison(original_ships_schedules_example, shortened_ships_schedules)
