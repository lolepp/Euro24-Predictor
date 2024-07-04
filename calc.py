import numpy as np
import math

def get_probs(odds):
    """
    Get the probabilities for victory, defeat or draw from the given quota.
    """
    total = sum(1/o for o in odds)
    return [(1/o) / total for o in odds]

def poisson_distribution(lam, k): # lam is the expected decimal value of the number of goals a team scores
    """
    Calculate the Poisson probability for k goals given an average lam.
    """
    return (lam**k * np.exp(-lam)) / math.factorial(k) # (lam^k * e^(-lam)) / k!

def expected_goals(probabilities, avg_goals): # avg goals is a variable that can be changed what to expect as of average goals per game
    """
    Calculate expected goals for each team.
    """
    # average goals after the group phase per game are 2.25
    home_goals = avg_goals[0] * probabilities[0] # avg goals of first team * chance of first team winning
    away_goals = avg_goals[1] * probabilities[2] # avg goals of other team * chance of the other team winning
    return home_goals, away_goals

def exact_score_probabilities(home_goals, away_goals, max_goals=5): # function calculates every chance of every score until max goals variable
    """
    Calculate the probabilities of exact scores using the Poisson distribution.
    """
    probabilities = {}
    for i in range(max_goals+1):
        for j in range(max_goals+1):
            prob = poisson_distribution(home_goals, i) * poisson_distribution(away_goals, j)
            probabilities[(i, j)] = prob
    return probabilities

def analyze_game(game, output = ""): # This the function where every function is calculated, combined and printed
    # Quoten ausgeben
    output += f"{game['name']}" + "\n"
    odds = game['odds']
    
    # Wahrscheinlichkeiten für Sieg, Unentschieden und Niederlage nach Quoten ausgeben
    probabilities = get_probs(odds)
    output += f"Wahrscheinlichkeiten: {probabilities}" + "\n" 
    
    # Durchschnittstore angeben
    avg_goals = game['average goals']
    output += f"Durchschnittstore Heim: {avg_goals[0]}, Durchschnittstore Auswärts: {avg_goals[1]}" + "\n"

    # Erwartete Anzahl an Toren für beide Teams berechnen
    home_goals, away_goals = expected_goals(probabilities, avg_goals)
    output += f"Erwartete Tore Heim: {home_goals:.2f}, Erwartete Tore Auswärts: {away_goals:.2f}" + "\n" 
    
    # Wahrscheinlichkeiten für alle bestimmten Punktzahlen berechnen
    score_probs = exact_score_probabilities(home_goals, away_goals)
    output += "Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:" + "\n" 
    for score, prob in sorted(score_probs.items(), key=lambda item: item[1], reverse=True): # sorting the list of chances of each score in reverse order from most to least probable
        if prob * 100 >= 0.1: # only print the probabilites of the score which are at least 0.1 %
            exact_score = f"Punktzahl {score}: {prob * 100:.2f}%"
            output += exact_score + "\n" 
    return output

def clean_output(file):
    with open(file, 'w') as file:
        file.write('')

def write_output(text, file):
    with open(file, 'a', encoding='utf-8') as file:
        file.write(text)

def printer(input, file):
    print(input)
    write_output(input, file)

def average_goal_calc(scores, number_of_games):
    goals = [0] * len(scores)
    for i in range(len(scores)):
        for j in range(number_of_games):
            goals[i] += scores[i][j]
        goals[i] /= number_of_games
    return goals


