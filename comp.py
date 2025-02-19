# list=[1,2,3,4,5,6,7,8,9]
# sr_num1=[]
# for i in list:

#     sr_num1.append(i**2)
# print(sr_num1)
# print('x'*20)

# # similar process done list comprehensive 

# sr_num2=[i**2 for i in [1,2,3,4,5,6,7,]]
# print(sr_num2)


# name=[]
# for letter in 'raksha':
#     name.append(letter)
# print(name)
# print('x'*20)

  
# similar task done with list comprehensive


# name=[letter for letter in 'raksha']
# print(name)

# # -----------------------------------------------

# apply if condition in list comprihensive 



# even=[]
# for i in range(10):
#     if i%2==0:
#         even.append(i)
# print(even)
# print('x'*20)

# # similar task done with list comprehensive 
# even=[i for i in range(10) if i%2==0 ]
# print(even)

# nested loop using list comprehensive
# first using normal 
# my_list=[]
# for x in [2,4,6]:
#     for y in [1,2,3,]:
#         my_list.append(x*y)
# print(my_list)
# print('x'*20)

# # now using list comprehensive for this also using nested if
# my_list=[x*y for x in [2,4,6]  for y in [1,2,3,] if x*y != 6 if x*y !=12 ]
# print(my_list)

# now using else with listy comprehensive

# list_=[['a','b','c',],['d','e','f'],['g','h','i']]
# my_list=[]
# for letter in list_:
#     if 'g' not in letter:
#         my_list.append(letter)
#     else:
#         my_list.append('letter was skipped')
# print(my_list)

# # using list comprehensive for this task
# my_lists=[letter if 'g' not in letter else  'letter was skipped' for letter in list_ ]
# print(my_lists)