#################################################################################

fruits = ["peaches", "pears", "apples"]
years = [3, "1998", 2.5, 987, "1994"]
print("#########")
'''
print(fruits,years)
print("#########")
for fruit in fruits:
    print(fruit)
print("#########")
'''
fruits.append("orange")
for fruit in fruits:
    print(fruit)
print("#########")
'''
#add one list to another list
fruits.extend(years)
for fruit in fruits:
    print(fruit)
print("#########")
#remove list item by name
fruits.remove("oranges")
for fruit in fruits:
    print(fruit)

print("#########")

#remove list item by index number
fruits.pop(0)
print("#########")

#remove list item by counting from the end backward
#remove the last item
'''
fruits.pop(-1)
for fruit in fruits:
    print(fruit)

print("#########")
#################################################################################
#list.sort is only used with items of the same type (except int and float dbl..

numbers = [5,1,3,4.75,99]
numbers.sort()
print(numbers)
print("#########")

#check membership
print("apple" in fruits)
if "apple" in fruits is True:
    print("apples")
else:
    print("no apples")