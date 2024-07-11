A Python script that calculates the chance of every outcome of every Euro24 match for each score but only based on given quotas.

The output of the script is below and also saved in the file output.txt.

Also there is another variant of the predictions saved in output2.txt that is more based on quota alone as I tried to change the calculations of the script to consider recent games.

You might need to install the Python compiler and numpy to run this script.

To install numpy you may need to run
    
    pip install numpy


This is the given output of the current version:

# Output for the finals

Remember, there cannot be a draw in the round of 16 and higher

Note, that for the finals the expected goals have been doubled just for the sake of the finals and the teams giving 110 %.

    Letztes Spiel: Spanien vs England
    Wahrscheinlichkeiten: [0.3876, 0.3332, 0.2793]
    Durchschnittstore Heim: 2.1666666666666665, Durchschnittstore Auswärts: 1.1666666666666667
    Erwartete Tore Heim: 1.68, Erwartete Tore Auswärts: 0.65
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 16.32%
    Punktzahl (2, 0): 13.71%
    Punktzahl (1, 1): 10.64%
    Punktzahl (0, 0): 9.72%
    Punktzahl (2, 1): 8.93%
    Punktzahl (3, 0): 7.67%
    Punktzahl (0, 1): 6.33%
    Punktzahl (3, 1): 5.00%
    Punktzahl (1, 2): 3.47%
    Punktzahl (4, 0): 3.22%
    Punktzahl (2, 2): 2.91%
    Punktzahl (4, 1): 2.10%
    Punktzahl (0, 2): 2.06%
    Punktzahl (3, 2): 1.63%
    Punktzahl (5, 0): 1.08%
    Punktzahl (1, 3): 0.75%
    Punktzahl (5, 1): 0.71%
    Punktzahl (4, 2): 0.68%
    Punktzahl (2, 3): 0.63%
    Punktzahl (0, 3): 0.45%
    Punktzahl (3, 3): 0.35%
    Punktzahl (5, 2): 0.23%
    Punktzahl (4, 3): 0.15%
    Punktzahl (1, 4): 0.12%
    Punktzahl (2, 4): 0.10%


# Output for the semifinals


    Spiel 1: Spanien vs Frankreich
    Wahrscheinlichkeiten: [0.3555, 0.3305, 0.314]
    Durchschnittstore Heim: 2.2, Durchschnittstore Auswärts: 0.6
    Erwartete Tore Heim: 0.78, Erwartete Tore Auswärts: 0.19
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 0): 37.89%
    Punktzahl (1, 0): 29.63%
    Punktzahl (2, 0): 11.59%
    Punktzahl (0, 1): 7.14%
    Punktzahl (1, 1): 5.58%
    Punktzahl (3, 0): 3.02%
    Punktzahl (2, 1): 2.18%
    Punktzahl (0, 2): 0.67%
    Punktzahl (4, 0): 0.59%
    Punktzahl (3, 1): 0.57%
    Punktzahl (1, 2): 0.53%
    Punktzahl (2, 2): 0.21%
    Punktzahl (4, 1): 0.11%

    --------------------------------------------------

    Spiel 2: Niederlande vs England
    Wahrscheinlichkeiten: [0.2964, 0.3388, 0.3648]
    Durchschnittstore Heim: 1.8, Durchschnittstore Auswärts: 1.0
    Erwartete Tore Heim: 0.53, Erwartete Tore Auswärts: 0.36
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 0): 40.72%
    Punktzahl (1, 0): 21.73%
    Punktzahl (0, 1): 14.86%
    Punktzahl (1, 1): 7.93%
    Punktzahl (2, 0): 5.80%
    Punktzahl (0, 2): 2.71%
    Punktzahl (2, 1): 2.11%
    Punktzahl (1, 2): 1.45%
    Punktzahl (3, 0): 1.03%
    Punktzahl (2, 2): 0.39%
    Punktzahl (3, 1): 0.38%
    Punktzahl (0, 3): 0.33%
    Punktzahl (1, 3): 0.18%
    Punktzahl (4, 0): 0.14%


# Output for the quarterfinals

    Spiel 1: Spanien vs Deutschland
    Wahrscheinlichkeiten: [0.353386621792175, 0.31215818258308786, 0.334455195624737]
    Durchschnittstore Heim: 2.25, Durchschnittstore Auswärts: 2.5
    Erwartete Tore Heim: 0.80, Erwartete Tore Auswärts: 0.84
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 0): 19.57%
    Punktzahl (0, 1): 16.36%
    Punktzahl (1, 0): 15.56%
    Punktzahl (1, 1): 13.01%
    Punktzahl (0, 2): 6.84%
    Punktzahl (2, 0): 6.19%
    Punktzahl (1, 2): 5.44%
    Punktzahl (2, 1): 5.17%
    Punktzahl (2, 2): 2.16%
    Punktzahl (0, 3): 1.91%
    Punktzahl (3, 0): 1.64%
    Punktzahl (1, 3): 1.52%
    Punktzahl (3, 1): 1.37%
    Punktzahl (2, 3): 0.60%
    Punktzahl (3, 2): 0.57%
    Punktzahl (0, 4): 0.40%
    Punktzahl (4, 0): 0.33%
    Punktzahl (1, 4): 0.32%
    Punktzahl (4, 1): 0.27%
    Punktzahl (3, 3): 0.16%
    Punktzahl (2, 4): 0.13%
    Punktzahl (4, 2): 0.11%

    --------------------------------------------------

    Spiel 2: Portugal vs Frankreich
    Wahrscheinlichkeiten: [0.29411764705882354, 0.3137254901960784, 0.39215686274509803]
    Durchschnittstore Heim: 1.25, Durchschnittstore Auswärts: 0.75
    Erwartete Tore Heim: 0.37, Erwartete Tore Auswärts: 0.29
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 0): 51.59%
    Punktzahl (1, 0): 18.97%
    Punktzahl (0, 1): 15.17%
    Punktzahl (1, 1): 5.58%
    Punktzahl (2, 0): 3.49%
    Punktzahl (0, 2): 2.23%
    Punktzahl (2, 1): 1.03%
    Punktzahl (1, 2): 0.82%
    Punktzahl (3, 0): 0.43%
    Punktzahl (0, 3): 0.22%
    Punktzahl (2, 2): 0.15%
    Punktzahl (3, 1): 0.13%

    --------------------------------------------------
    
    Spiel 3: England vs Schweiz
    Wahrscheinlichkeiten: [0.4277950310559006, 0.32453416149068326, 0.24767080745341613]
    Durchschnittstore Heim: 1.0, Durchschnittstore Auswärts: 1.75
    Erwartete Tore Heim: 0.43, Erwartete Tore Auswärts: 0.43
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 0): 42.26%
    Punktzahl (0, 1): 18.32%
    Punktzahl (1, 0): 18.08%
    Punktzahl (1, 1): 7.84%
    Punktzahl (0, 2): 3.97%
    Punktzahl (2, 0): 3.87%
    Punktzahl (1, 2): 1.70%
    Punktzahl (2, 1): 1.68%
    Punktzahl (0, 3): 0.57%
    Punktzahl (3, 0): 0.55%
    Punktzahl (2, 2): 0.36%
    Punktzahl (1, 3): 0.25%
    Punktzahl (3, 1): 0.24%

    --------------------------------------------------

    Spiel 4: Niederlande vs Türkei
    Wahrscheinlichkeiten: [0.5993545412632548, 0.24281542953742125, 0.1578300291993238]
    Durchschnittstore Heim: 1.75, Durchschnittstore Auswärts: 1.75
    Erwartete Tore Heim: 1.05, Erwartete Tore Auswärts: 0.28
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 27.88%
    Punktzahl (0, 0): 26.58%
    Punktzahl (2, 0): 14.62%
    Punktzahl (1, 1): 7.70%
    Punktzahl (0, 1): 7.34%
    Punktzahl (3, 0): 5.11%
    Punktzahl (2, 1): 4.04%
    Punktzahl (3, 1): 1.41%
    Punktzahl (4, 0): 1.34%
    Punktzahl (1, 2): 1.06%
    Punktzahl (0, 2): 1.01%
    Punktzahl (2, 2): 0.56%
    Punktzahl (4, 1): 0.37%
    Punktzahl (5, 0): 0.28%
    Punktzahl (3, 2): 0.19%


