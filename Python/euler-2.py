"""
@author mbartoli

Even Fibonacci numbers
Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def evenFib(upperBound,startA,startB):
  evenFibNums = set()
  if not startA & 1: # interger & 1 return false if odd
    evenFibNums.add(startA)
  while(startB < upperBound):
    if not startB & 1:
      evenFibNums.add(startB)
    startA,startB = startB, startA+startB
  return evenFibNums
  

def main():
  startA,startB = 1,2
  upperBound = 4000000
  print sum(evenFib(upperBound,startA,startB))

if __name__ == "__main__":
  main() 

