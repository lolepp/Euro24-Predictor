import numpy as np
import math

def calculate_probabilities(odds):
    """
    Calculate the probabilities from the given odds.
    """
    total = sum(1/o for o in odds)
    return [(1/o) / total for o in odds]

def poisson_distribution(lam, k):
    """
    Calculate the Poisson probability for k goals given an average lam.
    """
    return (lam**k * np.exp(-lam)) / math.factorial(k)

def expected_goals(probabilities, avg_goals=2.5):
    """
    Calculate expected goals for each team.
    """
    home_goals = avg_goals * probabilities[0]
    away_goals = avg_goals * probabilities[2]
    return home_goals, away_goals

def exact_score_probabilities(home_goals, away_goals, max_goals=5):
    """
    Calculate the probabilities of exact scores using the Poisson distribution.
    """
    probabilities = {}
    for i in range(max_goals+1):
        for j in range(max_goals+1):
            prob = poisson_distribution(home_goals, i) * poisson_distribution(away_goals, j)
            probabilities[(i, j)] = prob
    return probabilities

def analyze_game(game):
    print(f"Spiel: {game['name']}")
    odds = game['odds']
    
    # Wahrscheinlichkeiten für Sieg, Unentschieden, Niederlage berechnen
    probabilities = calculate_probabilities(odds)
    print(f"Wahrscheinlichkeiten: {probabilities}")
    
    # Erwartete Tore für beide Teams berechnen
    home_goals, away_goals = expected_goals(probabilities)
    print(f"Erwartete Tore Heim: {home_goals:.2f}, Erwartete Tore Auswärts: {away_goals:.2f}")
    
    # Wahrscheinlichkeiten für genaue Punktzahlen berechnen
    score_probs = exact_score_probabilities(home_goals, away_goals)
    
    # Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten ausgeben
    print("Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:")
    for score, prob in sorted(score_probs.items(), key=lambda item: item[1], reverse=True):
        if prob * 100 >= 0.1:
            print(f"Punktzahl {score}: {prob*100:.2f}%")
    print("\n" + "-"*50 + "\n")

def main():
    # Beispiel Wettquoten für verschiedene Spiele
    games = [
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
    
    for game in games:
        analyze_game(game)
 
if __name__ == "__main__":
    main()
