# Define switch_pairs up here!
def switch_pairs(s):
    """
    Write a function named switch_pairs that accepts a string 
    as a parameter and returns that string with each pair of 
    neighboring letters reversed. If the string has an odd number 
    of letters, the last letter should not be modified. For example, 
    the call switch_pairs("example") should return "xemalpe" and the 
    call switch_pairs("hello there") should return "ehll ohtree" .
    """
    if len(s) == 1:
        return s
    
    switched = ""
    i = 0
    print(len(s))
    s = s.strip()
    while i < len(s):
        if (len(s) % 2) != 0 and i + 1 == len(s):
            switched += s[-1]
        else:
            switched += s[i + 1]
            switched += s[i]
        i += 2

    return switched

def main():
    print(switch_pairs("hello there"))


if __name__ == '__main__':
    main()
