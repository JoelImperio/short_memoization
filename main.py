import pandas as pd
import functools
import time


mt = pd.read_excel('MortalityTable.xlsx')

qx = mt['male']
qy = mt['female']

lapse = 0.05 # per month

pol_inforce = qx * 0
nbr_surrender = qx * 0
pol_inforce[0] = 1
dx = qx * 0

@functools.cache
def inforce():
    for i in range(1, len(qx)):
        dx[i] = pol_inforce[i] * qx[i]
        nbr_surrender[i] = pol_inforce[i-1] * lapse
        pol_inforce[i] = pol_inforce[i - 1] - dx[i] - nbr_surrender[i]
        time.sleep(0.01)

    return pol_inforce

start = time.time()
print(inforce())
print(inforce())

print(time.time() - start)


