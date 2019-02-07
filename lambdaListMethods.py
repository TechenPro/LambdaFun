################# Lambda Sort #################
# Creates a list of strings from the user input, with each new element starting after a comma and a space ", "
stringList = [str(x) for x in input().split(", ")]
# Lamda functions may be passed into the sort key parameter.
# This allows you to perform various tasks to sort based on, such as sorting by 
# a specific part of the list item
# In the below case, the sort mechanism is based on the numbers folowing 3 characters after an underscore
# For example, it would sort based on the numbers at the end of this string `testStringlskdjfhslkdjfh_num3`
# It takes the part that follows the underscore, and starting at the 4th char, begins sorting based on integer value
stringList.sort(key= lambda x: int(x.split("_")[1][3:]))
print(stringList)

################# Lambda Map #################
mapList = list(range(10))
# Takes all list elements, squares them, then multiplies the result by 2
mapList = list(map(lambda x: 2*(x**2), mapList))
print("\n\nMapped List")
print(mapList)

################# List Comprehension Equivalent 2x faster #################
# Uses an implicit lambda function
mapList = list(range(10))
mapList = [2*(x**2) for x in mapList]
print("\n\nComprehended List")
print(mapList)



################# Lambda Filter #################
filterList = list(range(10))
# Filters out all even numbers
filterList = list(filter(lambda x: x%2==1, filterList))
print("\n\nFiltered List")
print(filterList)


################# Lambda Reduce #################
from functools import reduce
reduceList = list(range(10))
# Adds the next list element to the first one. This continues until only 1 element remains
reducedInt = reduce(lambda x, y: x+y, reduceList)
print("\n\nReduced List")
print(reducedInt)
