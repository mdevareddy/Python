num = int(input("Enter Number:"))
temp = num
rev = 0
while num!=0:
    digit = num%10
    rev = rev*10+digit
    num = num//10
if temp == rev:
    print("Palindrome Number")    
else:
    print("Not Palindrome Number")

# anagram String without recursing
s1 = input("Enter String:")
s2 = input("Enter String:")

if (sorted(s1)==sorted(s2)):
    print("Anagram String")
else:
    print("Not Anagram String")






# Anagram String With Recursing
def IsAnagram(s1,s2):
    if (sorted(s1)==sorted(s2)):
        print("Anagram String")
    else:
        print("Not Anagram Stirng")
s1 = 'listen' 
s2 = 'silent'
IsAnagram(s1,s2)               

    
    
