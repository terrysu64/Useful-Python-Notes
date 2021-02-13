#Author: Terry Su
#Purpose: some useful notes and tips

#THE ALL() & ANY FUNCTION

#The all() function returns True if all items in an iterable are true, otherwise it returns False.
#If the iterable object is empty, the all() function also returns True.

#Note: When used on a dictionary, the all() function checks if all the keys are true, not the values.

x = [1,2,0]
print(all(x))

#conditions can also be used where
#all(condition(item) for item in iterable)

print(all(element < 5 for element in x))

#The any() function returns True if at least one item in an iterable are true, otherwise it returns False.

print(any(x))
print(any(element == 0 for element in x))

#THE ZIP() FUNCTION

#The zip() function returns a zip object, which is an iterator of tuples where the items of each iterator passed for respective indexes are paired together
#assuming all iterators have a value at that index

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
c = [1,2,3]

x = zip(a, b, c)
print(tuple(x)) #use the tuple() function to display a readable version of the result:
