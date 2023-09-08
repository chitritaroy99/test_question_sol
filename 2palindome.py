def palindrome (str) :
    
    rev = str[::-1]
    if rev == str :
        return 1
    else :
        return 0

# driver code

str = input() 
print(palindrome (str))