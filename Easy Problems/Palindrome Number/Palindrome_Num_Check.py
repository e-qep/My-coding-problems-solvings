"""
    This, as the name and README.md says which I'd assume you read, is the palindrome number problem.
    Basically you input a number, and it checks if it's the same if you read it like manga.
"""

def is_palindrome(x_init):
    x = x_init
    if x < 0:                       #what this does is basically simplifying the process a lot as all negative numbers are not palindromes
        return False
    reverse = 0
    while x != 0:                   # This just takes the number and sees the last digit by dividing by 10,
        y = x % 10                  # Then it makes it so the second digit becomes the first digit and so on.
        x = (x - y) / 10            # Pretty cool I's say so myself.
        reverse = reverse * 10 + y
    return reverse == x_init        #if it is a palindrome the reverse should be equal to the number so the output should be true,
                                    # but if they're not equal (palindromes) then its false

number = int(input("Number: "))

print(is_palindrome(number))
