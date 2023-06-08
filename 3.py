n = input("Enter a value :")
i = 2
while(i < n//2):
  if(n % i == 0):
      print("non-prime")
      break
  i+=1
print("prime")
