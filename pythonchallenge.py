
<<<<<<< HEAD:python-challenge.py
from challenge2 import *

class Customers:
  def __init__(self, name):
      self.name = name
      self.id = name
  def __repr__(self): return repr(self.id)


class Products(object):
  def __init__(self, name, merchant):
      name = name
      discount = discount
      merchant = merchant
      id = name + "_" + merchant
  def __repr__(self): return repr(self.id)


class Merchants:
  def __init__(self, name):
      name = name
      id = name
      product_discounts = [Products]
  ## TO DO - provide function to get/set daily discount product list
  def __repr__(self): return repr(self.id)

#the dealer determines all the deals and assignments of products to customers
class Dealer:
  def __init__(self, name):
      name = name
      id = name
  def __repr__(self): return repr(self.id)

#offers are combinations of products and customers and have a ss determined on construction
class Offers(object):
  def __init__(self, customer, product):
      self.name = [customer, product]
      self.id = product(customers, products)
      self.customer = customer
      self.product = product
      self.dealer = dealer
      self.score = dealer.get_score(id)
  def __repr__(self): return repr(self.id)

class Deals(object):
  def __init__(self, customer, product):
      self.name = [customer, product]
      self.id = product(customers, products)
      self.customer = customer
      self.product = product
      self.dealer = dealer
      self.score = dealer.get_score(id)
  def __repr__(self): return repr(self.id)

class Marketer:
  def __init__(self, name):
    self.name = name
    self.customers = [Customers]
    self.products = [Products]
    self.all_offers = [Offers]
    self.optimum_offers = [Offers]
  def __repr__(self): return repr(self.name)
 # def set_product(self, product)



#all_offers = {x: dealer.get_score for x in product_map}
#class customer(object):
#    def __init__(self, name, product, score):
#        self.name = name
#        self.profession = profession
#        self.campaign_list = dict(product, campaign)

class Markets:
    def __init__(self):
        name = 'one little market'
        id = name
        merchants = list(Merchants())
        products =  list(Products())
        customers = list(Customers())

        deal_match = self.dealer.get_best_match()
    def __repr__(self): return repr(self.id)




=======
>>>>>>> 6492d047977f3c4d9c216ff6e208cc2478cd177c:pythonchallenge.py
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



<<<<<<< HEAD:python-challenge.py


def optimize(n):
	results = []
	n = n.strip("\n")
	n = re.sub("[\s+]", "", n)
	customers = n.split(";")[0].split(",")
	products = n.split(";")[1].split(",")
=======
>>>>>>> 6492d047977f3c4d9c216ff6e208cc2478cd177c:pythonchallenge.py

def get_optimum_score(n):
  score = 0
  results = []
  n = n.strip("\n")
  n = re.sub("[\s+]", "", n)
  customers = n.split(";")[0].split(",")
  products = n.split(";")[1].split(",")
  campaign_options = lambda dic: [(k, v) for k,v in product(customers, products)]
    # Uses the list composition to make the key value pairs over a dictionary.
    #campaignx = map(get_sscorex, products)


    #print campaignx

  return score

first_set = get_optimum_score(first_set)
print first_set
second_set = get_optimum_score(second_set)
print second_set
third_set = get_optimum_score(third_set)
print third_set

for line in text:

    get_optimum_score(line)
#counter += counter
#customer_values = dict((a, len(a)) for a in customers)

#print customer_values.values()
#set_ss(customers, products)

#text = file.readlines()

file = open(path, 'r')
counter = 0;
customers = []
products = []
deals = {}
for line in file.readlines():
    items = line.split(";")
    customer = Customers(items[0].translate(None, whitespace).split(","))
    customers.append(customer)
    products = items[1].translate(None, whitespace).split(",")
<<<<<<< HEAD:python-challenge.py
=======
    campaign_options = lambda dic: [(k, v) for k,v in product(customers, products)]

    campaigns = product(customers, products)
    print campaign_options
>>>>>>> 6492d047977f3c4d9c216ff6e208cc2478cd177c:pythonchallenge.py

    deals = dict(product(customers, products))

    print deals
    deals = product(customers, products)
    deals2 = dict(product(customers, products))
    offers = map(get_sscore, deals2.iteritems())
    print offers




import re
path = "customer_products.txt"
file = open(path, 'r')
text = file.readlines()



#    def map_set(n)


print "-----"


#    def testScore
