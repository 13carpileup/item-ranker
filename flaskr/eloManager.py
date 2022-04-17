def eloDetermine(score1,score2,outcome):
    # Calculate the expected score for each player
    expectedScore1 = 1/(1+10**((score2-score1)/400))
    expectedScore2 = 1/(1+10**((score1-score2)/400))
    # Calculate the new score for each player
    newScore1 = score1 - (32*(outcome-expectedScore1))
    newScore2 = score2 + (32*(outcome-expectedScore2))
    return newScore1,newScore2

