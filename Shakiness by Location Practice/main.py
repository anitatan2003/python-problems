import cse163_utils

# Write your function here!
"""We want you to write a function named 
shakiness_by_location that takes a parameter
that represents the earthquakes dataset from
the last problem in the list of dictionaries
format. This function should return a dict
that stores how “shaky” each location in
the dataset is. To define what this means, 
the return value should be a dict whose keys 
are location names and whose values are the 
sum of all the earthquakes’ magnitudes that 
occurred at that location. If there are no 
arthquakes in the dataset, it should return 
an empty dict ."""


def shakiness_by_location(data):
    dict = {}
    if len(data) == 0:
        return dict
   
    for location in data:
        if location['name'] in dict:
            dict[location['name']] += location['magnitude']
        else:
            dict[location['name']] = location['magnitude']
    return dict


def main():
    data = cse163_utils.parse("earthquakes.csv")
    print(shakiness_by_location(data))


if __name__ == "__main__":
    main()
