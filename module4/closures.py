"""
Closures are functions that capture variables from their enclosing scope.
"""


def outer(var):
    loc = var

    def inner():
        return loc

    return inner


x = outer(1)
print(x())
