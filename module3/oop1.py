"""
lab1:
Scenario
We need a class able to count seconds. Easy? Not as much as you may think as we're going to have some specific expectations.

Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23] - we will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside objects by +1/-1 second respectively.
Use the following hints:

all object's properties should be private;
consider writing a separate function (not method!) to format the time string.
Complete the template we've provided in the editor. Run your code and check whether the output looks the same as ours.

Expected output
23:59:59
00:00:00
23:59:59
"""


class Timer(object):
    def __init__(self, h, m, s):
        self.__h = h
        self.__m = m
        self.__s = s

    def __str__(self):
        return f"{self.__h:02}:{self.__m:02}:{self.__s:02}"

    def next_sec(self):
        self.__s += 1
        if self.__s > 59:
            self.__s = 0
            self.__m += 1
            if self.__m > 59:
                self.__m = 0
                self.__h += 1
                if self.__h > 23:
                    self.__h = 0

    def prev_sec(self):
        self.__s -= 1
        if self.__s < 0:
            self.__s = 59
            self.__m -= 1
            if self.__m < 0:
                self.__m = 59
                self.__h -= 1
                if self.__h < 0:
                    self.__h = 23


"""
Scenario
Your task is to implement a class called Weeker. Yes, your eyes don't deceive you – this name comes from the fact that objects of that class will be able to store and to manipulate the days of the week.

The class constructor accepts one argument – a string. The string represents the name of the day of the week and the only acceptable values must come from the following set:

Mon Tue Wed Thu Fri Sat Sun

Invoking the constructor with an argument from outside this set should raise the WeekDayError exception (define it yourself; don't worry, we'll talk about the objective nature of exceptions soon). The class should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the same form as the constructor arguments;
the class should be equipped with one-parameter methods called add_days(n) and subtract_days(n), with n being an integer number and updating the day of week stored inside the object in the way reflecting the change of date by the indicated number of days, forward or backward.
all object's properties should be private;
Complete the template we've provided in the editor and run your code and check whether your output looks the same as ours.

Expected output
Mon
Tue
Sun
Sorry, I can't serve your request.
"""


class WeekDayError(Exception):
    ...


class Weeker(object):
    __days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

    def __init__(self, day):
        if day not in self.__days:
            raise WeekDayError
        self.__day = day

    def __str__(self):
        return self.__day

    def add_days(self, days: int):
        day = self.__days.index(self.__day) + days % 7
        self.__day = self.__days[day]

    def subtract_days(self, days: int):
        day = self.__days.index(self.__day) - days % 7
        self.__day = self.__days[day]


def main():
    timer = Timer(23, 59, 59)
    print(f"Current time: {timer}")
    for _ in range(100):
        timer.next_sec()
        print(f"Time after a sec increment: {timer}")

    for _ in range(100):
        timer.prev_sec()
        print(f"Time after a sec decrement: {timer}")

    try:
        weekday = Weeker('Mon')
        print(weekday)

        weekday.add_days(15)
        print(weekday)

        weekday.subtract_days(23)
        print(weekday)

        weekday = Weeker('Monday')
    except WeekDayError:
        print("Sorry, I can't serve your request.")


if __name__ == "__main__":
    main()
