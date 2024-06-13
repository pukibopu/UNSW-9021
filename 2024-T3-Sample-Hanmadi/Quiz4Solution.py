# COMP9021 24T1 - Rachid Hamadi
# Sample Exam Question 4
 

'''
Will be tested with a at least equal to 2 and b at most equal to 10_000_000.
'''
    

import sys
from math import sqrt


def f(a, b):
    '''
    >>> f(2, 2)
    There is a unique prime number beween 2 and 2.
    >>> f(2, 3)
    There are 2 prime numbers between 2 and 3.
    >>> f(2, 5)
    There are 3 prime numbers between 2 and 5.
    >>> f(4, 4)
    There is no prime number beween 4 and 4.
    >>> f(14, 16)
    There is no prime number beween 14 and 16.
    >>> f(3, 20)
    There are 7 prime numbers between 3 and 20.
    >>> f(100, 800)
    There are 114 prime numbers between 100 and 800.
    >>> f(123, 456789)
    There are 38194 prime numbers between 123 and 456789.
    '''
    number_of_primes_at_most_equal_to_b = 0

    # normal正常解法    
    # for i in range(a,b+1):
    #     flag=True
    #     for j in range(2,i//2+1):
    #         if i%j==0:
    #             flag=False
    #             break
    #     if flag == True :
    #         number_of_primes_at_most_equal_to_b+=1
    
    #Sieve of Eratosthenes algorithm 埃拉托斯特尼筛法
    table=[True]*(b+1)
    table[0]=table[1]=False

    for i in range(2,int(sqrt(b))+1):
        if table[i]:
            for j in range(i*i,b+1,i):
                table[j]=False
    number_of_primes_at_most_equal_to_b=sum(table[a:b+1])
                
    
    # Insert your code here
    
    if not number_of_primes_at_most_equal_to_b:
        print(f'There is no prime number beween {a} and {b}.')
    elif number_of_primes_at_most_equal_to_b == 1:
        print(f'There is a unique prime number beween {a} and {b}.')
    else:
        print(f'There are {number_of_primes_at_most_equal_to_b} prime numbers between {a} and {b}.')


f(123,456789)