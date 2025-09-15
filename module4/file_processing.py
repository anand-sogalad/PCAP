# reading a file
def read_file(file):
    with open(file=file, mode="r") as f:
        print(f.read())  # this read entire file contenet and printed to terminal
        f.seek(0)  # this will set the cursor to starting of the stream

        print(f.readlines())  # this returns list of lines
        f.seek(0)  # this will set the cursor to starting of the stream

        for line in f:  # this helps to iterate through each line and access each line
            print(line)


"""
Scenario
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

Assuming that the test file contains just one line filled with:

aBc
samplefile.txt

the expected output should look as follows:

a -> 1
b -> 1
c -> 1
"""

"""
Scenario
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
Assuming that the input file contains just one line filled with:

cBabAa
samplefile.txt

the expected output should look as follows:

a -> 3
b -> 2
c -> 1
"""


def histogram(_str):
    _str = _str.strip().replace(" ", "").lower()
    [print(f"{i} --> {j}") for i, j in sorted({(s, _str.count(s)) for s in _str}, key=lambda x: x[-1], reverse=True)]


def main():
    read_file("module4/test_file.txt")
    histogram("aBcCbacbbb")


if __name__ == "__main__":
    main()
