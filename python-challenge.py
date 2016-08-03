
# collect and count customers and store the variables as collections where the count of each charecters name is stored
# as a pair...
def set_ss(customers, products):
    ss = {}
    multiplier = 1
    for product in products:
        for customer in customers:


            x = count_letters(product.strip())
            y = count_letters(customer.strip())
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
                ss[customer, product] = 1.5 * count_vowels(customer) * multiplier
            else:
                ss[customer, product] = 1 * count_consonants(customer) * multiplier

    print ss.values()

#def get_score(counter):



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

def rule_one(x, y):

    if (len(y) % 2 == 0): return True
    else: return False

def is_even(value):
    if (len(value) % 2 == 0): return True
    else: return False

def count_letters(value):
    return len(value)



#This function takes in an inut string and returns the number of consonants contained within it.
def vcv(x, y):
    if (len(y) % 2 == 0):
        vowels = "aeiouy"
        count = 0
        x = x.lower()
        for i in x:
            if i in vowels:
                count +=1
        score = count * 1.5

    else:
        consonants = "bcdfghjklmnpqrstvwxz"
        count = 0
        x = x.lower()
        for i in x:
            if i in consonants:
                count +=1

        score = count

    if hcf(x,y) > 1: score = score * 1.5

    return score

#This function takes in an inut string and returns the number of vowels contained within it.
def count_vowels(value):


    return count




    # For every customer iterate through every available product by the
    # following method:
    # 1. The first customer should check each available product and register each
    # score.  Repeat this process for all customers.
    # 2. Once all scores have been registered, the lowest
   #automatically check and select the he first
    # available product.  Then check all other available products for a higher
    # score.customer will check every available product by first checking and selecting the first avail  select the highest score



path = "customer_products.txt"

#set path to find the discount list.  Set Path to:
# /Shared/Projects/python-challenge/customer_products.txt
def product_assignments(path):
 #   from collections import deque
 from collections import deque
 from functools import reduce
# open the file and put in a while loop
file = open(path, 'r')
counter = 0;
text = file.readlines()

counter += counter


while (len(text) > 0):
# Split each line by the semicolon to sepaate out products from customers
    print text
    split = text[0].split(";")

# Split all collected customers]9
    customers = split[0].split(",")
    print customers

    products = split[1].split(",")
    print products

    customer_values = dict((a, len(a)) for a in customers)

    print customer_values.values()
    set_ss(customers, products)
    text = file.readline()

 # Check if e3. If the number of letters in the product's name share s any commo factors (besides 1) with
 # the
 # number of letters in
 # the customer's name then the SS is multiplied by 1.5.

#1. If the number of letters in the product's name is even then the SS is the number of vowels (a, e, i, o, u, y2) in the customer's name multiplied by 1.5.
