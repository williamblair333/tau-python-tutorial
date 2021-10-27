#################################################################################
'''
https://testautomationu.applitools.com/python-tutorial/chapter7.html

dictionary value by index
https://stackoverflow.com/questions/15114843/accessing-dictionary-value-by-index-in-python

access a dictionary key by index
https://www.kite.com/python/answers/how-to-access-a-dictionary-key-by-index-in-python
'''

stats = {
    "strength":11,
    "dexterity":12,
    "constitution":13,
    "intelligence":14,
    "wisdom":15,
    "charisma":16,
    "comeliness":19,
}

saves = {
    "fort":2,
    "reflex":2,
    "will":2,
}
'''
#removes the last key/value in dict
print(stats.popitem())

print(stats.setdefault("Saves", 0))

#get the value from the key value
print(stats.get("strength"))

#return keys + values which is a list of tuples
print(stats.items())

#return keys only
print(stats.keys())

#return values only
print(stats.values())
'''
#add one dict to another dict
stats.update(saves)

#update existing value or add new items
stats.update(will = 3)

dict_length = len(stats)

#key                             | value
print(tuple(stats.items())[0][0], tuple(stats.items())[0][1], sep="|", end="")

print("\n")
count = len(stats)
k, v = 0, 0

while k < count:
    print(tuple(stats.items())[k][0], tuple(stats.items())[k][1], sep=" | ", end="")
    print("\n")
    k += 1