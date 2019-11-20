class Dog:
  kingdom = 'Animals'

  def __init__(self, name, age, breed):
      self.name = name
      self.age = age
      self.breed = breed

  def bark(self, sound='uf'):
      print(sound * self.age)

dyzio = Dog('Dyzio', 3, 'mops')
dyzio.bark()
dyzio.bark('hauu')
hyzio = Dog('Hyzio', 3, 'pies')
hyzio.bark()
