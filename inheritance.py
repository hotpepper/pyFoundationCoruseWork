class Parent():
    def __init__(self, last_name, eye_color):
        print "Parent constructor called"
        self.last_name = last_name#'hotpepper'
        self.eye_color = eye_color#'green'
        
    def show_info(self):
        print "Last Name: %s" % self.last_name
        print "Eye color: %s" % self.eye_color
    
                  

class Child(Parent):
    '''inherents from parent'''
    def __init__(self, last_name, eye_color, number_of_toys):
        print "Child constructor called"
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        '''method overriding'''
        print "Last Name: %s" % self.last_name
        print "Eye color: %s" % self.eye_color
        print "Number of Toys: %i" % self.number_of_toys
        
        

        

billy_cyrus = Parent("Cyrus", "blue")
billy_cyrus.show_info()
print '\n'
miley_cyrus = Child("Cyrus", "blue", 5)
miley_cyrus.show_info()
##print miley_cyrus.last_name
##print miley_cyrus.number_of_toys
