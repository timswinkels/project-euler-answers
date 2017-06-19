def getMultiplesOfUntil(multiples, limit):
  answer = sum(x for x in range(limit) if (x % 3 == 0 or x % 5 == 0))
  return answer

print(getMultiplesOfUntil(4, 1000))