def main():
    # Gruppenphase
    group_games = [
        # 1. Spieltag
        {"name": "Spiel 1: Deutschand vs Schottland", "odds": [1.28, 5.75, 11.0]},
        {"name": "Spiel 2: Ungarn vs Schweiz", "odds": [3.3, 3.2, 2.25]},
        {"name": "Spiel 3: Spanien vs Kroatien", "odds": [1.9, 3.4, 4.2]},
        {"name": "Spiel 4: Italien vs Albanien", "odds": [1.39, 4.5, 8.75]},
        {"name": "Spiel 5: Polen vs Niederlande", "odds": [5.5, 4, 1.61]},
        {"name": "Spiel 6: Slowenien vs Dänemark", "odds": [5, 3.6, 1.73]},
        {"name": "Spiel 7: Serbien vs England", "odds": [7, 4.4, 1.46]},
        
        # 2. Spieltag
        {"name": "Spiel 8: Rumänien vs Ukraine", "odds": [3.7, 3.3, 2.05]},
        {"name": "Spiel 9: Belgien vs Slowakei", "odds": [1.49, 4.33, 6.75]},
        {"name": "Spiel 10: Österreich vs Frankreich", "odds": [6, 4.5, 1.5]},
        {"name": "Spiel 11: Türkei vs Georgien", "odds": [1.8, 3.5, 3.75]},
        {"name": "Spiel 12: Portugal vs Tschechien", "odds": [1.53, 4.2, 6]},
        
        # 3. Spieltag
        {"name": "Spiel 13: Kroatien vs Albanien", "odds": [1.53, 4, 6.5]},
        {"name": "Spiel 14: Deutschland vs Ungarn", "odds": [1.33, 5.25, 9.25]},
        {"name": "Spiel 15: Schottland vs Schweiz", "odds": [3.5, 3.4, 2.1]},
        {"name": "Spiel 16: Slowenien vs Serbien", "odds": [3.9, 3.4, 1.98]},
        {"name": "Spiel 17: Dänemark vs England", "odds": [5.5, 3.9, 1.62]},
        {"name": "Spiel 18: Spanien vs Italien", "odds": [2.25, 3.3, 3.1]},
        
        # 4. Spieltag
        {"name": "Spiel 19: Slowakei vs Ukraine", "odds": [3.6, 3.3, 2.05]},
        {"name": "Spiel 20: Polen vs Österreich", "odds": [3.5, 3.5, 2.05]},
        {"name": "Spiel 21: Niederlande vs Frankreich", "odds": [4.1, 3.6, 1.87]},
        {"name": "Spiel 22: Georgien vs Tschechien", "odds": [4.4, 3.5, 1.83]},
        {"name": "Spiel 23: Türkei vs Portugal", "odds": [5.25, 4, 1.62]},
        {"name": "Spiel 24: Belgien vs Rumänien", "odds": [1.49, 4.4, 6.5]},
        
        # 5. Spieltag
        {"name": "Spiel 25: Schweiz vs Deutschland", "odds": [4.6, 3.9, 1.71]},
        {"name": "Spiel 26: Schottland vs Ungarn", "odds": [2.8, 3.5, 2.37]},
        {"name": "Spiel 27: Kroatien vs Italien", "odds": [3.5, 3.4, 2.1]},
        {"name": "Spiel 28: Albanien vs Spanien", "odds": [10, 5.25, 1.32]},
        
        # 6. Spieltag
        {"name": "Spiel 29: Niederlande vs Österreich", "odds": [2.1, 3.5, 3.4]},
        {"name": "Spiel 30: Frankreich vs Polen", "odds": [1.36, 5.25, 8]},
        {"name": "Spiel 31: Dänemark vs Serbien", "odds": [2.4, 3.4, 2.85]},
        {"name": "Spiel 32: England vs Slowenien", "odds": [1.33, 5.25, 9.5]},
        
        # 7. Spieltag
        {"name": "Spiel 33: Ukraine vs Belgien", "odds": [4.6, 3.9, 1.72]},
        {"name": "Spiel 34: Slowakei vs Rumänien", "odds": [2.65, 3.1, 2.75]},
        {"name": "Spiel 35: Tschechien vs Türkei", "odds": [2.87, 3.3, 2.4]},
        {"name": "Spiel 36: Georgien vs Portugal", "odds": [9.75, 5.75, 1.29]}
        
    ]
    
    # Achtelfinale
    roundOf16 = [
        {"name": "Spiel 1: Schweiz vs Italien", "odds": [3.25, 2.95, 2.40], "average goals": []},
        {"name": "Spiel 2: Deutschland vs Dänemark", "odds": [1.60, 3.90, 5.75], "average goals": []},
        {"name": "Spiel 3: England vs Slowakei", "odds": [1.43, 4.33, 8], "average goals": []},
        {"name": "Spiel 4: Spanien vs Georgien", "odds": [1.22, 6.25, 14.5], "average goals": []},
        {"name": "Spiel 5: Frankreich vs Belgien", "odds": [1.90, 3.30, 4.33], "average goals": []},
        {"name": "Spiel 6: Portugal vs Slowenien", "odds": [1.42, 4.4, 8], "average goals": []},
        {"name": "Spiel 7: Rumänien vs Niederlande", "odds": [7.75, 4.33, 1.43], "average goals": []},
        {"name": "Spiel 8: Österreich vs Türkei", "odds": [1.90, 3.40, 4.10], "average goals": []}
    ]
    
    quarterfinals = [
        {"name": "Spiel 1: Spanien vs Deutschland", "odds": [2.60, 3.10, 2.80], "average goals": [0.0, 0.0]},
        {"name": "Spiel 2: Portugal vs Frankreich", "odds": [3.20, 3, 2.40], "average goals": [0.0, 0.0]},
        {"name": "Spiel 3: England vs Schweiz", "odds": [2.20, 3.00, 3.70], "average goals": [0.0, 0.0]},
        {"name": "Spiel 4: Niederlande vs Türkei", "odds": [1.63, 4.00, 5.25], "average goals": [0.0, 0.0]}
    ]

    number_of_games = 4 
    scores = [ # How many goals each team scored per game
        [3, 1, 1, 4], # Spanien
        [5, 2, 1, 2], # Deutschland
        [2, 3, 0, 0], # Portugal
        [1, 0, 1, 1], # Frankreich
        [1, 1, 0, 2], # England
        [3, 1, 1, 2], # Schweiz
        [2, 0, 2, 3], # Niederlande
        [3, 0, 2, 2]  # Türkei
    ]
    avg_goals = average_goal_calc(scores, number_of_games) # [2.25, 2.5, 1.25, 0.75, 1.0, 1.75, 1.75, 1.75]
    counter = 0
    for game in quarterfinals:
        game['average goals'] = avg_goals[counter], avg_goals[counter + 1]
        counter += 2
    output_file = 'output.txt'
    clean_output(output_file)
    
    output = ""
    games = quarterfinals # change here what games shall be predicted
    for game in games:
        output += analyze_game(game)
        if not game == games[len(games) - 1]:
            output += "\n" + "-" * 50 + "\n"
    printer(output, output_file)

if __name__ == "__main__":
    main()
