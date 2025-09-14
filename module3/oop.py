"""
Builing Stack using Oop
"""


# class representation of Stack object
class Stack(object):
    def __init__(self):  # this is the constructor method
        self.__stack = list()  # a list that is used to store stack data

    def push(self, val):  # this method used to append the data to the stack list
        self.__stack.append(val)

    def pop(self):  # this method used to remove and return last value in the stack list
        return self.__stack.pop()


# creating another class that is going to be
# derived from the origional class
# this class will be able to track the sume of the all the elements present in the stack currently
class AdvancedStack1(Stack):
    def __init__(self):
        super().__init__()
        self.__sum = 0

    def push(self, val):
        super().push(val)
        self.__sum += val

    def pop(self):
        val = super().pop()
        self.__sum -= val
        return val

    def sum(self):
        return self.__sum


"""
lab1:
Scenario
We've showed you recently how to extend Stack possibilities by defining a new class (i.e., a subclass) which retains all inherited traits and adds some new ones.

Your task is to extend the Stack class behavior in such a way so that the class is able to count all the elements that are pushed and popped (we assume that counting pops is enough). Use the Stack class we've provided in the editor.

Follow the hints:

introduce a property designed to count pop operations and name it in a way which guarantees hiding it;
initialize it to zero inside the constructor;
provide a method which returns the value currently assigned to the counter (name it get_counter()).
Complete the code in the editor. Run it to check whether your code outputs 100.
"""


# I am going to create a class that derives from AdvancedStack1
class AdvancedStack2(AdvancedStack1):
    def __init__(self):
        super().__init__()  # created this method only to define new instance variable
        self.__counter = 0

    # adding counter to only pop method as counting pop method is more than enough
    # as per propblem statement
    def pop(self):
        val = super().pop()
        self.__counter += 1
        return val

    def counter(self):
        return self.__counter


"""
lab2:
Scenario
As you already know, a stack is a data structure realizing the LIFO (Last In – First Out) model. It's easy and you've already grown perfectly accustomed to it.

Let's try something new now. A queue is a data model characterized by the term FIFO: First In – First Out. Note: a regular queue (line) you know from shops or post offices works exactly in the same way – a customer who came first is served first too.

Your task is to implement the Queue class with two basic operations:

put(element), which puts an element at end of the queue;
get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.)
Follow the hints:

use a list as your storage (just like we did with the stack)
put() should append elements to the beginning of the list, while get() should remove the elements from the end of the list;
define a new exception named QueueError (choose an exception to derive it from) and raise it when get() tries to operate on an empty list.
Complete the code we've provided in the editor. Run it to check whether its output is similar to ours.

Expected output
1
dog
False
Queue error
"""


# creating a Queue class
class Queue(object):
    def __init__(self):
        self.__queue = list()

    def put(self, val):
        self.__queue.insert(0, val)

    def get(self):
        if self.is_empty():
            raise QueueError
        return self.__queue.pop()

    def is_empty(self):
        return len(self.__queue) == 0


class QueueError(IndexError):
    pass


def main():
    simple_stack = Stack()  # creating stack object
    # adding values to the stack list
    simple_stack.push(3)
    simple_stack.push(2)
    simple_stack.push(1)

    # removing last values from the stack
    print(f"Removed value: {simple_stack.pop()}")
    print(f"Removed value: {simple_stack.pop()}")
    print(f"Removed value: {simple_stack.pop()}")
    # ------------------------------------------------------

    # creating advanced stack object
    advanced_stack = AdvancedStack1()

    # adding values to stack list
    advanced_stack.push(3)
    advanced_stack.push(2)
    advanced_stack.push(1)

    # removing values from stack lisst
    print(f"Sum of the stack: {advanced_stack.sum()}")

    print(f"Removed value: {advanced_stack.pop()}")
    print(f"Sum of the stack: {advanced_stack.sum()}")

    print(f"Removed value: {advanced_stack.pop()}")
    print(f"Sum of the stack: {advanced_stack.sum()}")

    print(f"Removed value: {advanced_stack.pop()}")
    print(f"Sum of the stack: {advanced_stack.sum()}")
    # ------------------------------------------------------
    # creating object of AdvancedStack2
    stk = AdvancedStack2()
    for i in range(100):
        stk.push(i)
        stk.pop()
    print(stk.counter())
    # ------------------------------------------------------
    que = Queue()
    que.put(1)
    que.put("dog")
    que.put(False)
    try:
        for i in range(4):
            print(que.get())
    except QueueError:
        print("Queue error")


if __name__ == "__main__":
    main()  # function invocation
