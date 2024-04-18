# Import your custom module but use a alias by putting as at the end of the import and end it with a new alias
import my_module as my

# Using the function from my_module
result = my.greet("Alice")
print(result)

# Acessing the variable
print(my.my_variable)

# Creating an instance of the MyClass
MyClass = my.MyClass("42")
MyClass.display()
