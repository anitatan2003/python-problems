import cse163_utils


# Write your function here!
"""Write a function named largest_magnitude that
takes a parameter data that stores this earthquakes
dataset represented as a list of dictionaries as a
parameter. It should return the name of the location
that experienced the largest earthquake in the dataset.
If there are no rows in the dataset, it should return None .

If you only look at the rows of the dataset shown above,
the result would be 'Burma' because it had the earthquake
 with the largest magnitude (4.9).

You should not assume the dataset passed has the exact
same values or the number of rows like the one shown above.
For example, you should not assume the dataset has more than
one row. However, you should assume the dataset provided will
have all of the columns provided for any row in the dataset
(we sometimes call the set of columns of a CSV its schema )."""


def largest_magnitude(data):
    if len(data) == 0:
        return None
    max_magnitude = 0
    for location in data:
        if location['magnitude'] > max_magnitude:
            max_magnitude = location['magnitude']
            max_magnitude_location = location['name']
    return max_magnitude_location
  

def main():
    data = cse163_utils.parse('earthquakes.csv')
    print(largest_magnitude(data))


if __name__ == '__main__':
    main()
