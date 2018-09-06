def even_number_of_evens(numbers):
    if not numbers: #could also be written as if numbers == []:
        return False
    else:
        evens_count = 0
        for number in numbers:
            if (number % 2 == 0):
                evens_count += 1
    print("p-final: " + str(evens_count))
    if (evens_count == 0):  #this must come first, as Python sees 0 as being divisible, unlike regular maths where this would throw an error
        return False
    elif (evens_count % 2 == 0):
        return True
    else:
        return False


assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All tests passed!")