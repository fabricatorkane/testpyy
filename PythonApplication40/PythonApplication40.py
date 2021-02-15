import random
X = []
for i in range(1,1000):
       X.append(random.randint(-1000,1000))
print(X)
#id1 = 0
#id2 = 0


def find_odd_numb(X):
    global id1
    id1 = 0
    global id2
    id2 = 0
    for i in range(len(X)):
        if X[i]%2 != 0 and (X[i + 1])%2 != 0:
            id1 = i
            id2 = i + 1
            break
    return(id1, id2)

find_odd_numb(X)
if id1 == 0 and id2 == 0:
    print('Здесь нет пары нечетных чисел :( ')
else:
    print(id1, id2)