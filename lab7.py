class Vector3f:
    def  __init__(self, x=0, y=0, z=0):
        self._x=x
        self._y=y
        self._z=z
    def setx(self,X):
        self._x=X
    def  sety(self,Y):
        self._y=Y
    def   setz(self,Z):
        self._z=Z
     
    def getx(self):
        return self._x
    def  gety(self):
        return self._y
    def   getz(self):
        return self._z
    
    def __add__(self,anothervector):
        X1=self._x + anothervector._x
        Y1=self._y +  anothervector._y
        Z1=self._z + anothervector._z
        return Vector3f(X1,Y1,Z1)
    
    def __mul__(self,operand):
       if isinstance(operand,(int,float)):
        return Vector3f(self._x*operand,self._y*operand,self._z*operand)
       elif  isinstance(operand,Vector3f):
           return Vector3f(self._x*operand._x, self._y*operand._y, self._z*operand._z)
    
    def dotproduct(self, other):
        return self._x * other.getx() + self._y * other.gety() + self._z * other.getz()

    
    def length(self):
        return  (self._x**2 + self._y**2 + self._z**2)**0.5
    
    def  normalize(self):
        vectoradd=vector1 + vector2
        print(vectoradd)
        length1=vectoradd.length()
        return (vectoradd._x/length1,vectoradd._y/length1,vectoradd._z/length1)
    def __str__(self):
        return f"({self._x},{self._y},{self._z})"
        

    
        
###main

vector1=Vector3f(3,1,2)
vector2=Vector3f(4,5,6)

addition=vector1 +  vector2
print(f'addition of two vectors:{addition}')

scalarproduct=vector1 * 4
print(f'multiplication of vector with scalar: {scalarproduct}')

length11=vector1.length()
print(f'length of vector: {length11}')

vectorproduct=vector1*vector2
print(f'multiplication of two vectors: {vectorproduct}')\

print(f'normalized vector: {vector1.normalize()}')



