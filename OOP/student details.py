class csstudent:
    #class variable
    stream = "cse"

    #the init method or constructor
    def __init__(self, roll):

        #instance variable
        self.roll = roll

    def setaddress(self, address):
        self.address = address
        
    # retrieves instance variable
    def getaddress(self):
        return self.address
    
# driver code
add = csstudent(101)
add.setaddress("123 Main St")
print(add.getaddress())

# object of csstudent class
a = csstudent(101)
b = csstudent(102)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.roll)   # prints 101

print(csstudent.stream) # prints "cse"