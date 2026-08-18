def revString(str):
    print(str)
    for i in range(len(str)-1, -1,-1):
        print(str[i],end=" ")


#----------palindrom---------------------#

def stringPalindrome(s):
    tempstring = "";
    count = 0

    for i in range(len(s)-1, -1, -1):
       tempstring += s[i]
    #count = count + 1
    print(tempstring)

    if tempstring == s:
      print("String Palindrome checked")
    else:
     print("String not Palindrome checked")
#----------Angrams---------------------#
 def stringAngrams(s1,s2):
      if sorted(s1) == sorted(s2):
          print("ANGRAMS")
      else:
          print("NOT ANGRAMS")
