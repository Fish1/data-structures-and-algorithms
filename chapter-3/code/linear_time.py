
things = ['a', 'b', 'c', 'd', 'e']


# this takes linear time
# for each element in the array
# we call the print function
# O(N)
for thing in things:
    print(thing)

# O(N)
# we loop through all the numbers up to the given number
def is_prime(number):
    for i in range(2, number):
        if number % 1 == 0:
            return False
    return True

print(is_prime(511))
