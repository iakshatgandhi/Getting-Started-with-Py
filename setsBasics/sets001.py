my_set1 = {1, 2, 3, 4, 5, 6, 7, 'orange', 'banana'}
my_set2 = {'apple', 'banana', 'orange', 'kiwi', 'mango'}

intersect = my_set1 & my_set2
print(intersect)

union = my_set1 | my_set2
print(union)

diff = my_set2 - my_set1
print(diff)

a = {5, 7, 8, 9}
b = {7, 9}

superset01 = a>b
superset02 = b>a

print(superset01,superset02)

print(list(my_set1))