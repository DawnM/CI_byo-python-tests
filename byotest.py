# def is_even(number):
#     return number % 2 == 0 # will return true or false accordlingly
    
# def number_of_evens(numbers):
#     evens = sum([1 for n in numbers if is_even(n)])
#     return evens
    
def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(actual, expected):
    assert actual != expected, "Did not expect {0}, but got {1}".format(actual, expected)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)

def test_not_in(collection, item):
    assert item not in collection, "{0} does contain {1}".format(collection, item)

# collection = [1, 2, 3, 4, 5]

# test_are_equal(number_of_evens([1, 2, 3, 4, 5]), 2)
# test_not_equal(5, 2)
# test_is_in(collection, 3)
# test_not_in(collection, 6)
# print("All tests ran")