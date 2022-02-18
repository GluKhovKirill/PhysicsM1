#CONFIG 
L = [0.35, 0.3, 0.25, 0.2]  # Длина веревки в метрах
filename = 'Phys1' # текстовый файл с данными
#--------------------------------------------------


from decimal import Decimal
import json


with open(filename) as f: data = f.readlines()

X = []
period = []

for i in data:
    if i[0].isdigit():
        period.append(float(i.replace(',','.')))
    else:
        if period:
            X.append(period)
        period = []
if period:
    X.append(period)

Ns = [len(i) for i in X]

MAX = len(max(X))
for i in range(4):
    X[i] += [-8]*(MAX-len(X[i]))

with open('data.json','w') as file:
    data = {'periods': X,
            'lengths': L,
            'Ns': Ns}
    file.write(json.dumps(data))