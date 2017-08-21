class Customer:
  def __init__(self, name): self.name = name
  def __repr__(self): return repr(self.name)



  def high_score(self): return self.high_score
  def high_product(self): return self.high_product
 # def set_product(self, product)

#class customer(object):
#    def __init__(self, name, product, score):
#        self.name = name
#        self.profession = profession
#        self.campaign_list = dict(product, campaign)

class product(object):
  def __init__(self, name): self.name = name
  def __repr__(self): return repr(self.name)

class campaign(object):
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

#student_objects = [
#Student('john', 'A', 15),
#Student('jane', 'B', 12),
#Student('dave', 'B', 10),
#]
#sorted(student_objects, key=lambda student: student.age)

#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
