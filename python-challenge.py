
# collect and count customers and store the variables as collections where the count of each charecters name is stored
# as a pair...

path = '/Shared/Projects/python-challenge/customer_products.txt'

#set path to find the discount list.  Set Path to:
# /Shared/Projects/python-challenge/customer_products.txt
def product_assignments(path):
 #   from collections import deque
 from collections import deque
 from functools import reduce
# open the file and put in a while loop
file = open(path, 'r')

text = file.readline()
while (len(text) > 0):
# Split each line by the semicolon to sepaate out products from customers
 split = text.split(";")

# Split all collected customers]9
 customers = split[0].split(",")
 print customers

 products = split[1].split(",")
 print products


 #Step One:


 customer_values = dict((a, len(a)) for a in customers)

 print customer_values.values()
 text = file.readline()

 # Check if e3. If the number of letters in the product's name share s any commo factors (besides 1) with
 # the
 # number of letters in
 # the customer's name then the SS is multiplied by 1.5.

#1. If the number of letters in the product's name is even then the SS is the number of vowels (a, e, i, o, u, y2) in the customer's name multiplied by 1.5.

def set_ss(customers, products):

    for product in products:
        for customer in customers:

            x = count_letters(product)
            y = count_letters(customer)
            common_factor = hcf(x,y)

            if common_factor > 1: multipler = 1.5
            else:
             multipler = 1

            # Apply SS rule #1
            # If the number of letters in the product's name is even then the SS
            # is the number of vowels (a, e, i, o, u, y) in the customer's name
            # multiplied by 1.5.
            # Apply SS rule #2
            # If the number of letters in the product's name is even then the SS
            # is the number of vowels (a, e, i, o, u, y) in the customer's name
            # multiplied by 1.5.
            # Apply SS rule #3
            # If the number of letters in the product's name is even then the SS
            # is the number of vowels (a, e, i, o, u, y) in the customer's name
            # multiplied by 1.5.
            if is_even(product):
                ss[customer] = 1.5 * count_vowels(customer) * multiplier
            else:
                ss[customer] = 1 * count_consonants(customer) * multiplier




# Python program to find the H.C.F of two input number
# http://www.programiz.com/python-programming/examples/hcf
def hcf(x, y):
   """This function takes two
   integers and returns the H.C.F"""

   # choose the smaller number
   if x > y:
       smaller = y
   else:
       smaller = x

   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i

   return


def is_even(input):
    if (len(input) % 2 == 0): return true
    else: return false

def count_letters(input):
    return len(input)

#This function takes in an inut string and returns the number of consonants contained within it.
def count_consonants(input):
    consonants = "bcdfghjklmnpqrstvwxz"
    count = 0
    input = input.lower()
    for i in string:
        if i in consonants:
            count +=1

    return count

#This function takes in an inut string and returns the number of vowels contained within it.
def count_vowels(input):
    vowels = "aeiouy"
    count = 0
    input = input.lower()
    for i in input:
        if i in vowels:
            count +=1

    return count



    # For every customer iterate through every available product by the
    # following method:
    # 1. The first customer should check each available product and register each
    # score.  Repeat this process for all customers.
    # 2. Once all scores have been registered, the lowest
   #automatically check and select the he first
    # available product.  Then check all other available products for a higher
    # score.customer will check every available product by first checking and selecting the first avail  select the highest score
