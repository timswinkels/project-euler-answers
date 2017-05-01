start = 0
stop = 1000
multiples_of_three = range(start, stop, 3)
multiples_of_five = range(start, stop, 5)

multiples = multiples_of_three + multiples_of_five

print(multiples)

output = 'The sum of the multiples of 3 or 5 from 0 till 1000 is: %s'
print(output % sum(multiples))
