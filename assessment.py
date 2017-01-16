"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

2. What is a class?

3. What is an instance attribute?

4. What is a method?

5. What is an instance in object orientation?

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

Answers:

1. 	Encapsulation: is including data and all its functionality in one unit called class

	Abstraction: is hiding all mechanics from user and exposing only the relevant data
	
	Polymorphism: is being able to use methods and variables with different types of data

2. Class: is a template for creating objects. It includes data and functionality of objects in one unit.

3. instance attribute: is an attribute (data or method) defined in the object (or instance) itself 
or __init__ method in class. It's relevant only to that particular object and not the other objects
instantiated using the class template.

4. method: is a function defined within a class

5. instance: is an object created using the template class.

6. How is a class attribute different than an instance attribute?: Instance attributes 
are relevant only for each instance. Class attributes are common to all instances of the class. 
If you change a class attribute, that attribute in all instances made from that class will be changed.
If you change an intance attribute, that attribute will changed only in that instance. 

example: see below. 
The rectangle class has 'name' which is a class attribute.
it has instance attributes that is relevant only to each instance made.


"""


# Parts 2 through 5:
# Create your classes and class methods

class AbstractShape(object):
	""" place hollders for a shape class atrributes"""

	def __init__(self):
	  pass

	def Area(self):
	  pass


class Rectangle(AbstractShape):
	"""rectangle class"""
	name = 'rectangle'	# class atrribute, all objects will have a name object.

 	def __init__(self, length=0, height=0):
 		try:
	  		self.length = int(length)
	 		self.height = int(height)
	 	except ValueError as err:
	 		raise err

		
 	def area(self):		
 		area = int(self.length) * int(self.height)
 		return area

#main
rect = Rectangle(5,6)

print rect.area()