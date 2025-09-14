"""
Creating user defined exceptions
"""


class MySimpleException(Exception):
    """
    This is the most simple exception
    Doesn't have any attributes, hence uses Exception's attributes
    """
    ...


class MySimpleException1(Exception):
    """
    This is very similer as above but has  default error message
    which will be passed to Exception class
    and that message will be printed upon printing exception
    """

    def __init__(self, message="MySimpleException1 with default message"):
        super().__init__(message)


class MyCustomException(Exception):
    """
    This class (exception) has custom arguments
    currently set to default values.
    something like that you can pass those paramerters during raising exception
    """

    def __init__(self, message="some message", arg1="Some argument", arg2=30, arg3=20):
        """
        Learning: If you dont call super class's init method is fine
        but can't see whart are the args it has
        if you need to know excption class's attributes, please pass those to base class's init method
        """
        super().__init__(message, arg1, arg2, arg3)  # calling base class init method
        self.__message = message
        self.__arg1 = arg1
        self.__arg2 = arg2
        self.__arg3 = arg3

    def __str__(self):
        return f"This is customised error message: {self.__message}\narguments are: arg1: {self.__arg1}\narg2: {self.__arg2}\narg3: {self.__arg3}"


def raise_my_simple_exception():
    raise MySimpleException


def raise_my_simple_exception_with_message(
        message="This is user message while raising exception for: MySimpleException"):
    raise MySimpleException(message)


def raise_my_simple_exception_1():
    raise MySimpleException1


def raise_my_custon_exception():
    raise MyCustomException


if __name__ == "__main__":
    # simple exception example
    try:
        raise_my_simple_exception()
    except MySimpleException as e:
        print(f"Exception: {e}")

    # simple exception with custom message
    try:
        raise_my_simple_exception_with_message()
    except MySimpleException as e:
        print(f"Exception: {e}")

    # simple exception1 that has default message
    try:
        raise_my_simple_exception_1()
    except MySimpleException1 as e:
        print(f"Exception: {e}")

    # simple but custom exception
    try:
        raise_my_custon_exception()
    except MyCustomException as e:
        print(f"Exception: {e}")
        print(f"Exception arguments are: {e.args}")
