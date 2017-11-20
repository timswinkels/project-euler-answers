# Count sum of event Fibonacci numbers until "limit"
def evenFibonacciSum(limit):
  answer = 0

  # Define x as the two numbers to add, in order to get
  # a Fibonacci number. Starting at 1 and 1.
  #
  # https://en.wikipedia.org/wiki/Fibonacci_number
  x = [1, 1]

  # Start building Fibonacci numbers and counting the even numbers
  while x[0] <= limit:

    # Define next Fibonacci number
    fibonacci = sum(x)

    # Check if Fibonacci number is even, if so add it to the sum
    if not fibonacci % 2: answer += fibonacci

    # Define next numbers fo Fibonacci
    x = [fibonacci, x[0]]

  return answer

print(evenFibonacciSum(4000000))
