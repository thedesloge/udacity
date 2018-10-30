def popularity(p): #circular definition, will never actually end
    score = 0
    for f in friends(p):
        score += popularity(f)
    return score
