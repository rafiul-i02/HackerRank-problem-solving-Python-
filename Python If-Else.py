n=int(input("n"))

if n%2!=0 and 1<=n<=100:
   print("Weird")
elif n%2==0 and 6<=n<=20:
   print("Weird")
elif n%2==0 and 2<=n<=5:
   print("Not Weird")
elif n%2==0 and 20<n<=100:
   print("Not Weird")   
else:
   print("Not applicable") 