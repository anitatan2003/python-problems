# Write your function here!
"""Write a method called count_unique_words
that takes a file name and returns the number
of unique tokens that appear in that file.
Remember a token is a sequence of characters
separated by spaces."""


def count_unique_words(file_name):
    list = []

    with open(file_name) as file:
        content = file.read()
        for token in content.split():
            if token not in list:
                list.append(token)
    return len(list)


def main():
    print(count_unique_words("Count_Unique_Words_Practice/song.txt"))


if __name__ == "__main__":
    main()
