# a = {1,2,3,4,5}
# b = {2,4,6,8,10}
# c = a - b
# print(c)
# c = a.union(b)
# c = a.update(b)
# c = a.intersection(b)
# c = a.intersection_update(b)
# a.remove(4)
# a.discard(7)
# a.clear()
# print(a)
# print(b)
# print(c)

# a,b = 12,3
# if a + b:
#     print('True')
# else:
#     print('False')

# for num in range(2,-5,-1):
#    print(num, end=" ")



# a = {1,2,3,4,5}
# b = {2,4,6,8,10}
# c = b - a
# print(c)

eng_input = input("The no of english candidate \n >::")
eng_list = input("Space seperated list \n >::").split()
new_list = set(eng_list)
fre_input = input("The no of french candidate \n >::")
fre_list = input("Space seperated list \n >::").split()
new1_list = set(fre_list)
final = new_list.symmetric_difference(new1_list)
final1 = len(final)
print(f"the final set is {final}")
print(f"the final answer is {final1}")