def evenFibonacciSum(limit):
  answer = 0

  x = [1, 1]

  while x[0] <= limit:
    fibonacci = sum(x)
    if not fibonacci % 2: answer += fibonacci

    x = [fibonacci, x[0]]

  return answer

print(evenFibonacciSum(4000000))
