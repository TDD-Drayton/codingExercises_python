#Is it a palindrome?

rotor=str(input("I will tell you if your input is a palindrome: "))
#string reversal
racecar=rotor[::-1]
if rotor==racecar:
    print("Yes, that's a palindrome. Other cool palindromes include the words rotor and racecar")
else:
    print("Not a palindrome.")
