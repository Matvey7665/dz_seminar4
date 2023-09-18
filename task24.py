n = int(input())
list_bushes = list(map(int, input().split()))
list_bushes.append(list_bushes[0])
list_bushes.append(list_bushes[1])
summa = list_bushes[0] + list_bushes[1] + list_bushes[2]
for i in range(2, n + 1):
    summa = max(summa, list_bushes[i] + list_bushes[i - 1] + list_bushes[i + 1])
print(summa)
