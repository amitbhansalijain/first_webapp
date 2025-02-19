# local scope = local scope define to the scope of variable that are defined within the specific function
# def fun():
#      global x
#      x=3
#      print(x)
     
        
# fun()
# print(x)
# global scope
# x=2
# def fun ():
#     print(x)
# fun()
# print(x)
# cloths='dirty cloths'
# def washingmachine(cleancloths):
#     global cloths
#     cloths=cleancloths
#     print(cloths)
# print(cloths)
# washingmachine('clean cloths')
# print(cloths)
# nested function
# def fun1():
#     def fun2():
#         print(1)
#     fun2()
#     print(2)
# fun1()
# def washingmachine():
#     cloths='clean but wet'
#     def drycleaner():
#         nonlocal cloths
#         cloths='dry and clean'
#         print(cloths)
#     drycleaner()
#     print(cloths)
# washingmachine()




# #  calculate facturial
# def fact_fun(n):
#      result=1
#      for n in range(2,n+1):
#          result=result*n
#      return result
# for i in range(1,10):
#     print(i,fact_fun(i))

# print('x'*20)
# def recursivefun(n):
#      if n <= 1:
#           return 1
#      else:
#           a =n*recursivefun(n-1)
#           return a 
# for i in range(1,10):
#     print(i,recursivefun(i))


# febanucci seuence,recursive fuction
# def fib (n):
#     if n<2:
#         return n
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(10):

#     print(i,fib(i))

# import os
# list_os=os.walk('C:\\Users\\Owner\\OneDrive\\Desktop\\python')


# for root,direct,file in list_os:
#      print(root)
#      for i in direct:
#         print(i)
#      for j in file:
#             print(j)

# def fun_name(x,y):
#     print(x*y)
#     fun_name(x,y)

# fun_name(2,3)

# def table(num,i):
#     result=num*i
#     print(f'{i} multiply {num}={result}')
#     i += 1
#     while i !=  11:
#         table(num,i)
#         break
# table(2,1)
      
     
     




   
    
         
        






    
    
        
    
       