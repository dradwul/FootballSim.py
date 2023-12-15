import random
from itertools import combinations

# Number of seasons to sim
number_of_series = 100

# Keep track of total number of league wins for each team
league_wins_per_team = {'Athletic Club':0,'Atlético Madrid':0,'CA Osasuna':0,'Cádiz CF':0,
                        'Deportivo Alavés':0,'FC Barcelona':0,'Getafe CF':0,'Girona FC':0,
                        'Granada CF':0,'Rayo Vallecano':0,'Celta de Vigo':0,'RCD Mallorca':0,
                        'Real Betis':0,'Real Madrid':0,'Real Sociedad':0,'Sevilla FC':0,
                        'UD Almería':0,'UD Las Palmas':0,'Valencia CF':0,'Villareal CF':0}

for serie_num in range(1, number_of_series + 1):
    print(f'\n\n ----- Season {serie_num} -----')
    #######['Lagnamn'  ,Pwr,Plac.,Played,P,W,D,L,G,GA,Diff]
    #List of teams based on EAFC Rankings
    teams = [['Athletic Club',79,0,0,0,0,0,0,0,0,0],
            ['Atlético Madrid',83,0,0,0,0,0,0,0,0,0],
            ['CA Osasuna',77,0,0,0,0,0,0,0,0,0],
            ['Cádiz CF',74,0,0,0,0,0,0,0,0,0],
            ['Deportivo Alavés',71,0,0,0,0,0,0,0,0,0],
            ['FC Barcelona',84,0,0,0,0,0,0,0,0,0],
            ['Getafe CF',76,0,0,0,0,0,0,0,0,0],
            ['Girona FC',76,0,0,0,0,0,0,0,0,0],
            ['Granada CF',74,0,0,0,0,0,0,0,0,0],
            ['Rayo Vallecano',77,0,0,0,0,0,0,0,0,0],
            ['Celta de Vigo',76,0,0,0,0,0,0,0,0,0],
            ['RCD Mallorca',76,0,0,0,0,0,0,0,0,0],
            ['Real Betis',80,0,0,0,0,0,0,0,0,0],
            ['Real Madrid',85,0,0,0,0,0,0,0,0,0],
            ['Real Sociedad',80,0,0,0,0,0,0,0,0,0],
            ['Sevilla FC',80,0,0,0,0,0,0,0,0,0],
            ['UD Almería',74,0,0,0,0,0,0,0,0,0],
            ['UD Las Palmas',73,0,0,0,0,0,0,0,0,0],
            ['Valencia CF',75,0,0,0,0,0,0,0,0,0],
            ['Villareal CF',79,0,0,0,0,0,0,0,0,0],]
    # Create list with possible matchings
    matchings = list(combinations(teams, 2))

    # Shuffle the list
    random.shuffle(matchings)

    # Simple match simulator
    def simulate_match(team1, team2):
        # Get power from list for each team
        team1_power = team1[1]
        team2_power = team2[1]
        # Generating goals based on power
        team1_goals = random.randint(0,4) * (team1_power/100)
        team2_goals = random.randint(0,4) * (team2_power/100)
        # Rounding to whole number
        team1_goals = round(team1_goals)
        team2_goals = round(team2_goals)

        return team1_goals, team2_goals

    # Iterate the list of matches and simulate a match
    for match_num, match in enumerate(matchings, start=1):
        team1, team2 = match
        team1_name, team1_power, team1_played, team1_plac, team1_p, team1_w, team1_d, team1_l, team1_g, team1_ga, team1_diff = team1
        team2_name, team2_power, team2_played, team2_plac, team2_p, team2_w, team2_d, team2_l, team2_g, team2_ga, team2_diff = team2

        team1_score, team2_score = simulate_match(team1,team2)

        # Update matches played
        team1_played += 1
        team2_played += 1
        # Update goals scored/conceded
        team1_g += team1_score
        team2_g += team2_score
        team1_ga += team2_score
        team2_ga += team1_score
        # Update goal diff
        team1_diff = team1_g - team1_ga
        team2_diff = team2_g - team2_ga
        # Update points
        if team1_score > team2_score:
            team1_p += 3
            team1_w += 1
            team2_l += 1
        elif team2_score > team1_score:
            team2_p += 3
            team2_w += 1
            team1_l += 1
        else:
            team1_p += 1
            team1_d += 1
            team2_p += 1
            team2_d += 1
        # Update lists with match values
        team1[2:] = [team1_played, team1_plac, team1_p, team1_w, team1_d, team1_l, team1_g, team1_ga, team1_diff]
        team2[2:] = [team2_played, team2_plac, team2_p, team2_w, team2_d, team2_l, team2_g, team2_ga, team2_diff]
        # Print every match with result
        ''' COMMENT THIS AWAY TO SIM LOADS OF MATCH SERIES
        print(f"Match #{match_num}: {team1_name.ljust(17)} {team1_score} - {team2_score} {team2_name}")
        '''

    # Sort list based on index 4 (points)
    teams.sort(key=lambda x: x[4], reverse=True)

    print('TEAM             GP  P   W   L   D   GF  GA  DIFF')
    for i in range(0,len(teams)):
        print(f'{teams[i][0].ljust(17)}' +
            f'{str(teams[i][2]).ljust(4)}' +
            f'{str(teams[i][4]).ljust(4)}' +
            f'{str(teams[i][5]).ljust(4)}' +
            f'{str(teams[i][6]).ljust(4)}' +
            f'{str(teams[i][7]).ljust(4)}' +
            f'{str(teams[i][8]).ljust(4)}' +
            f'{str(teams[i][9]).ljust(4)}' +
            f'{str(teams[i][10]).ljust(4)}')
    winner = teams[0][0]
    if teams[1][4] > teams[0][4]:
        winner = teams[1][0]
    print(f'--------------- Winner: {winner}')
    league_wins_per_team[winner] += 1

    

# Print team league win statistics
print('\nLeague wins:')
for team, wins in league_wins_per_team.items():
    print(f'{team.ljust(17,'-')} {wins} wins')