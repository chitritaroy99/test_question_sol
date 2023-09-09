def palindrome (str) :
    
    rev = str[::-1] #reverse
    #if reerse and main array same = palindrome
    if rev == str :
        return 1
    else :
        return 0

# driver code

str = input() 
print(palindrome (str))
