# main.py
# author Julia Frances <jrf343@drexel.edu>
# date July 13, 2022

# This is a Python implementation of Eratosthenes'
# sieve, a classic algorithm used to identify small prime 
# numbers in some range. This file is meant to accompany my research and analysis
# on the algorithm, which can be found on GitHub.
# as well. The implementation here is partially based 
# on the Wikipedia pseudocode found at 
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

def Eratosthenes_Sieve(num):
  # begin by assuming all numbers are prime 
  prime_list = [True for c in range(num+1)]
  p = 2 # begin counting with 2
  while p**2 <= num: # until the counting number^2 >= the limit
    # Here is where my implementation differs from Wikipedia's* (see below)
    for c in range(p**2, num, p): # the counting by p is the critical aspect
      prime_list[c] = False # if the number is reached by counting it is not prime 
    p += 1
  for c in range(2, num):
    if prime_list[c] == True: 
      print(c)

print("List of Primes:")
Eratosthenes_Sieve(100)
      
    
# *Wikipedia's psuedocode included the (paraphrased) line
# "if prime_list[c] == True:" at this point. However, based on my 
# research (see paper & sources), the original algorithm by 
# Eratosthenes involved eliminiating numbers multiple times, and
# therefore the implementation would not skip the numbers already 
# deemed not prime. An implementation which skipped eliminated numbers
# would be Euler's modification to the original algorithm (see paper).
    
  
