def alternatingSums(a):
    sum1 = 0
    sum2 = 0
    teams = []
    for i in range(len(a)):
        if (i % 2 == 0):
            sum1 += a[i]
        else:
            sum2 += a[i]
    teams.append(sum1)
    teams.append(sum2)
    return teams
