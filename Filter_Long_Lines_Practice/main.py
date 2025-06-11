def filter_long_lines(file_name, min_words):
    """
    Prints each line in the file with the given name that has
    at least the given number of words in that line.
    """
    # Write your code here :)
    with open(file_name) as file:
        content = file.read()
        print(content)
        for line in content.splitlines():
            if len(line.split()) >= min_words:
                print(line.strip())


def main():
    filter_long_lines("Filter_Long_Lines_Practice/song.txt", 7)


if __name__ == "__main__":
    main()
