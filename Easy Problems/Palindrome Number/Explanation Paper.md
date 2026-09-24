# <center>Palindrome Number.</center>

> A palindrome number is a number that reads the same **forward and backward**. 
> This term can also be used for words (try saying *racecar* backwards, I dare you)

---

- 121  (palindrome)
- 1331 (palindrome)
- 123  (impostor)

---

## The Idea

Take a number, make it do a barrel roll, and check if it’s the same.

If yes → congrats I guess, you found a symemtrical number.
If no → it’s just a number.

---

## Simple Approach

1. Save the original number
2. Reverse the number
3. Compare

---

## Example (python)

```python
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
```
---

## Actual Fun Fact
> This exact idea works in any mathematical base.
>> You can do it in binary, base 10, base 12, base √3, base e^iπ and any other imaginable base.

> If you ***somehow*** don't know what a base is I'd advise you to look here: [Mathematical Bases](https://simple.wikipedia.org/wiki/Base_(mathematics) "You ACTUALLY don't know what a base is??")

