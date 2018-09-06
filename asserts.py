x = 2
y = 1

# This is our test - the curly braces and format puts the given values of x & y into the error statement:
assert x < y, "{0} should be less than {1}".format(x,y)

print(x + y)