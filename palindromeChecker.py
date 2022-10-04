def palindromeChecker(checkString):
    
    comparision = checkString[::-1]
    if comparision == "":
        return False
    if comparision == checkString:
        return True
    else:
        return False
        
check = input("What do you want to check?: ")
if palindromeChecker(check):
    print("It's a palindrome")
else:
    print("It's not a palindrome")