# -*- coding: utf-8 -*-

import numpy as np


def calculate_med(hyp, ref, method='word'):
    """ 
    Berechnung der Editierdistanz mit Hilfe des Levenshtein-Abstand-
    Algorithmus.
    Die variable method gibt an, ob die Berechnung auf Wortebene (word) oder
    auf Buchstabenebene (char) stattfindet.

    Folgende Webseite wurde als Leitfaden für die Programmierung des 
    Algorithmus verwendet: https://www.python-course.eu/levenshtein_distance.php
    """
    if method == 'word':
        ref = ref.split()
        hyp = hyp.split()
    else:
        ref = list(ref)
        hyp = list(hyp)
    
    rows = len(hyp)
    cols = len(ref)
    
    # Hinweis: Schritt 1
    matrix = np.zeros((rows+1, cols+1))
    for i in range(0, rows+1):
        matrix[i, 0] = i
    for i in range(0, cols+1):
        matrix[0, i] = i

    # Hinweis: Schritt 2:
    for col in range(1, cols+1):
        for row in range(1, rows+1):
            if hyp[row-1] == ref[col-1]:
                cost = 0
            else:
                cost = 1
            matrix[row, col] = min(matrix[row-1, col] + 1,  # Löschen
                                   matrix[row, col-1] + 1,  # Einfügen
                                   matrix[row-1, col-1] + cost)  # Substituieren 
    med = matrix[rows, cols]
    return med

def calculate_med_onlinefrage(hyp, ref, method='word'):
    """ 
    Anpassung der Strafpunkte für Substitutionen
    und Berechnung auf Wortebene
    """
    
    ref = ref.split()
    hyp = hyp.split()
    
    
    rows = len(hyp)
    cols = len(ref)
    
    # Hinweis: Schritt 1
    matrix = np.zeros((rows+1, cols+1))
    for i in range(0, rows+1):
        matrix[i, 0] = i
    for i in range(0, cols+1):
        matrix[0, i] = i

    # Hinweis: Schritt 2:
    for col in range(1, cols+1):
        for row in range(1, rows+1):
            if hyp[row-1] == ref[col-1]:
                cost = 0
            else:
                cost = 2
            matrix[row, col] = min(matrix[row-1, col] + 1,  # Löschen
                                   matrix[row, col-1] + 1,  # Einfügen
                                   matrix[row-1, col-1] + cost)  # Substituieren 
    med = matrix[rows, cols]
    return med

def main():
    ref = "wenn es im Juni viel donnert kommt ein trueber Sommer"
    hyp1 = "im Juni viel Sonne kommt einen trueberen Sommer"
    hyp2 = "viel Donner im Juni einen trueben Sommer bringt"
    hyp3 = "Juni Donner einen Sommer"
    hyp4 = "im Juni viel Donner bringt einen trueben Sommer"
    hyp5 = "wenns im Juno viel Donner gibts einen trueben Sommer"
    hyps = [hyp1, hyp2, hyp3, hyp4, hyp5]

    # Aufgabenteil a:
    print("Minimale Editierdistanz (MED) als Ähnlichkeitsmaß:")
    print("Aufgabenteil a")
    
    for i in range(0, len(hyps)):
        print("Hypothese ",i+1,": MED = ", calculate_med(hyps[i], ref,
                                                       method='word'))
    # Ausgabe:
    # Minimale Editierdistanz (MED) als Ähnlichkeitsmaß"
    # Aufgabenteil a
    # Hypothese  1 : MED =  5.0
    # Hypothese  2 : MED =  8.0
    # Hypothese  3 : MED =  8.0
    # Hypothese  4 : MED =  6.0
    # Hypothese  5 : MED =  7.0
    # Hypothese 1 ist also der Referenz am ähnlichsten
    
    # Aufgabenteil b:
    print("Aufgabenteil b")
        
    for i in range(0, len(hyps)):
        print("Hypothese ",i+1,": MED = ", calculate_med(hyps[i], ref,
                                                       method='char'))
    # Ausgabe:
    # Aufgabenteil b
    # Hypothese  1 : MED =  15.0
    # Hypothese  2 : MED =  34.0
    # Hypothese  3 : MED =  31.0
    # Hypothese  4 : MED =  18.0
    # Hypothese  5 : MED =  13.0
    # Hypothese 5 ist also der Referenz am ähnlichsten
    
    # Aufgabenteil c:
    print("Aufgabenteil c")
    
    for i in range(0, len(hyps)):
        print("Hypothese ",i+1,": MED = ", calculate_med_onlinefrage(hyps[i], ref,
                                                       method='word'))
    # Ausgabe:
    # Aufgabenteil c
    # Hypothese  1 : MED =  8.0
    # Hypothese  2 : MED =  12.0
    # Hypothese  3 : MED =  10.0
    # Hypothese  4 : MED =  10.0
    # Hypothese  5 : MED =  13.0
    # Hypothese 1 (ED 8) ist also der Referenz am ähnlichsten
    
    
    
    