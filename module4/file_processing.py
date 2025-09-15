# reading a file
def read_file(file):
    with open(file=file, mode="r") as f:
        print(f.read())  # this read entire file contenet and printed to terminal
        f.seek(0)  # this will set the cursor to starting of the stream

        print(f.readlines())  # this returns list of lines
        f.seek(0)  # this will set the cursor to starting of the stream

        for line in f:  # this helps to iterate through each line and access each line
            print(line)


def main():
    read_file("module4/test_file.txt")


if __name__ == "__main__":
    main()
