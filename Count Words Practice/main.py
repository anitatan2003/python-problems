# Write your function here!
"""Write a method called count_words
that takes a file name and returns
a dict that stores the words
as keys and values that counts
the number of times that word
appeared in the file. Remember a token
is a sequence of characters separated by spaces."""


def count_words(file):
    d = {}

    with open(file) as f:
        content = f.read()
        words = content.split()
        for word in words:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
    return d


def main():
    print(count_words("popular_techno_song.txt"))


if __name__ == "__main__":
    main()
