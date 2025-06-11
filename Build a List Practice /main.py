# Write your function here
"""takes a start number and stop number and 
returns a list of all “fun” numbers between 
start (inclusive) and stop (exclusive). A 
number is “fun” if it is divisible by 2 or 
divisible by 5. The result should have the numbers 
arranged from smallest to largest.

If there or no fun numbers within the 
range start (inclusive) and stop (exclusive) 
(e.g. if stop is less than start meaning the 
range doesn’t have any numbers in it), the function 
should return an empty list."""


def fun_numbers(start, end):
    list = []

    if start >= end:
        return list
    
    for i in range(start, end):
        if i % 2 == 0 or i % 5 == 0:
            list.append(i)

    return list


def main():
    print(fun_numbers(2, 16))
    print(fun_numbers(5, 5))


if __name__ == "__main__":
    main()
