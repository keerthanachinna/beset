def isDivBy10(bin) :
    n = len(bin)
    if (bin[n - 1] == '1') :
        return False
        sum = 0
     i = n - 2
    while i >= 0 :
          if (bin[i] == '1') :
           posFromRight = n - i - 1
            if (posFromRight % 4 == 1) :
                sum = sum + 2
            elif (posFromRight % 4 == 2) :
                sum = sum + 4
            elif (posFromRight % 4 == 3) :
                sum = sum + 8
            elif (posFromRight % 4 == 0) :
                sum = sum + 6
            i = i - 1
         if (sum % 10 == 0) :
        return True
        else:
          return False
         
bin = "1100101"
if (isDivBy10(bin)== True) :
    print("Yes")
else :
    print("No")
 

