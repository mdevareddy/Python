num = int(input("Enter Number:")
temp = num
sum = 0
while temp>0:
      digit = temp%10
      sum += digit**3
      temp = temp//10
if sum == num:
   print("Amstrong Number")
else:
    print("Not Amstrong Number")
      
