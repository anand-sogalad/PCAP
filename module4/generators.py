"""
In python generators are piece of code that is able to produce series of values and controls the iteration
Generators are functions/methods that keeps the state of the last method call
"""
from tokenize import endpats


class GeneratorExamples(object):

    @staticmethod
    def range_function(*args):
        for i in range(*args):
            print(i, end=" ")

    @staticmethod
    def custom_range(*args):
        for i in range(*args):
            yield i


"""
Interators are also same but implemeted using iter protocol and class
"""


class MyIter(object):
    def __init__(self, *args):
        if len(args) == 0:
            raise Exception("Atleast 1 argument needed")
        elif len(args) == 1:
            self.__start = 0
            self.__stop = args[0]
            self.__step = 1
        elif len(args) == 2:
            self.__start = args[0]
            self.__stop = args[1]
            self.__step = 1
        else:
            self.__start = args[0]
            self.__stop = args[1]
            self.__step = args[2]

    def __iter__(self):
        return self

    def __next__(self):
        self.__start += self.__step
        if self.__start >= self.__stop:
            raise StopIteration
        return self.__start


"""
Impement a generator that yields power of 2 till a given number
"""


class GeneratorExamples1(GeneratorExamples):
    @staticmethod
    def power_of_two(n):
        for i in range(1, n + 1):
            yield pow(i, 2)


def main():
    GeneratorExamples.range_function(1, 10)
    print()

    for i in GeneratorExamples.custom_range(1, 10):
        print(i, end=" ")
    print()

    for i in MyIter(0, 10, 2):
        print(i, end=" ")
    print()

    for i in GeneratorExamples1.power_of_two(10):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
