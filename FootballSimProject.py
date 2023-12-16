import random
from itertools import combinations

# Number of seasons to sim
number_of_series = 1

# Keep track of total number of league wins for each team
league_wins_per_team = {'Athletic Club': 0, 'Atlético Madrid': 0, 'CA Osasuna': 0, 'Cádiz CF': 0,
                        'Deportivo Alavés': 0, 'FC Barcelona': 0, 'Getafe CF': 0, 'Girona FC': 0,
                        'Granada CF': 0, 'Rayo Vallecano': 0, 'Celta de Vigo': 0, 'RCD Mallorca': 0,
                        'Real Betis': 0, 'Real Madrid': 0, 'Real Sociedad': 0, 'Sevilla FC': 0,
                        'UD Almería': 0, 'UD Las Palmas': 0, 'Valencia CF': 0, 'Villareal CF': 0}

for serie_num in range(1, number_of_series + 1):
    print(f'\n\n ----- Season {serie_num} -----')
    # Dictionary structure for each team
    # {'Pwr': , 'Played': , 'P': , 'W': , 'D': , 'L': , 'G': , 'GA': , 'Diff': }
    teams = {'Athletic Club': {'Pwr': 79, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Atlético Madrid': {'Pwr': 83, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'CA Osasuna': {'Pwr': 77, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Cádiz CF': {'Pwr': 74, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Deportivo Alavés': {'Pwr': 71, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'FC Barcelona': {'Pwr': 84, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Getafe CF': {'Pwr': 76, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Girona FC': {'Pwr': 76, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Granada CF': {'Pwr': 74, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Rayo Vallecano': {'Pwr': 77, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Celta de Vigo': {'Pwr': 76, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'RCD Mallorca': {'Pwr': 76, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Real Betis': {'Pwr': 80, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Real Madrid': {'Pwr': 85, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Real Sociedad': {'Pwr': 80, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Sevilla FC': {'Pwr': 80, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'UD Almería': {'Pwr': 74, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'UD Las Palmas': {'Pwr': 73, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Valencia CF': {'Pwr': 75, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0},
             'Villareal CF': {'Pwr': 79, 'Played': 0, 'P': 0, 'W': 0, 'D': 0, 'L': 0, 'G': 0, 'GA': 0, 'Diff': 0}}

    # Create list with possible matchings
    matchings = list(combinations(teams.keys(), 2))

    # Shuffle the list
    random.shuffle(matchings)

    # Simple match simulator
    def simulate_match(team1, team2):
        # Get power from dictionary for each team
        team1_power = teams[team1]['Pwr']
        team2_power = teams[team2]['Pwr']
        # Generating goals based on power
        team1_goals = random.randint(0, 4) * (team1_power / 100)
        team2_goals = random.randint(0, 4) * (team2_power / 100)
        # Rounding to whole number
        team1_goals = round(team1_goals)
        team2_goals = round(team2_goals)

        return team1_goals, team2_goals

    # Iterate the list of matches and simulate a match
    for match_num, match in enumerate(matchings, start=1):
        team1, team2 = match
        team1_score, team2_score = simulate_match(team1, team2)

        # Update matches played
        teams[team1]['Played'] += 1
        teams[team2]['Played'] += 1
        # Update goals scored/conceded
        teams[team1]['G'] += team1_score
        teams[team2]['G'] += team2_score
        teams[team1]['GA'] += team2_score
        teams[team2]['GA'] += team1_score
        # Update goal diff
        teams[team1]['Diff'] = teams[team1]['G'] - teams[team1]['GA']
        teams[team2]['Diff'] = teams[team2]['G'] - teams[team2]['GA']
        # Update points
        if team1_score > team2_score:
            teams[team1]['P'] += 3
            teams[team1]['W'] += 1
            teams[team2]['L'] += 1
        elif team2_score > team1_score:
            teams[team2]['P'] += 3
            teams[team2]['W'] += 1
            teams[team1]['L'] += 1
        else:
            teams[team1]['P'] += 1
            teams[team1]['D'] += 1
            teams[team2]['P'] += 1
            teams[team2]['D'] += 1

    # Sort dictionary based on points
    teams = dict(sorted(teams.items(), key=lambda x: x[1]['P'], reverse=True))

    print(f'{"TEAM".ljust(17)}GP  P   W   L   D   GF  GA  DIFF')
    for team, data in teams.items():
        print(f'{team.ljust(17)}' +
              f'{str(data["Played"]).ljust(4)}' +
              f'{str(data["P"]).ljust(4)}' +
              f'{str(data["W"]).ljust(4)}' +
              f'{str(data["L"]).ljust(4)}' +
              f'{str(data["D"]).ljust(4)}' +
              f'{str(data["G"]).ljust(4)}' +
              f'{str(data["GA"]).ljust(4)}' +
              f'{str(data["Diff"]).ljust(4)}')

    winner = list(teams.keys())[0]
    if teams[list(teams.keys())[1]]['P'] > teams[winner]['P']:
        winner = list(teams.keys())[1]

    print(f'--------------- Winner: {winner}')
    league_wins_per_team[winner] += 1

# Print team league win statistics
print('\nLeague wins:')
for team, wins in league_wins_per_team.items():
    print(f'{team.ljust(17)} {wins} wins')
