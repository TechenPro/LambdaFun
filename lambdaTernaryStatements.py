# Ternary Statements may be replicated through the use of tuple indexing.
# This is because False naturally evaluates to 0, while True evaluates to 1
# Thus, we can put a boolean statement in the '[]' used to pick the element of a tuple

a, b = 10, 20
print((False, True)[a < b]) # Prints True

# Dictionaries may also be used in order to more clearly display your logic to other readers
print({True: "This is True", False: "This is False"}[a < b]) # Prints `This is True`

# If we store functions within the dictionary, we can add a function call to the end of the statement
# and execute that function from the ternary statement
def test1():
    print("Executing 1")

def test2():
    print("Executing 2")

{True: test1, False: test2}[a < b]() # Calls test1()

# While this does indeed work, we can run into problems when using long running functions, as a dictionaries do not
# have short-circuiting logic. This means both items are akways evaluated, which is especially problematic if you
# have looping functions.
#
# The solution for this is to use lambda expressions

(lambda: test1, lambda: test2)[a < b]()() # Calls test2()
print((lambda: a, lambda: b)[a < b]()) # Prints b
