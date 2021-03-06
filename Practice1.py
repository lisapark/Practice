"""
Hi Lisa.
For your exercises, I think one of the easiest ways to practice
is to go through the Project Euler problems. For reference,
they can be found at https://projecteuler.net/

I'll come up with more extensive problems but this should
be a good start.

The first few Project Euler problems are listed here to start.
They should be simple enough to come up with quick solutions,
but also complex enough to where you need to remember actual
Python.

I generalized the problems, because that's what you should do
when you program. However, I listed the original value in the
problem for reference.
"""
import math

def MultiplesOf3Or5(n):
	"""
	Problem 1:
	If we list all the natural numbers below 10 that are multiples
	of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples
	is 23.

	Find the sum of all the multiples of 3 or 5 below n.

	n=1000
	"""
	sum35 = 0
	for i in range(n):
		if i%3==0 or i%5 ==0:
			sum35 = sum35 + i
	return sum35

print MultiplesOf3Or5(1000)

def SumFibonacciEven(n):
	"""
	Problem 2:
	Each new term in the Fibonacci sequence is generated by adding
	the previous two terms. By starting with 1 and 2, the first
	10 terms will be:
		1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

	By considering the terms in the Fibonacci sequence whose values
	do not exceed n, find the sum of the even valued terms.

	n=4000000
	"""
	fib = [1,2]
	sumfib = 0
	while fib[0] <= n:
		if fib[0]%2 == 0:
			sumfib = sumfib + fib[0]
		fib.append(fib[1]+fib[0])
		fib.pop(0)
	return sumfib

print SumFibonacciEven(4000000)


def LargestPrimeFactor(n):
	"""
	Problem 3:
	The prime factors of 13195 are 5, 7, 13, and 29.

	What is the largest prime factor of the number n?

	n=600851475143
	"""
	primeNumbers = []
	i = 2
	while i <= n:
		if n%i == 0:
			isPrime = True
			for primeNum in primeNumbers:
				if i%primeNum == 0:
					isPrime = False
			if isPrime:
				primeNumbers.append(i)
			n = n/i
		i = i + 1
	return primeNumbers.pop()

print LargestPrimeFactor(6857)

def LargestPalindromeProduct(n):
	"""
	Problem 4:
	A palindromic number reads the same both ways. The largest
	palindrome made from the product of two 2-digi numbers is
	9009 = 91 x 99.

	Find the largest palindrome made from the product of two
	n-digit numbers.


	n=3
	"""

	def isPalindrome(mult_ij):
		stringMult = str(mult_ij)
		if stringMult == stringMult[::-1]:
			return True
		return False
	nNines = int(math.pow(10,n)) -1
	reverseRange = range(nNines + 1)
	reverseRange = reverseRange[::-1]
	for i in reverseRange:
		j = nNines
		while j >= i:
			mult_ij = i*j
			if isPalindrome(mult_ij):
				return mult_ij
			j = j - 1
	return -1

print LargestPalindromeProduct(3)

def SmallestMultiple(n):
	"""
	Problem 5:
	2520 is the smallest number that can be divided by each
	of the numbers from 1 to 10 without any remainder.

	What is the smallest positive number that is evenly divisible
	by all of the numbers from 1 to n?

	n=20
	"""
	smallestMultiple = 1
	allDivisible = False
	while allDivisible==False:
		allDivisible = True
		for i in range(1,n+1):
			if smallestMultiple%i !=0:

				noDiv = True
				for j in range(1,i)[::-1]:
					if i%j==0:
						smallestMultiple = smallestMultiple * i/j
						print smallestMultiple
						noDiv = False
						break

				if noDiv:
					smallestMultiple = smallestMultiple * i

				allDivisible = False
				break
	return smallestMultiple

print SmallestMultiple(20)
