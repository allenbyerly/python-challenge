from collections import deque
from functools import reduce
import re
from itertools import product
from string import whitespace

class Customers:
  def __init__(self, name):
      self.name = name
      self.is_even = (len(name))
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
class Dealers:
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

class Campaigns(object):
  def __init__(self, customer, product):
      self.customer = customer
      self.product = product
      self.name = [customer, product]
      #Suitability Score
      self.ss = 0

  def __repr__(self): return repr((self.name, self.product, self.score))
  def high_score(self): return self.high_score
  def high_product(self): return self.high_product
  def __repr__(self): return repr([self.name, self.score])



#>>> student_objects = [
#        Student('john', 'A', 15),
#        Student('jane', 'B', 12),
#        Student('dave', 'B', 10),
#]
#>>> sorted(student_objects, key=lambda student: student.age)   # sort by age
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
