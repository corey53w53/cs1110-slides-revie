def count_vowels(s):
    """
    Returns: number of vowels in a string

    Vowels are a,e,i,o,u

    Upper case and lower case both work

    Examples:...

    Paramter s: The string to check for vowels
    Precondition: s is a string
    """
    r=0
    for letter in s.lower():
        if letter in "aeiou":
            r+=1
    return r
print(count_vowels("aeiou"))