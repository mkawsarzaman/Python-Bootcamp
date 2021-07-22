def generate_squares(n): #Create a generator that generates the squares of numbers up to some number N
    for i in range(n):
        yield i**2
for i in generate_squares(10):
        print (i)
        
    
from random import randint #Create a generator that yields "n" random numbers between a low and high number (that are inputs).
def rand_num(low,high,n):
    for i in range(n):
        yield randint(low, high)
for i in rand_num(1, 10, 12):
    print(i)
    
    
s = 'hello' #Use the iter() function to convert the string below into an iterator
s_iter = iter(s)



my_list = [1,2,3,4,5] # Generator Comprehension
gencomp = (item for item in my_list if item > 3)
for item in gencomp:
    print(item)
