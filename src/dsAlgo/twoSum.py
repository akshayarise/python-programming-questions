# Check if pair with given Sum exists in Array (Two Sum)

n = int(input("Enter the number of elements you want to enter\n"))
x = int(input("enter the sum\n"))
arr = []

for i in range(n):
   arr.append(int(input("enter the element\n")))


def twoSum(arr):
 arr.sort()
 print('arr ',arr)
 i=0
 j=n-1
 while i<=j:
   sum = arr[i]+arr[j]
   if sum==x:
      return 1
   elif sum > x:
      j= j-1
   else:
      i=i+1
 return 0

if(twoSum(arr)):
   print("sum is present in the array\n")
else:
   print("sum is not present in the array\n")