# Output for the round of 16

    Spiel 1: Schweiz vs Italien
    Wahrscheinlichkeiten: [0.2893634412996832, 0.31879023194032896, 0.3918463267599877]
    Erwartete Tore Heim: 1.01, Erwartete Tore Auswärts: 1.37
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 1): 12.80%
    Punktzahl (0, 1): 12.64%
    Punktzahl (1, 0): 9.33%
    Punktzahl (0, 0): 9.22%
    Punktzahl (1, 2): 8.78%
    Punktzahl (0, 2): 8.67%
    Punktzahl (2, 1): 6.48%
    Punktzahl (2, 0): 4.73%
    Punktzahl (2, 2): 4.44%
    Punktzahl (1, 3): 4.01%
    Punktzahl (0, 3): 3.96%
    Punktzahl (3, 1): 2.19%
    Punktzahl (2, 3): 2.03%
    Punktzahl (3, 0): 1.60%
    Punktzahl (3, 2): 1.50%
    Punktzahl (1, 4): 1.38%
    Punktzahl (0, 4): 1.36%
    Punktzahl (2, 4): 0.70%
    Punktzahl (3, 3): 0.69%
    Punktzahl (4, 1): 0.55%
    Punktzahl (4, 0): 0.40%
    Punktzahl (4, 2): 0.38%
    Punktzahl (1, 5): 0.38%
    Punktzahl (0, 5): 0.37%
    Punktzahl (3, 4): 0.24%
    Punktzahl (2, 5): 0.19%
    Punktzahl (4, 3): 0.17%
    Punktzahl (5, 1): 0.11%

    --------------------------------------------------

    Spiel 2: Deutschland vs Dänemark
    Wahrscheinlichkeiten: [0.5922355737488446, 0.24296844051234656, 0.16479598573880894]
    Erwartete Tore Heim: 2.07, Erwartete Tore Auswärts: 0.58
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (2, 0): 15.18%
    Punktzahl (1, 0): 14.65%
    Punktzahl (3, 0): 10.49%
    Punktzahl (2, 1): 8.76%
    Punktzahl (1, 1): 8.45%
    Punktzahl (0, 0): 7.07%
    Punktzahl (3, 1): 6.05%
    Punktzahl (4, 0): 5.44%
    Punktzahl (0, 1): 4.08%
    Punktzahl (4, 1): 3.14%
    Punktzahl (2, 2): 2.53%
    Punktzahl (1, 2): 2.44%
    Punktzahl (5, 0): 2.25%
    Punktzahl (3, 2): 1.75%
    Punktzahl (5, 1): 1.30%
    Punktzahl (0, 2): 1.18%
    Punktzahl (4, 2): 0.90%
    Punktzahl (2, 3): 0.49%
    Punktzahl (1, 3): 0.47%
    Punktzahl (5, 2): 0.37%
    Punktzahl (3, 3): 0.34%
    Punktzahl (0, 3): 0.23%
    Punktzahl (4, 3): 0.17%

    --------------------------------------------------

    Spiel 3: England vs Slowakei
    Wahrscheinlichkeiten: [0.6626887486393263, 0.2188556375413941, 0.11845561381927956]
    Erwartete Tore Heim: 2.32, Erwartete Tore Auswärts: 0.41
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (2, 0): 17.47%
    Punktzahl (1, 0): 15.07%
    Punktzahl (3, 0): 13.51%
    Punktzahl (4, 0): 7.83%
    Punktzahl (2, 1): 7.24%
    Punktzahl (0, 0): 6.50%
    Punktzahl (1, 1): 6.25%
    Punktzahl (3, 1): 5.60%
    Punktzahl (5, 0): 3.63%
    Punktzahl (4, 1): 3.25%
    Punktzahl (0, 1): 2.69%
    Punktzahl (5, 1): 1.51%
    Punktzahl (2, 2): 1.50%
    Punktzahl (1, 2): 1.29%
    Punktzahl (3, 2): 1.16%
    Punktzahl (4, 2): 0.67%
    Punktzahl (0, 2): 0.56%
    Punktzahl (5, 2): 0.31%
    Punktzahl (2, 3): 0.21%
    Punktzahl (1, 3): 0.18%
    Punktzahl (3, 3): 0.16%

    --------------------------------------------------

    Spiel 4: Spanien vs Georgien
    Wahrscheinlichkeiten: [0.7816543039503191, 0.15257892013110227, 0.06576677591857857]
    Erwartete Tore Heim: 2.74, Erwartete Tore Auswärts: 0.23
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (2, 0): 19.28%
    Punktzahl (3, 0): 17.58%
    Punktzahl (1, 0): 14.09%
    Punktzahl (4, 0): 12.02%
    Punktzahl (5, 0): 6.58%
    Punktzahl (0, 0): 5.15%
    Punktzahl (2, 1): 4.44%
    Punktzahl (3, 1): 4.05%
    Punktzahl (1, 1): 3.24%
    Punktzahl (4, 1): 2.77%
    Punktzahl (5, 1): 1.51%
    Punktzahl (0, 1): 1.19%
    Punktzahl (2, 2): 0.51%
    Punktzahl (3, 2): 0.47%
    Punktzahl (1, 2): 0.37%
    Punktzahl (4, 2): 0.32%
    Punktzahl (5, 2): 0.17%
    Punktzahl (0, 2): 0.14%

    --------------------------------------------------

    Spiel 5: Frankreich vs Belgien
    Wahrscheinlichkeiten: [0.4963871326339192, 0.28579865212255956, 0.21781421524352113]
    Erwartete Tore Heim: 1.74, Erwartete Tore Auswärts: 0.76
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 14.27%
    Punktzahl (2, 0): 12.39%
    Punktzahl (1, 1): 10.88%
    Punktzahl (2, 1): 9.45%
    Punktzahl (0, 0): 8.21%
    Punktzahl (3, 0): 7.18%
    Punktzahl (0, 1): 6.26%
    Punktzahl (3, 1): 5.47%
    Punktzahl (1, 2): 4.15%
    Punktzahl (2, 2): 3.60%
    Punktzahl (4, 0): 3.12%
    Punktzahl (0, 2): 2.39%
    Punktzahl (4, 1): 2.38%
    Punktzahl (3, 2): 2.09%
    Punktzahl (5, 0): 1.08%
    Punktzahl (1, 3): 1.05%
    Punktzahl (2, 3): 0.92%
    Punktzahl (4, 2): 0.91%
    Punktzahl (5, 1): 0.83%
    Punktzahl (0, 3): 0.61%
    Punktzahl (3, 3): 0.53%
    Punktzahl (5, 2): 0.31%
    Punktzahl (4, 3): 0.23%
    Punktzahl (1, 4): 0.20%
    Punktzahl (2, 4): 0.17%
    Punktzahl (0, 4): 0.12%
    Punktzahl (3, 4): 0.10%

    --------------------------------------------------

    Spiel 6: Portugal vs Slowenien
    Wahrscheinlichkeiten: [0.6665656718678987, 0.2151189213755491, 0.11831540675655201]
    Erwartete Tore Heim: 2.33, Erwartete Tore Auswärts: 0.41
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (2, 0): 17.45%
    Punktzahl (1, 0): 14.96%
    Punktzahl (3, 0): 13.57%
    Punktzahl (4, 0): 7.91%
    Punktzahl (2, 1): 7.23%
    Punktzahl (0, 0): 6.41%
    Punktzahl (1, 1): 6.19%
    Punktzahl (3, 1): 5.62%
    Punktzahl (5, 0): 3.69%
    Punktzahl (4, 1): 3.28%
    Punktzahl (0, 1): 2.66%
    Punktzahl (5, 1): 1.53%
    Punktzahl (2, 2): 1.50%
    Punktzahl (1, 2): 1.28%
    Punktzahl (3, 2): 1.16%
    Punktzahl (4, 2): 0.68%
    Punktzahl (0, 2): 0.55%
    Punktzahl (5, 2): 0.32%
    Punktzahl (2, 3): 0.21%
    Punktzahl (1, 3): 0.18%
    Punktzahl (3, 3): 0.16%

    --------------------------------------------------

    Spiel 7: Rumänien vs Niederlande
    Wahrscheinlichkeiten: [0.12181130353183728, 0.2180225409634501, 0.6601661555047127]
    Erwartete Tore Heim: 0.43, Erwartete Tore Auswärts: 2.31
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 2): 17.29%
    Punktzahl (0, 1): 14.97%
    Punktzahl (0, 3): 13.32%
    Punktzahl (0, 4): 7.69%
    Punktzahl (1, 2): 7.37%
    Punktzahl (0, 0): 6.48%
    Punktzahl (1, 1): 6.38%
    Punktzahl (1, 3): 5.68%
    Punktzahl (0, 5): 3.55%
    Punktzahl (1, 4): 3.28%
    Punktzahl (1, 0): 2.76%
    Punktzahl (2, 2): 1.57%
    Punktzahl (1, 5): 1.52%
    Punktzahl (2, 1): 1.36%
    Punktzahl (2, 3): 1.21%
    Punktzahl (2, 4): 0.70%
    Punktzahl (2, 0): 0.59%
    Punktzahl (2, 5): 0.32%
    Punktzahl (3, 2): 0.22%
    Punktzahl (3, 1): 0.19%
    Punktzahl (3, 3): 0.17%

    --------------------------------------------------

    Spiel 8: Österreich vs Türkei
    Wahrscheinlichkeiten: [0.4945015963107485, 0.27633912735012417, 0.2291592763391274]
    Erwartete Tore Heim: 1.73, Erwartete Tore Auswärts: 0.80
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 13.75%
    Punktzahl (2, 0): 11.90%
    Punktzahl (1, 1): 11.03%
    Punktzahl (2, 1): 9.54%
    Punktzahl (0, 0): 7.94%
    Punktzahl (3, 0): 6.86%
    Punktzahl (0, 1): 6.37%
    Punktzahl (3, 1): 5.51%
    Punktzahl (1, 2): 4.42%
    Punktzahl (2, 2): 3.83%
    Punktzahl (4, 0): 2.97%
    Punktzahl (0, 2): 2.56%
    Punktzahl (4, 1): 2.38%
    Punktzahl (3, 2): 2.21%
    Punktzahl (1, 3): 1.18%
    Punktzahl (5, 0): 1.03%
    Punktzahl (2, 3): 1.02%
    Punktzahl (4, 2): 0.96%
    Punktzahl (5, 1): 0.82%
    Punktzahl (0, 3): 0.68%
    Punktzahl (3, 3): 0.59%
    Punktzahl (5, 2): 0.33%
    Punktzahl (4, 3): 0.26%
    Punktzahl (1, 4): 0.24%
    Punktzahl (2, 4): 0.21%
    Punktzahl (0, 4): 0.14%
    Punktzahl (3, 4): 0.12%


