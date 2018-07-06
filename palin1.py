def isPalindrome(str):
 
    
    for i in xrange(0, len(str)/2): 
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 

s = "laptop"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")
