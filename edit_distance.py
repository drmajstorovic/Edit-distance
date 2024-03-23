# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:32:54 2022

@author: majst
"""

def min_edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)

    # Pravimo tabelu za chuvanje rezultata potproblema
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Popunjavamo d[][] odozdo prema gore
    for i in range(m + 1):
        for j in range(n + 1):
            
            # Ukoliko je prva niska prazna, jedina opcija
            # jeste umetnuti sva slova iz druge niske
            if i == 0:
                dp[i][j] = j * 20 # cijena umetanja slova

            # Ukoliko je druga niska prazna, jedina opcija
            # jeste ukloniti sva slova iz druge niske
            elif j == 0:
                dp[i][j] = i * 20 # cijena uklanjanja slova

            # Ako su posljednja slova jednaka, ignorishemo posljednje
            # slovo i ponavljamo za ostatak niske
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # Ukoliko se posljednje slovo razlikuje, razmatramo
            # sve mogucnosti i trazhimo minimum
            else:
                dp[i][j] = min(dp[i][j - 1] + 20,  # cijena umetanja slova
                               dp[i - 1][j] + 20,  # cijena uklanjanja slova
                               dp[i - 1][j - 1] + 5) # cijena zamjene slova

    return dp[m][n]
    
# glavni program
if __name__ == '__main__':
    
    # print(min_edit_distance("algorithm", "alligator"))
    print(min_edit_distance("dragana", "dragon"))