# Output for group phase:
    
    Spiel: Spiel 1: Deutschand vs Schottland
    Wahrscheinlichkeiten: [0.7468414216554493, 0.1662533947337348, 0.08690518361081592]
    Erwartete Tore Heim: 1.87, Erwartete Tore Auswärts: 0.22
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 23.22%
    Punktzahl (2, 0): 21.68%
    Punktzahl (3, 0): 13.49%
    Punktzahl (0, 0): 12.44%
    Punktzahl (4, 0): 6.30%
    Punktzahl (1, 1): 5.05%
    Punktzahl (2, 1): 4.71%
    Punktzahl (3, 1): 2.93%
    Punktzahl (0, 1): 2.70%
    Punktzahl (5, 0): 2.35%
    Punktzahl (4, 1): 1.37%
    Punktzahl (1, 2): 0.55%
    Punktzahl (2, 2): 0.51%
    Punktzahl (5, 1): 0.51%
    Punktzahl (3, 2): 0.32%
    Punktzahl (0, 2): 0.29%
    Punktzahl (4, 2): 0.15%

    --------------------------------------------------

    Spiel: Spiel 2: Ungarn vs Schweiz
    Wahrscheinlichkeiten: [0.2858844550327576, 0.2948183442525313, 0.41929720071471116]
    Erwartete Tore Heim: 0.71, Erwartete Tore Auswärts: 1.05
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 17.98%
    Punktzahl (0, 0): 17.15%
    Punktzahl (1, 1): 12.85%
    Punktzahl (1, 0): 12.26%
    Punktzahl (0, 2): 9.42%
    Punktzahl (1, 2): 6.74%
    Punktzahl (2, 1): 4.59%
    Punktzahl (2, 0): 4.38%
    Punktzahl (0, 3): 3.29%
    Punktzahl (2, 2): 2.41%
    Punktzahl (1, 3): 2.35%
    Punktzahl (3, 1): 1.09%
    Punktzahl (3, 0): 1.04%
    Punktzahl (0, 4): 0.86%
    Punktzahl (2, 3): 0.84%
    Punktzahl (1, 4): 0.62%
    Punktzahl (3, 2): 0.57%
    Punktzahl (2, 4): 0.22%
    Punktzahl (3, 3): 0.20%
    Punktzahl (4, 1): 0.20%
    Punktzahl (4, 0): 0.19%
    Punktzahl (0, 5): 0.18%
    Punktzahl (1, 5): 0.13%
    Punktzahl (4, 2): 0.10%

    --------------------------------------------------

    Spiel: Spiel 3: Spanien vs Kroatien
    Wahrscheinlichkeiten: [0.4972144846796657, 0.27785515320334264, 0.22493036211699163]
    Erwartete Tore Heim: 1.24, Erwartete Tore Auswärts: 0.56
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 20.44%
    Punktzahl (0, 0): 16.44%
    Punktzahl (2, 0): 12.70%
    Punktzahl (1, 1): 11.49%
    Punktzahl (0, 1): 9.25%
    Punktzahl (2, 1): 7.14%
    Punktzahl (3, 0): 5.26%
    Punktzahl (1, 2): 3.23%
    Punktzahl (3, 1): 2.96%
    Punktzahl (0, 2): 2.60%
    Punktzahl (2, 2): 2.01%
    Punktzahl (4, 0): 1.64%
    Punktzahl (4, 1): 0.92%
    Punktzahl (3, 2): 0.83%
    Punktzahl (1, 3): 0.61%
    Punktzahl (0, 3): 0.49%
    Punktzahl (5, 0): 0.41%
    Punktzahl (2, 3): 0.38%
    Punktzahl (4, 2): 0.26%
    Punktzahl (5, 1): 0.23%
    Punktzahl (3, 3): 0.16%

    --------------------------------------------------

    Spiel: Spiel 4: Italien vs Albanien
    Wahrscheinlichkeiten: [0.6813167798589782, 0.21045118311199548, 0.10823203702902624]
    Erwartete Tore Heim: 1.70, Erwartete Tore Auswärts: 0.27
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 23.66%
    Punktzahl (2, 0): 20.15%
    Punktzahl (0, 0): 13.89%
    Punktzahl (3, 0): 11.44%
    Punktzahl (1, 1): 6.40%
    Punktzahl (2, 1): 5.45%
    Punktzahl (4, 0): 4.87%
    Punktzahl (0, 1): 3.76%
    Punktzahl (3, 1): 3.10%
    Punktzahl (5, 0): 1.66%
    Punktzahl (4, 1): 1.32%
    Punktzahl (1, 2): 0.87%
    Punktzahl (2, 2): 0.74%
    Punktzahl (0, 2): 0.51%
    Punktzahl (5, 1): 0.45%
    Punktzahl (3, 2): 0.42%
    Punktzahl (4, 2): 0.18%

    --------------------------------------------------

    Spiel: Spiel 5: Polen vs Niederlande
    Wahrscheinlichkeiten: [0.17267730258747824, 0.23743129105778257, 0.5898914063547392]
    Erwartete Tore Heim: 0.43, Erwartete Tore Auswärts: 1.47
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 21.92%
    Punktzahl (0, 2): 16.16%
    Punktzahl (0, 0): 14.86%
    Punktzahl (1, 1): 9.46%
    Punktzahl (0, 3): 7.94%
    Punktzahl (1, 2): 6.98%
    Punktzahl (1, 0): 6.42%
    Punktzahl (1, 3): 3.43%
    Punktzahl (0, 4): 2.93%
    Punktzahl (2, 1): 2.04%
    Punktzahl (2, 2): 1.51%
    Punktzahl (2, 0): 1.38%
    Punktzahl (1, 4): 1.26%
    Punktzahl (0, 5): 0.86%
    Punktzahl (2, 3): 0.74%
    Punktzahl (1, 5): 0.37%
    Punktzahl (3, 1): 0.29%
    Punktzahl (2, 4): 0.27%
    Punktzahl (3, 2): 0.22%
    Punktzahl (3, 0): 0.20%
    Punktzahl (3, 3): 0.11%

    --------------------------------------------------

    Spiel: Spiel 6: Slowenien vs Dänemark
    Wahrscheinlichkeiten: [0.1894275807530872, 0.26309386215706554, 0.5474785570898474]
    Erwartete Tore Heim: 0.47, Erwartete Tore Auswärts: 1.37
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 21.69%
    Punktzahl (0, 0): 15.85%
    Punktzahl (0, 2): 14.84%
    Punktzahl (1, 1): 10.27%
    Punktzahl (1, 0): 7.50%
    Punktzahl (1, 2): 7.03%
    Punktzahl (0, 3): 6.77%
    Punktzahl (1, 3): 3.21%
    Punktzahl (2, 1): 2.43%
    Punktzahl (0, 4): 2.32%
    Punktzahl (2, 0): 1.78%
    Punktzahl (2, 2): 1.66%
    Punktzahl (1, 4): 1.10%
    Punktzahl (2, 3): 0.76%
    Punktzahl (0, 5): 0.63%
    Punktzahl (3, 1): 0.38%
    Punktzahl (1, 5): 0.30%
    Punktzahl (3, 0): 0.28%
    Punktzahl (3, 2): 0.26%
    Punktzahl (2, 4): 0.26%
    Punktzahl (3, 3): 0.12%

    --------------------------------------------------

    Spiel: Spiel 7: Serbien vs England
    Wahrscheinlichkeiten: [0.13540173678441955, 0.21541185397521292, 0.6491864092403676]
    Erwartete Tore Heim: 0.34, Erwartete Tore Auswärts: 1.62
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 22.83%
    Punktzahl (0, 2): 18.52%
    Punktzahl (0, 0): 14.07%
    Punktzahl (0, 3): 10.02%
    Punktzahl (1, 1): 7.73%
    Punktzahl (1, 2): 6.27%
    Punktzahl (1, 0): 4.76%
    Punktzahl (0, 4): 4.07%
    Punktzahl (1, 3): 3.39%
    Punktzahl (1, 4): 1.38%
    Punktzahl (0, 5): 1.32%
    Punktzahl (2, 1): 1.31%
    Punktzahl (2, 2): 1.06%
    Punktzahl (2, 0): 0.81%
    Punktzahl (2, 3): 0.57%
    Punktzahl (1, 5): 0.45%
    Punktzahl (2, 4): 0.23%
    Punktzahl (3, 1): 0.15%
    Punktzahl (3, 2): 0.12%

    --------------------------------------------------

    Spiel: Spiel 8: Rumänien vs Ukraine
    Wahrscheinlichkeiten: [0.25470632530120474, 0.2855798192771084, 0.45971385542168675]
    Erwartete Tore Heim: 0.64, Erwartete Tore Auswärts: 1.15
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 19.26%
    Punktzahl (0, 0): 16.76%
    Punktzahl (1, 1): 12.27%
    Punktzahl (0, 2): 11.07%
    Punktzahl (1, 0): 10.67%
    Punktzahl (1, 2): 7.05%
    Punktzahl (0, 3): 4.24%
    Punktzahl (2, 1): 3.91%
    Punktzahl (2, 0): 3.40%
    Punktzahl (1, 3): 2.70%
    Punktzahl (2, 2): 2.24%
    Punktzahl (0, 4): 1.22%
    Punktzahl (2, 3): 0.86%
    Punktzahl (3, 1): 0.83%
    Punktzahl (1, 4): 0.78%
    Punktzahl (3, 0): 0.72%
    Punktzahl (3, 2): 0.48%
    Punktzahl (0, 5): 0.28%
    Punktzahl (2, 4): 0.25%
    Punktzahl (3, 3): 0.18%
    Punktzahl (1, 5): 0.18%
    Punktzahl (4, 1): 0.13%
    Punktzahl (4, 0): 0.11%

    --------------------------------------------------

    Spiel: Spiel 9: Belgien vs Slowakei
    Wahrscheinlichkeiten: [0.6390382340658596, 0.2198999927847877, 0.1410617731493527]
    Erwartete Tore Heim: 1.60, Erwartete Tore Auswärts: 0.35
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 22.72%
    Punktzahl (2, 0): 18.15%
    Punktzahl (0, 0): 14.22%
    Punktzahl (3, 0): 9.67%
    Punktzahl (1, 1): 8.01%
    Punktzahl (2, 1): 6.40%
    Punktzahl (0, 1): 5.02%
    Punktzahl (4, 0): 3.86%
    Punktzahl (3, 1): 3.41%
    Punktzahl (1, 2): 1.41%
    Punktzahl (4, 1): 1.36%
    Punktzahl (5, 0): 1.23%
    Punktzahl (2, 2): 1.13%
    Punktzahl (0, 2): 0.88%
    Punktzahl (3, 2): 0.60%
    Punktzahl (5, 1): 0.44%
    Punktzahl (4, 2): 0.24%
    Punktzahl (1, 3): 0.17%
    Punktzahl (2, 3): 0.13%
    Punktzahl (0, 3): 0.10%

    --------------------------------------------------

    Spiel: Spiel 10: Österreich vs Frankreich
    Wahrscheinlichkeiten: [0.15789473684210528, 0.2105263157894737, 0.6315789473684211]
    Erwartete Tore Heim: 0.39, Erwartete Tore Auswärts: 1.58
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 21.94%
    Punktzahl (0, 2): 17.32%
    Punktzahl (0, 0): 13.89%
    Punktzahl (0, 3): 9.12%
    Punktzahl (1, 1): 8.66%
    Punktzahl (1, 2): 6.84%
    Punktzahl (1, 0): 5.48%
    Punktzahl (0, 4): 3.60%
    Punktzahl (1, 3): 3.60%
    Punktzahl (2, 1): 1.71%
    Punktzahl (1, 4): 1.42%
    Punktzahl (2, 2): 1.35%
    Punktzahl (0, 5): 1.14%
    Punktzahl (2, 0): 1.08%
    Punktzahl (2, 3): 0.71%
    Punktzahl (1, 5): 0.45%
    Punktzahl (2, 4): 0.28%
    Punktzahl (3, 1): 0.22%
    Punktzahl (3, 2): 0.18%
    Punktzahl (3, 0): 0.14%

    --------------------------------------------------

    Spiel: Spiel 11: Türkei vs Georgien
    Wahrscheinlichkeiten: [0.501432664756447, 0.25787965616045844, 0.24068767908309455]
    Erwartete Tore Heim: 1.25, Erwartete Tore Auswärts: 0.60
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 19.61%
    Punktzahl (0, 0): 15.64%
    Punktzahl (2, 0): 12.29%
    Punktzahl (1, 1): 11.80%
    Punktzahl (0, 1): 9.41%
    Punktzahl (2, 1): 7.39%
    Punktzahl (3, 0): 5.14%
    Punktzahl (1, 2): 3.55%
    Punktzahl (3, 1): 3.09%
    Punktzahl (0, 2): 2.83%
    Punktzahl (2, 2): 2.22%
    Punktzahl (4, 0): 1.61%
    Punktzahl (4, 1): 0.97%
    Punktzahl (3, 2): 0.93%
    Punktzahl (1, 3): 0.71%
    Punktzahl (0, 3): 0.57%
    Punktzahl (2, 3): 0.45%
    Punktzahl (5, 0): 0.40%
    Punktzahl (4, 2): 0.29%
    Punktzahl (5, 1): 0.24%
    Punktzahl (3, 3): 0.19%
    Punktzahl (1, 4): 0.11%

    --------------------------------------------------

    Spiel: Spiel 12: Portugal vs Tschechien
    Wahrscheinlichkeiten: [0.6175562417291575, 0.22496691662990734, 0.15747684164093514]
    Erwartete Tore Heim: 1.54, Erwartete Tore Auswärts: 0.39
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 22.24%
    Punktzahl (2, 0): 17.17%
    Punktzahl (0, 0): 14.41%
    Punktzahl (3, 0): 8.84%
    Punktzahl (1, 1): 8.76%
    Punktzahl (2, 1): 6.76%
    Punktzahl (0, 1): 5.67%
    Punktzahl (3, 1): 3.48%
    Punktzahl (4, 0): 3.41%
    Punktzahl (1, 2): 1.72%
    Punktzahl (4, 1): 1.34%
    Punktzahl (2, 2): 1.33%
    Punktzahl (0, 2): 1.12%
    Punktzahl (5, 0): 1.05%
    Punktzahl (3, 2): 0.68%
    Punktzahl (5, 1): 0.41%
    Punktzahl (4, 2): 0.26%
    Punktzahl (1, 3): 0.23%
    Punktzahl (2, 3): 0.17%
    Punktzahl (0, 3): 0.15%

    --------------------------------------------------

    Spiel: Spiel 13: Kroatien vs Albanien
    Wahrscheinlichkeiten: [0.6180910495661476, 0.23641982645905146, 0.1454891239748009]
    Erwartete Tore Heim: 1.55, Erwartete Tore Auswärts: 0.36
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 22.91%
    Punktzahl (2, 0): 17.70%
    Punktzahl (0, 0): 14.82%
    Punktzahl (3, 0): 9.12%
    Punktzahl (1, 1): 8.33%
    Punktzahl (2, 1): 6.44%
    Punktzahl (0, 1): 5.39%
    Punktzahl (4, 0): 3.52%
    Punktzahl (3, 1): 3.32%
    Punktzahl (1, 2): 1.52%
    Punktzahl (4, 1): 1.28%
    Punktzahl (2, 2): 1.17%
    Punktzahl (5, 0): 1.09%
    Punktzahl (0, 2): 0.98%
    Punktzahl (3, 2): 0.60%
    Punktzahl (5, 1): 0.40%
    Punktzahl (4, 2): 0.23%
    Punktzahl (1, 3): 0.18%
    Punktzahl (2, 3): 0.14%
    Punktzahl (0, 3): 0.12%

    --------------------------------------------------

    Spiel: Spiel 14: Deutschland vs Ungarn
    Wahrscheinlichkeiten: [0.7157596079442868, 0.18132576734588599, 0.1029146247098272]
    Erwartete Tore Heim: 1.79, Erwartete Tore Auswärts: 0.26
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 23.11%
    Punktzahl (2, 0): 20.68%
    Punktzahl (0, 0): 12.92%
    Punktzahl (3, 0): 12.33%
    Punktzahl (1, 1): 5.95%
    Punktzahl (4, 0): 5.52%
    Punktzahl (2, 1): 5.32%
    Punktzahl (0, 1): 3.32%
    Punktzahl (3, 1): 3.17%
    Punktzahl (5, 0): 1.97%
    Punktzahl (4, 1): 1.42%
    Punktzahl (1, 2): 0.76%
    Punktzahl (2, 2): 0.68%
    Punktzahl (5, 1): 0.51%
    Punktzahl (0, 2): 0.43%
    Punktzahl (3, 2): 0.41%
    Punktzahl (4, 2): 0.18%

    --------------------------------------------------

    Spiel: Spiel 15: Schottland vs Schweiz
    Wahrscheinlichkeiten: [0.27055702917771884, 0.2785145888594165, 0.4509283819628648]
    Erwartete Tore Heim: 0.68, Erwartete Tore Auswärts: 1.13
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 18.57%
    Punktzahl (0, 0): 16.47%
    Punktzahl (1, 1): 12.56%
    Punktzahl (1, 0): 11.14%
    Punktzahl (0, 2): 10.46%
    Punktzahl (1, 2): 7.08%
    Punktzahl (2, 1): 4.25%
    Punktzahl (0, 3): 3.93%
    Punktzahl (2, 0): 3.77%
    Punktzahl (1, 3): 2.66%
    Punktzahl (2, 2): 2.39%
    Punktzahl (0, 4): 1.11%
    Punktzahl (3, 1): 0.96%
    Punktzahl (2, 3): 0.90%
    Punktzahl (3, 0): 0.85%
    Punktzahl (1, 4): 0.75%
    Punktzahl (3, 2): 0.54%
    Punktzahl (2, 4): 0.25%
    Punktzahl (0, 5): 0.25%
    Punktzahl (3, 3): 0.20%
    Punktzahl (1, 5): 0.17%
    Punktzahl (4, 1): 0.16%
    Punktzahl (4, 0): 0.14%

    --------------------------------------------------

    Spiel: Spiel 16: Slowenien vs Serbien
    Wahrscheinlichkeiten: [0.24290972071877034, 0.27863173847153067, 0.47845854080969913]
    Erwartete Tore Heim: 0.61, Erwartete Tore Auswärts: 1.20
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 19.70%
    Punktzahl (0, 0): 16.47%
    Punktzahl (1, 1): 11.97%
    Punktzahl (0, 2): 11.78%
    Punktzahl (1, 0): 10.00%
    Punktzahl (1, 2): 7.16%
    Punktzahl (0, 3): 4.70%
    Punktzahl (2, 1): 3.63%
    Punktzahl (2, 0): 3.04%
    Punktzahl (1, 3): 2.85%
    Punktzahl (2, 2): 2.17%
    Punktzahl (0, 4): 1.41%
    Punktzahl (2, 3): 0.87%
    Punktzahl (1, 4): 0.85%
    Punktzahl (3, 1): 0.74%
    Punktzahl (3, 0): 0.61%
    Punktzahl (3, 2): 0.44%
    Punktzahl (0, 5): 0.34%
    Punktzahl (2, 4): 0.26%
    Punktzahl (1, 5): 0.20%
    Punktzahl (3, 3): 0.18%
    Punktzahl (4, 1): 0.11%

    --------------------------------------------------

    Spiel: Spiel 17: Dänemark vs England
    Wahrscheinlichkeiten: [0.17225584819237694, 0.24292491411745465, 0.5848192376901685]
    Erwartete Tore Heim: 0.43, Erwartete Tore Auswärts: 1.46
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 22.03%
    Punktzahl (0, 2): 16.10%
    Punktzahl (0, 0): 15.07%
    Punktzahl (1, 1): 9.49%
    Punktzahl (0, 3): 7.85%
    Punktzahl (1, 2): 6.93%
    Punktzahl (1, 0): 6.49%
    Punktzahl (1, 3): 3.38%
    Punktzahl (0, 4): 2.87%
    Punktzahl (2, 1): 2.04%
    Punktzahl (2, 2): 1.49%
    Punktzahl (2, 0): 1.40%
    Punktzahl (1, 4): 1.24%
    Punktzahl (0, 5): 0.84%
    Punktzahl (2, 3): 0.73%
    Punktzahl (1, 5): 0.36%
    Punktzahl (3, 1): 0.29%
    Punktzahl (2, 4): 0.27%
    Punktzahl (3, 2): 0.21%
    Punktzahl (3, 0): 0.20%
    Punktzahl (3, 3): 0.10%

    --------------------------------------------------

    Spiel: Spiel 18: Spanien vs Italien
    Wahrscheinlichkeiten: [0.415347137637028, 0.2831912302070646, 0.30146163215590743]
    Erwartete Tore Heim: 1.04, Erwartete Tore Auswärts: 0.75
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 17.30%
    Punktzahl (0, 0): 16.66%
    Punktzahl (1, 1): 13.04%
    Punktzahl (0, 1): 12.56%
    Punktzahl (2, 0): 8.98%
    Punktzahl (2, 1): 6.77%
    Punktzahl (1, 2): 4.91%
    Punktzahl (0, 2): 4.73%
    Punktzahl (3, 0): 3.11%
    Punktzahl (2, 2): 2.55%
    Punktzahl (3, 1): 2.34%
    Punktzahl (1, 3): 1.23%
    Punktzahl (0, 3): 1.19%
    Punktzahl (3, 2): 0.88%
    Punktzahl (4, 0): 0.81%
    Punktzahl (2, 3): 0.64%
    Punktzahl (4, 1): 0.61%
    Punktzahl (1, 4): 0.23%
    Punktzahl (4, 2): 0.23%
    Punktzahl (0, 4): 0.22%
    Punktzahl (3, 3): 0.22%
    Punktzahl (5, 0): 0.17%
    Punktzahl (5, 1): 0.13%
    Punktzahl (2, 4): 0.12%

    --------------------------------------------------

    Spiel: Spiel 19: Slowakei vs Ukraine
    Wahrscheinlichkeiten: [0.25994236311239194, 0.28357348703170027, 0.4564841498559078]
    Erwartete Tore Heim: 0.65, Erwartete Tore Auswärts: 1.14
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 19.03%
    Punktzahl (0, 0): 16.68%
    Punktzahl (1, 1): 12.37%
    Punktzahl (0, 2): 10.86%
    Punktzahl (1, 0): 10.84%
    Punktzahl (1, 2): 7.06%
    Punktzahl (0, 3): 4.13%
    Punktzahl (2, 1): 4.02%
    Punktzahl (2, 0): 3.52%
    Punktzahl (1, 3): 2.68%
    Punktzahl (2, 2): 2.29%
    Punktzahl (0, 4): 1.18%
    Punktzahl (2, 3): 0.87%
    Punktzahl (3, 1): 0.87%
    Punktzahl (1, 4): 0.77%
    Punktzahl (3, 0): 0.76%
    Punktzahl (3, 2): 0.50%
    Punktzahl (0, 5): 0.27%
    Punktzahl (2, 4): 0.25%
    Punktzahl (3, 3): 0.19%
    Punktzahl (1, 5): 0.17%
    Punktzahl (4, 1): 0.14%
    Punktzahl (4, 0): 0.12%

    --------------------------------------------------

    Spiel: Spiel 20: Polen vs Österreich
    Wahrscheinlichkeiten: [0.26973684210526316, 0.26973684210526316, 0.46052631578947373]
    Erwartete Tore Heim: 0.67, Erwartete Tore Auswärts: 1.15
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 18.55%
    Punktzahl (0, 0): 16.11%
    Punktzahl (1, 1): 12.51%
    Punktzahl (1, 0): 10.86%
    Punktzahl (0, 2): 10.68%
    Punktzahl (1, 2): 7.20%
    Punktzahl (2, 1): 4.22%
    Punktzahl (0, 3): 4.10%
    Punktzahl (2, 0): 3.66%
    Punktzahl (1, 3): 2.76%
    Punktzahl (2, 2): 2.43%
    Punktzahl (0, 4): 1.18%
    Punktzahl (3, 1): 0.95%
    Punktzahl (2, 3): 0.93%
    Punktzahl (3, 0): 0.82%
    Punktzahl (1, 4): 0.80%
    Punktzahl (3, 2): 0.55%
    Punktzahl (0, 5): 0.27%
    Punktzahl (2, 4): 0.27%
    Punktzahl (3, 3): 0.21%
    Punktzahl (1, 5): 0.18%
    Punktzahl (4, 1): 0.16%
    Punktzahl (4, 0): 0.14%

    --------------------------------------------------

    Spiel: Spiel 21: Niederlande vs Frankreich
    Wahrscheinlichkeiten: [0.2308721149559313, 0.2629376864775884, 0.5061901985664803]
    Erwartete Tore Heim: 0.58, Erwartete Tore Auswärts: 1.27
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 20.04%
    Punktzahl (0, 0): 15.84%
    Punktzahl (0, 2): 12.68%
    Punktzahl (1, 1): 11.57%
    Punktzahl (1, 0): 9.14%
    Punktzahl (1, 2): 7.32%
    Punktzahl (0, 3): 5.35%
    Punktzahl (2, 1): 3.34%
    Punktzahl (1, 3): 3.09%
    Punktzahl (2, 0): 2.64%
    Punktzahl (2, 2): 2.11%
    Punktzahl (0, 4): 1.69%
    Punktzahl (1, 4): 0.98%
    Punktzahl (2, 3): 0.89%
    Punktzahl (3, 1): 0.64%
    Punktzahl (3, 0): 0.51%
    Punktzahl (0, 5): 0.43%
    Punktzahl (3, 2): 0.41%
    Punktzahl (2, 4): 0.28%
    Punktzahl (1, 5): 0.25%
    Punktzahl (3, 3): 0.17%

    --------------------------------------------------

    Spiel: Spiel 22: Georgien vs Tschechien
    Wahrscheinlichkeiten: [0.21452255752419871, 0.2696855008875641, 0.5157919415882373]
    Erwartete Tore Heim: 0.54, Erwartete Tore Auswärts: 1.29
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 20.77%
    Punktzahl (0, 0): 16.11%
    Punktzahl (0, 2): 13.39%
    Punktzahl (1, 1): 11.14%
    Punktzahl (1, 0): 8.64%
    Punktzahl (1, 2): 7.18%
    Punktzahl (0, 3): 5.76%
    Punktzahl (1, 3): 3.09%
    Punktzahl (2, 1): 2.99%
    Punktzahl (2, 0): 2.32%
    Punktzahl (2, 2): 1.93%
    Punktzahl (0, 4): 1.86%
    Punktzahl (1, 4): 1.00%
    Punktzahl (2, 3): 0.83%
    Punktzahl (3, 1): 0.53%
    Punktzahl (0, 5): 0.48%
    Punktzahl (3, 0): 0.41%
    Punktzahl (3, 2): 0.34%
    Punktzahl (2, 4): 0.27%
    Punktzahl (1, 5): 0.26%
    Punktzahl (3, 3): 0.15%

    --------------------------------------------------

    Spiel: Spiel 23: Türkei vs Portugal
    Wahrscheinlichkeiten: [0.18007503126302626, 0.236348478532722, 0.5835764902042518]
    Erwartete Tore Heim: 0.45, Erwartete Tore Auswärts: 1.46
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 21.62%
    Punktzahl (0, 2): 15.77%
    Punktzahl (0, 0): 14.82%
    Punktzahl (1, 1): 9.73%
    Punktzahl (0, 3): 7.67%
    Punktzahl (1, 2): 7.10%
    Punktzahl (1, 0): 6.67%
    Punktzahl (1, 3): 3.45%
    Punktzahl (0, 4): 2.80%
    Punktzahl (2, 1): 2.19%
    Punktzahl (2, 2): 1.60%
    Punktzahl (2, 0): 1.50%
    Punktzahl (1, 4): 1.26%
    Punktzahl (0, 5): 0.82%
    Punktzahl (2, 3): 0.78%
    Punktzahl (1, 5): 0.37%
    Punktzahl (3, 1): 0.33%
    Punktzahl (2, 4): 0.28%
    Punktzahl (3, 2): 0.24%
    Punktzahl (3, 0): 0.23%
    Punktzahl (3, 3): 0.12%

    --------------------------------------------------

    Spiel: Spiel 24: Belgien vs Rumänien
    Wahrscheinlichkeiten: [0.637809147878058, 0.21598537053143327, 0.1462054815905087]
    Erwartete Tore Heim: 1.59, Erwartete Tore Auswärts: 0.37
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 22.46%
    Punktzahl (2, 0): 17.91%
    Punktzahl (0, 0): 14.09%
    Punktzahl (3, 0): 9.52%
    Punktzahl (1, 1): 8.21%
    Punktzahl (2, 1): 6.54%
    Punktzahl (0, 1): 5.15%
    Punktzahl (4, 0): 3.79%
    Punktzahl (3, 1): 3.48%
    Punktzahl (1, 2): 1.50%
    Punktzahl (4, 1): 1.39%
    Punktzahl (5, 0): 1.21%
    Punktzahl (2, 2): 1.20%
    Punktzahl (0, 2): 0.94%
    Punktzahl (3, 2): 0.64%
    Punktzahl (5, 1): 0.44%
    Punktzahl (4, 2): 0.25%
    Punktzahl (1, 3): 0.18%
    Punktzahl (2, 3): 0.15%
    Punktzahl (0, 3): 0.11%

    --------------------------------------------------

    Spiel: Spiel 25: Schweiz vs Deutschland
    Wahrscheinlichkeiten: [0.2053579676674365, 0.2422170900692841, 0.5524249422632794]
    Erwartete Tore Heim: 0.51, Erwartete Tore Auswärts: 1.38
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 20.77%
    Punktzahl (0, 0): 15.04%
    Punktzahl (0, 2): 14.34%
    Punktzahl (1, 1): 10.66%
    Punktzahl (1, 0): 7.72%
    Punktzahl (1, 2): 7.36%
    Punktzahl (0, 3): 6.60%
    Punktzahl (1, 3): 3.39%
    Punktzahl (2, 1): 2.74%
    Punktzahl (0, 4): 2.28%
    Punktzahl (2, 0): 1.98%
    Punktzahl (2, 2): 1.89%
    Punktzahl (1, 4): 1.17%
    Punktzahl (2, 3): 0.87%
    Punktzahl (0, 5): 0.63%
    Punktzahl (3, 1): 0.47%
    Punktzahl (3, 0): 0.34%
    Punktzahl (3, 2): 0.32%
    Punktzahl (1, 5): 0.32%
    Punktzahl (2, 4): 0.30%
    Punktzahl (3, 3): 0.15%

    --------------------------------------------------

    Spiel: Spiel 26: Schottland vs Ungarn
    Wahrscheinlichkeiten: [0.3354090008491368, 0.2683272006793094, 0.3962637984715539]
    Erwartete Tore Heim: 0.84, Erwartete Tore Auswärts: 0.99
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 0): 16.05%
    Punktzahl (0, 1): 15.90%
    Punktzahl (1, 0): 13.46%
    Punktzahl (1, 1): 13.34%
    Punktzahl (0, 2): 7.88%
    Punktzahl (1, 2): 6.61%
    Punktzahl (2, 0): 5.64%
    Punktzahl (2, 1): 5.59%
    Punktzahl (2, 2): 2.77%
    Punktzahl (0, 3): 2.60%
    Punktzahl (1, 3): 2.18%
    Punktzahl (3, 0): 1.58%
    Punktzahl (3, 1): 1.56%
    Punktzahl (2, 3): 0.91%
    Punktzahl (3, 2): 0.77%
    Punktzahl (0, 4): 0.64%
    Punktzahl (1, 4): 0.54%
    Punktzahl (4, 0): 0.33%
    Punktzahl (4, 1): 0.33%
    Punktzahl (3, 3): 0.26%
    Punktzahl (2, 4): 0.23%
    Punktzahl (4, 2): 0.16%
    Punktzahl (0, 5): 0.13%
    Punktzahl (1, 5): 0.11%

    --------------------------------------------------

    Spiel: Spiel 27: Kroatien vs Italien
    Wahrscheinlichkeiten: [0.27055702917771884, 0.2785145888594165, 0.4509283819628648]
    Erwartete Tore Heim: 0.68, Erwartete Tore Auswärts: 1.13
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 18.57%
    Punktzahl (0, 0): 16.47%
    Punktzahl (1, 1): 12.56%
    Punktzahl (1, 0): 11.14%
    Punktzahl (0, 2): 10.46%
    Punktzahl (1, 2): 7.08%
    Punktzahl (2, 1): 4.25%
    Punktzahl (0, 3): 3.93%
    Punktzahl (2, 0): 3.77%
    Punktzahl (1, 3): 2.66%
    Punktzahl (2, 2): 2.39%
    Punktzahl (0, 4): 1.11%
    Punktzahl (3, 1): 0.96%
    Punktzahl (2, 3): 0.90%
    Punktzahl (3, 0): 0.85%
    Punktzahl (1, 4): 0.75%
    Punktzahl (3, 2): 0.54%
    Punktzahl (2, 4): 0.25%
    Punktzahl (0, 5): 0.25%
    Punktzahl (3, 3): 0.20%
    Punktzahl (1, 5): 0.17%
    Punktzahl (4, 1): 0.16%
    Punktzahl (4, 0): 0.14%

    --------------------------------------------------

    Spiel: Spiel 28: Albanien vs Spanien
    Wahrscheinlichkeiten: [0.09541511771995043, 0.18174308137133413, 0.7228418009087153]
    Erwartete Tore Heim: 0.24, Erwartete Tore Auswärts: 1.81
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 23.37%
    Punktzahl (0, 2): 21.11%
    Punktzahl (0, 0): 12.93%
    Punktzahl (0, 3): 12.72%
    Punktzahl (0, 4): 5.75%
    Punktzahl (1, 1): 5.57%
    Punktzahl (1, 2): 5.04%
    Punktzahl (1, 0): 3.08%
    Punktzahl (1, 3): 3.03%
    Punktzahl (0, 5): 2.08%
    Punktzahl (1, 4): 1.37%
    Punktzahl (2, 1): 0.66%
    Punktzahl (2, 2): 0.60%
    Punktzahl (1, 5): 0.50%
    Punktzahl (2, 0): 0.37%
    Punktzahl (2, 3): 0.36%
    Punktzahl (2, 4): 0.16%

    --------------------------------------------------

    Spiel: Spiel 29: Niederlande vs Österreich
    Wahrscheinlichkeiten: [0.45092838196286467, 0.2705570291777188, 0.27851458885941643]
    Erwartete Tore Heim: 1.13, Erwartete Tore Auswärts: 0.70
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 18.20%
    Punktzahl (0, 0): 16.14%
    Punktzahl (1, 1): 12.67%
    Punktzahl (0, 1): 11.24%
    Punktzahl (2, 0): 10.26%
    Punktzahl (2, 1): 7.14%
    Punktzahl (1, 2): 4.41%
    Punktzahl (0, 2): 3.91%
    Punktzahl (3, 0): 3.85%
    Punktzahl (3, 1): 2.68%
    Punktzahl (2, 2): 2.49%
    Punktzahl (4, 0): 1.09%
    Punktzahl (1, 3): 1.02%
    Punktzahl (3, 2): 0.93%
    Punktzahl (0, 3): 0.91%
    Punktzahl (4, 1): 0.76%
    Punktzahl (2, 3): 0.58%
    Punktzahl (4, 2): 0.26%
    Punktzahl (5, 0): 0.24%
    Punktzahl (3, 3): 0.22%
    Punktzahl (1, 4): 0.18%
    Punktzahl (5, 1): 0.17%
    Punktzahl (0, 4): 0.16%
    Punktzahl (2, 4): 0.10%

    --------------------------------------------------

    Spiel: Spiel 30: Frankreich vs Polen
    Wahrscheinlichkeiten: [0.6997667444185273, 0.18127290903032325, 0.11896034655114963]
    Erwartete Tore Heim: 1.75, Erwartete Tore Auswärts: 0.30
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 22.59%
    Punktzahl (2, 0): 19.76%
    Punktzahl (0, 0): 12.91%
    Punktzahl (3, 0): 11.52%
    Punktzahl (1, 1): 6.72%
    Punktzahl (2, 1): 5.88%
    Punktzahl (4, 0): 5.04%
    Punktzahl (0, 1): 3.84%
    Punktzahl (3, 1): 3.43%
    Punktzahl (5, 0): 1.76%
    Punktzahl (4, 1): 1.50%
    Punktzahl (1, 2): 1.00%
    Punktzahl (2, 2): 0.87%
    Punktzahl (0, 2): 0.57%
    Punktzahl (5, 1): 0.52%
    Punktzahl (3, 2): 0.51%
    Punktzahl (4, 2): 0.22%

    --------------------------------------------------

    Spiel: Spiel 31: Dänemark vs Serbien
    Wahrscheinlichkeiten: [0.3924665856622115, 0.2770352369380316, 0.330498177399757]
    Erwartete Tore Heim: 0.98, Erwartete Tore Auswärts: 0.83
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 0): 16.41%
    Punktzahl (1, 0): 16.10%
    Punktzahl (0, 1): 13.56%
    Punktzahl (1, 1): 13.30%
    Punktzahl (2, 0): 7.90%
    Punktzahl (2, 1): 6.53%
    Punktzahl (0, 2): 5.60%
    Punktzahl (1, 2): 5.50%
    Punktzahl (2, 2): 2.70%
    Punktzahl (3, 0): 2.58%
    Punktzahl (3, 1): 2.13%
    Punktzahl (0, 3): 1.54%
    Punktzahl (1, 3): 1.51%
    Punktzahl (3, 2): 0.88%
    Punktzahl (2, 3): 0.74%
    Punktzahl (4, 0): 0.63%
    Punktzahl (4, 1): 0.52%
    Punktzahl (0, 4): 0.32%
    Punktzahl (1, 4): 0.31%
    Punktzahl (3, 3): 0.24%
    Punktzahl (4, 2): 0.22%
    Punktzahl (2, 4): 0.15%
    Punktzahl (5, 0): 0.12%
    Punktzahl (5, 1): 0.10%

    --------------------------------------------------

    Spiel: Spiel 32: England vs Slowenien
    Wahrscheinlichkeiten: [0.7177033492822967, 0.18181818181818185, 0.10047846889952154]
    Erwartete Tore Heim: 1.79, Erwartete Tore Auswärts: 0.25
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (1, 0): 23.20%
    Punktzahl (2, 0): 20.82%
    Punktzahl (0, 0): 12.93%
    Punktzahl (3, 0): 12.45%
    Punktzahl (1, 1): 5.83%
    Punktzahl (4, 0): 5.58%
    Punktzahl (2, 1): 5.23%
    Punktzahl (0, 1): 3.25%
    Punktzahl (3, 1): 3.13%
    Punktzahl (5, 0): 2.00%
    Punktzahl (4, 1): 1.40%
    Punktzahl (1, 2): 0.73%
    Punktzahl (2, 2): 0.66%
    Punktzahl (5, 1): 0.50%
    Punktzahl (0, 2): 0.41%
    Punktzahl (3, 2): 0.39%
    Punktzahl (4, 2): 0.18%

    --------------------------------------------------

    Spiel: Spiel 33: Ukraine vs Belgien
    Wahrscheinlichkeiten: [0.206019656019656, 0.24299754299754298, 0.550982800982801]
    Erwartete Tore Heim: 0.52, Erwartete Tore Auswärts: 1.38
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 20.76%
    Punktzahl (0, 0): 15.07%
    Punktzahl (0, 2): 14.30%
    Punktzahl (1, 1): 10.69%
    Punktzahl (1, 0): 7.76%
    Punktzahl (1, 2): 7.36%
    Punktzahl (0, 3): 6.56%
    Punktzahl (1, 3): 3.38%
    Punktzahl (2, 1): 2.75%
    Punktzahl (0, 4): 2.26%
    Punktzahl (2, 0): 2.00%
    Punktzahl (2, 2): 1.90%
    Punktzahl (1, 4): 1.16%
    Punktzahl (2, 3): 0.87%
    Punktzahl (0, 5): 0.62%
    Punktzahl (3, 1): 0.47%
    Punktzahl (3, 0): 0.34%
    Punktzahl (3, 2): 0.33%
    Punktzahl (1, 5): 0.32%
    Punktzahl (2, 4): 0.30%
    Punktzahl (3, 3): 0.15%

    --------------------------------------------------

    Spiel: Spiel 34: Slowakei vs Rumänien
    Wahrscheinlichkeiten: [0.3548017896160649, 0.3032983040266361, 0.3418999063572989]
    Erwartete Tore Heim: 0.89, Erwartete Tore Auswärts: 0.85
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 0): 17.52%
    Punktzahl (1, 0): 15.54%
    Punktzahl (0, 1): 14.98%
    Punktzahl (1, 1): 13.28%
    Punktzahl (2, 0): 6.89%
    Punktzahl (0, 2): 6.40%
    Punktzahl (2, 1): 5.89%
    Punktzahl (1, 2): 5.68%
    Punktzahl (2, 2): 2.52%
    Punktzahl (3, 0): 2.04%
    Punktzahl (0, 3): 1.82%
    Punktzahl (3, 1): 1.74%
    Punktzahl (1, 3): 1.62%
    Punktzahl (3, 2): 0.74%
    Punktzahl (2, 3): 0.72%
    Punktzahl (4, 0): 0.45%
    Punktzahl (0, 4): 0.39%
    Punktzahl (4, 1): 0.39%
    Punktzahl (1, 4): 0.35%
    Punktzahl (3, 3): 0.21%
    Punktzahl (4, 2): 0.17%
    Punktzahl (2, 4): 0.15%

    --------------------------------------------------

    Spiel: Spiel 35: Tschechien vs Türkei
    Wahrscheinlichkeiten: [0.32620783393055724, 0.283701964660818, 0.3900902014086247]
    Erwartete Tore Heim: 0.82, Erwartete Tore Auswärts: 0.98
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 0): 16.68%
    Punktzahl (0, 1): 16.27%
    Punktzahl (1, 0): 13.61%
    Punktzahl (1, 1): 13.27%
    Punktzahl (0, 2): 7.93%
    Punktzahl (1, 2): 6.47%
    Punktzahl (2, 0): 5.55%
    Punktzahl (2, 1): 5.41%
    Punktzahl (2, 2): 2.64%
    Punktzahl (0, 3): 2.58%
    Punktzahl (1, 3): 2.10%
    Punktzahl (3, 0): 1.51%
    Punktzahl (3, 1): 1.47%
    Punktzahl (2, 3): 0.86%
    Punktzahl (3, 2): 0.72%
    Punktzahl (0, 4): 0.63%
    Punktzahl (1, 4): 0.51%
    Punktzahl (4, 0): 0.31%
    Punktzahl (4, 1): 0.30%
    Punktzahl (3, 3): 0.23%
    Punktzahl (2, 4): 0.21%
    Punktzahl (4, 2): 0.15%
    Punktzahl (0, 5): 0.12%
    Punktzahl (1, 5): 0.10%

    --------------------------------------------------

    Spiel: Spiel 36: Georgien vs Portugal
    Wahrscheinlichkeiten: [0.09752489892515531, 0.16536830687308943, 0.7371067942017552]
    Erwartete Tore Heim: 0.24, Erwartete Tore Auswärts: 1.84
    Alle möglichen Punktzahlen und deren Wahrscheinlichkeiten:
    Punktzahl (0, 1): 22.87%
    Punktzahl (0, 2): 21.07%
    Punktzahl (0, 3): 12.94%
    Punktzahl (0, 0): 12.41%
    Punktzahl (0, 4): 5.96%
    Punktzahl (1, 1): 5.58%
    Punktzahl (1, 2): 5.14%
    Punktzahl (1, 3): 3.16%
    Punktzahl (1, 0): 3.03%
    Punktzahl (0, 5): 2.20%
    Punktzahl (1, 4): 1.45%
    Punktzahl (2, 1): 0.68%
    Punktzahl (2, 2): 0.63%
    Punktzahl (1, 5): 0.54%
    Punktzahl (2, 3): 0.38%
    Punktzahl (2, 0): 0.37%
    Punktzahl (2, 4): 0.18%
