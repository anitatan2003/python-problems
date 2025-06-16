# Define your function up here!
"""Write a function called area_codes that
takes a list of str as input where each str
in the list is a phone number and returns the
number of unique area codes found in those
phone numbers. Each phone number will be
of the format '123-456-7890' and the area
code is the first three characters in
the str ."""


def area_codes(str):
    unique_area_codes = set()
    for number in str:
        area_code = number.split('-')[0]
        unique_area_codes.add(area_code)

    return unique_area_codes


def main():
    print(area_codes([
        '123-456-7890',
        '206-123-45676',
        '123-000-0000',
        '425-999-9999'
    ]))
    

if __name__ == '__main__':
    main()
