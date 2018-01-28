under = 1.0
over = 1.0
N = 2000
for i in range (N):
    under = under/2
    over = over*2
    print ("Loop: ", i, " ", under, " ", over)
