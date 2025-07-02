### What is oops?

# programming through objects
## class syntax

#class classname
     #attri
     #methods
     #class body
class person_details():
    user_name="ajay"
    employee_id=1234
    height=5.7
    def details(remo,):
        print("this is class method 1")
        print(remo.user_name)
    def details_2(remo,):
        print("this class is method 2") 
obj=person_details()
obj.details()
print(obj.user_name)
print(obj.employee_id)
obj.details()
print(obj.height)