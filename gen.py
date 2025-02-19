# import sys
# def my_gen(n:int):    
#     start = 0
#     while start < n:
#        print(f'my range is returning: {start}')
#        yield start
#        start += 1

        
# gen_list=my_gen(10)
# print(next(gen_list))
# print(next(gen_list))
# print(next(gen_list))
# print(f'this gen_list takes {sys.getsizeof(gen_list)} bytes ')
# print('x'*20)
# itr_list=[]
# for var in gen_list:
#     itr_list.append(var)
# print(f'this is normal list takes {sys.getsizeof(itr_list)} bytes ')



