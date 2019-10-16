numbers = [1, 2, 3, (10, 20), 4, 5]

counter = 0

for n in numbers:
    if isinstance(n, tuple):
        break
    counter += 1
print(counter)


#zadanie 1
#Utwórz dowolną krotkę, w której elementy mogą się powtarzać. Przekształć ją w set.

uno = (1, 2, 3, 5, 3)

set(uno)
