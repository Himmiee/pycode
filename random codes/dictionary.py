# a = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }


# print(a['a'])

my_arr = [0,3,2,3,4,6,7,8,3,2,1,0,3,2,1,5,6,7,8,9,4,5,6,1,3,4,5,6,0,9,9,8,5,4,9,1,2,8]
freq = {}

for ele in my_arr:
    freq[str(ele)] = freq.get(str(ele),0) + 1
    
print(freq)

# a = {}
# for ele in set(my_arr):
#     a[ele] = my_arr.count(ele)
# print(a)   

# a = {
#     'k1':'v1',
#     'k2':'v2',
#     'k3':'v3'
# }

# # for i in a:
# #     print(i)

# b = {
#     'ka':'va',
#     'kb':'vb',
# }

# c = a.update(b)
# print(a)


# data = {
#     'name':'wale',
#     'city': 'silicon valley',
#     'salary' : '$20 000',
#     'id': '456789'
# }



# data['employee id'] = data.pop('city')
# print(data)




