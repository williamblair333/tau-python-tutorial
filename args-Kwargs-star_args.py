#################################################################################
'''
argument, keywords:
https://testautomationu.applitools.com/python-tutorial/chapter3.html
https://realpython.com/python-kwargs-and-args/
Error Handling:
https://docs.python.org/3/tutorial/errors.html
https://stackoverflow.com/questions/45526000/exception-handling-python-typeerror-nonetype-object-is-not-callable
args* & kwargs**
    https://www.geeksforgeeks.org/args-kwargs-python/
    https://www.programiz.com/python-programming/args-and-kwargs

'''

#Positional Arguments Example
#def user_info(name, age, city):

#Keyword Argument Example
def user_info(name="No Name", age="0", city="No City"):
    print("{} is {} years old, from {}.".format(name, age, city))

try:
    user_info("Janet", 58, "Oklahoma City")
    user_info(34, "New York")
    user_info()
except TypeError:
        print("Missing arguments")
        pass

def application(fname, lname, company, email, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname,
company, email))

application("Jess", "Ingrass", "TeachCode.org", "mail@mail.com", 75000, \
hire_date="2010SEP")
#################################################################################