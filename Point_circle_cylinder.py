import math
class Point:
	def __init__(self,x,y):
		 self.x=x
		 self.y=y
	def str (self):
		return ("%d %d"%(self.x , self.y))
		 
     
		

print("--------------------------------------------")

p=Point(3,4)

print ("X coordinate is %d"%(p.x))
print ("Y coordinate is %d"% (p.y))
print("--------------------------------------------")


p.x = 10
p.y = 10

print ("X coordinate is %d"%(p.x))
print ("Y coordinate is %d"% (p.y))
print("--------------------------------------------")

class Circle( Point ):
	def __init__(self,x,y,radius):
		super().__init__(x,y)
		self.radius=radius
	def area(self):
		return math.pi * self.radius ** 2
	def str (self):	
    
		return ("%d %d %f"%(self.x , self.y,self.radius))

print("--------------------------------------------")
c=Circle(1,2,4.8)

print ("X coordinate is %d"% (c.x))
print ("Y coordinate is %d"% (c.y))
print ("Radius is  %.2f"%(c.radius))

print("The area of circle is: %.2f"%(c.area()))
print("--------------------------------------------")
class Cylinder( Circle ):
	 def __init__(self,x,y,radius,height):
		 super().__init__(x,y,radius)
		 self.height=height
	 def str (self):	
          return ("%d %d %f %f"%(self.x , self.y,self.radius,self.height)) 	 
	 def area (self):	
           return 2 * Circle.area( self ) + 2 * math.pi * self.radius * self.height  
     
     
		 	
	
print("--------------------------------------------")	
cyl=Cylinder(2, 2,4.250000,10.000000)	

print ("X coordinate is %d"%(cyl.x))
print ("Y coordinate is %d"% (cyl.y))
print ("Radius is %.2f"% (cyl.radius))
print ("Height is %.2f"% (cyl.height))

print("--------------------------------------------")

print ("CYLINDER AREA")
print ("The area of the given cylinder is %.3f"%(cyl.area()))
