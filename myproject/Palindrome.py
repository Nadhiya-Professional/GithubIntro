str= input("Please enter the string:)
new_Str =''
length = len(str)
for i in range(-1,-(length+1),-1):  
  new_Str += str[i]
if str.upper() == new_str.upper() :
   print("The string is a palindrome")        
else:
  print("The word os not a palindrome")
