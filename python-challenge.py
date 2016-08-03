

#1. If the number of letters in the product's name is even then the SS is the number of vowels (a, e, i, o, u, y) in the customer's name multiplied by 1.5.
#2. If the number of letters in the product's name is odd then the SS is the number of consonants in the customer's name.
#3. If the number of letters in the product's name shares any common factors (besides 1) with the number of letters in the customer's name then the SS is multiplied by 1.5.

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line


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

    if hcf(len(x),len(y)) > 1: score = score * 1.5
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

print "pre test"
#set path to find the discount list.  Set Path to:
# /Shared/Projects/python-challenge/customer_products.txt
 #   from collections import deque
print "start test"
from collections import deque
from functools import reduce
import re
from itertools import product
from string import whitespace
# open the file and put in a while loop
path = "customer_products.txt"

file = open(path, 'r')
counter = 0;
text = file.readlines()

first_set, second_set, third_set = text[0],text[1],text[2]

print first_set
print second_set
print third_set
def get_sscore(campaign):
    #for campaign in campaigns
    print "getting score of " + str(vcv(campaign[0],campaign[1])) + " for [" + campaign[0] + " , " + campaign[1]# campaign
    return vcv(campaign[0],campaign[1])

def my_product(dicts):
    return (dict(izip(dicts, x)) for x in product(*dicts.itervalues()))


def get_sscorex(customer, products):
    #for campaign in campaigns
    scores = []
    print "GENERATING scores for " + customer
    pools = map(tuple, args) * kwds.get('repeat', 1)
    ss_capaigns = map(get_sscore, campaigns)
    result = [[]]
    for product in products:
        result = [x+[y] for x in result for y in product]
    for prod in result:
        yield tuple(prod)

        scores.append(vcv(customer,product))
        print "getting score of " + str(vcv(customer,product)) + " for " + product
    yield scores
    return


def optimize(n):
	results = []
	n = n.strip("\n")
	n = re.sub("[\s+]", "", n)
	customers = n.split(";")[0].split(",")
	products = n.split(";")[1].split(",")

    # Uses the list composition to make the key value pairs over a dictionary.

        #campaignx = map(get_sscorex, products)
    #print campaignx
	return [customers, products]

first_set = optimize(first_set)
print first_set
second_set = optimize(second_set)
print second_set
third_set = optimize(third_set)
print third_set

#counter += counter
#customer_values = dict((a, len(a)) for a in customers)

#print customer_values.values()
#set_ss(customers, products)

#text = file.readlines()

file = open(path, 'r')
counter = 0;

for line in file.readlines():
    items = line.split(";")
    customers = items[0].translate(None, whitespace).split(",")
    products = items[1].translate(None, whitespace).split(",")
    campaign_options = lambda dic: [(k, v) for k,v in product(customers, products)]
    campaigns = product(customers, products)
    print campaign_options

    ss_capaigns = map(get_sscore, campaigns)







import re
path = "customer_products.txt"
file = open(path, 'r')
text = file.readlines()



#    def map_set(n)


print "-----"


#    def testScore
