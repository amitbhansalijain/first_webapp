# class map():
#     material="house"
#     print(f'i build a {material}')

# house1=map()
# house2=map()
# house3=map()

# house1.material='new house'
# house1.material2='very good house'
# print(house1.material2)
# # house2.material='big house'
# print(house2.material)
# house3.material='luxury house'
# print(house3.material)

# -------------------------------------------


# class map():
#     material="house"
#     print(f'i build a {material}')
#     def adder(self):
#         x=2+2
#         return x
# house=map()
# house.material='a sweeet home'
# house.adder=3+4+5
# print(house.material)
# print(house.adder)


# -----------------------------------------------
# surrary of class
# 1) class : template for creating object
# all object created from same class will have Attribute
# 2) object : is intance of a class
# 3) intentiate : process of creating isinstance
# 4) method : a function defined in class
# 5) attribute :A variable bound to an instance of a class

# class employes():
#     def putdata(self):
#         self.id=int(input('plz enter your employee id:'))
#         self.name=input('plz enter your name:')
#         self.salary=float(input('plz enter your salary:'))
#     def function(self):
#         print('employee id:',self.id)
#         print('employee name:',self.name)
#         print('employee salary',self.salary)
    
# a=employes()
# a.putdata()
# a.function()

# class watch():
#     def putdata(self):
#         self.colou=input('plz enter colour of watch:')
#         self.price=int(input('plz enter a price of watch:'))
#     def fuction(self):
#         print('clour of watch is :',self.colou)
#         print('price of watch is :',self.price)
# a=watch()
# a.putdata()
# a.fuction()


# class map():
#     def __init__(self,material):
#         self.material=material
        
#         print(f'i build a {material}')
# house1=map('new house')
# house2=map('very big')
# house3=map('i love this')
# house4=map('sweet home')
# ----------------------------------------------------------------------



# class kattle():
#     # universal Attribute
#     power_src='solar'

#     def __init__(self,make,price):
#         self.make=make
#         self.price=price
#         self.on=False
#     def switch(self):
# #         self.on=True
# kenwood=kattle('kenwood',10)
# hamilton=kattle('hamilton',10)
# print(kenwood.price)
# print(kenwood.make)
# print(kenwood.on)
# kenwood.switch()
# print(kenwood.on)
    
# print(kenwood.power_src)
# print(hamilton.make)
# print(hamilton.price)
# print(hamilton.on)
# hamilton.switch()
# print(hamilton.on)
# print(hamilton.power_src)
# kenwood.power_src='ac'
# print(kenwood.power_src)
# hamilton.power_src='dc'
# print(hamilton.power_src)
# kenwood.model=2019
# print(kenwood.model)
# kattle.power_src='solar'
# print(kenwood.__dict__)
# print(kattle.__dict__)
# print(hamilton.__dict__)


# -------------------------------------------------------------------------------

# import datetime
# class bank():
#     @staticmethod
#     def current_time(self):
#         time=datetime.datetime.now()
#         return time
#     def __init__(self,_name,balance):
#         self._name=_name
#         self.__balance= balance
#         print(f'account created for {_name}')
#         self.trans_list=[(bank.current_time(self),balance)]
#         self.show()
#     def deposite(self,amount):
#         if amount>0:
#             self.__balance += amount
#             self.show()
#             self.trans_list.append((bank.current_time(self),amount))
#     def withdraw(self,amount):
#         if amount>0 and self.__balance >= amount:
#             self.__balance -= amount
#             self.show()
#             self.trans_list.append((bank.current_time(self),-amount))
#         else:
#             print(f'insufiicient balance')
#     def show(self):
#         print(f'{self._name} balance is {self.__balance}')
    
#     def show_trans(self):
#         for date,amount in self.trans_list:
#             if amount>0:
#                 trans_type='Deposite'
#             else:
#                 trans_type='Withdraw'
#                 amount *= -1
#             print(f'amount {amount} dollar,{trans_type} on {date}')
# # piyush=bank('piyush',20)
# # piyush.deposite(50)
# # piyush.show_trans()
# # print('x'*20)
# # amit=bank('amit',200)
# # amit.deposite(300)
# # amit.show()
# # amit.withdraw(450)
# # amit.show()
# raksha=bank('raksha',100)
# raksha.__balance=500
# raksha.deposite(100)
# raksha.show_trans()

# print(raksha.__dict__)



# ----------------------------------------x--------------------------------------x-----------------------------------------------------------


        