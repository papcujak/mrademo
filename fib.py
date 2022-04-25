# Program to display the Fibonacci sequence up to n-th term

recursive = input("Run recursive?")
nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   if recursive == "True":
     for i in range(nterms):
       print(recur_fibo(i))
   else:
     while count < nterms:
         print(n1)
         nth = n1 + n2
         # update values
         n1 = n2
         n2 = nth
         count += 1
