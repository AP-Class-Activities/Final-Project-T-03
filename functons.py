# from Products import Product
# from random import randint
# from users import Customer, 

import pickle

with open('ID_file.txt', 'w') as file:
     pickle.dump(file)


# with open('ID_file.txt', 'r') as file:
#     ID_list = pickle.load(file)



# def ID_creater(value):
#     if type(value) is Product:
#         x = randint(100000,999999)
#         while 'PR' + str(x) in []:   # ID_list should be made by ID_file :(
#             x = randint(100000,999999)
#         return 'PR' + str(x) 
#     elif type(value) is Seller:
#         x = randint(100000,999999)
#         while 'SL' + str(x) in []:   # ID_list should be made by ID_file :(
#             x = randint(100000,999999)
#         return 'SL' + str(x)
#     elif type(value) is Customer:
#         x = randint(100000,999999)
#         while 'CU' + str(x) in []:   # ID_list should be made by ID_file :(
#             x = randint(100000,999999)
#         return 'CU' + str(x)   

    



# def buy_history(customer):  # buy_history = [sale1,sale2,...]
#     l = []
#     for i in sale_list:   # sale_list should be created by the sale_file 
#         if i.customer == customer:
#             l.append(i)
#     l.sort()
#     return l

# def sale_history(seller):
#     l = []
#     for i in sale_list:   # sale_list should be created by the sale_file 
#         if i.seller == seller:
#             l.append(i)
#     l.sort()
#     return l

# def stock_check(seller,product):
#     for i in selller.product_stock:
#         if i[0] == product:
#             return i[1]
#     return 0

# def buy(customer):    # shopping_bag = [[product1, seller1, number1],...]    product_stock = [[product1, stock1],[product2, stock2],...]
#     for i in customer.shopping_bag:
#         if stock_check(i[1],i[0]) < i[2]:
#             return 'There is not enough{}'\
#                 .format(i[0].name)
#     total_price = 0
#     for i in customer.shopping_bag:
#         total_price += i[0].new_price() * i[2]
#     if customer.electronic_wallet > total_price or customer.electronic_wallet == total_price:
#         customer.electronic_wallet((-1)*total_price)
#         for i in customer.shopping_bag:
#             for j in range(0,i[2]):
#                 s = Sale(i[0],i[1],customer)
#                 sale_list.append(s)  # using file :(
#                 i[1].electonic_wallet(i[0].new_price())
#                 i[1].add_product([i[0],-1])     
#     else: 
#         print('You do not have enough money.')
#     return

# def comment(customer,product,value):
#     if product in buy_history(customer):
#         product.comment_list(customer.first_name + ' ' + customer.last_name + ': ' + value)
#         return
#     else:
#         raise ValueError('You can only comment for the products you have bought before!')

# def rate(customer,product,value):
#     if product in buy_history(customer):
#         product.score(value)
#         for i in buy_history(customer):   # buy_history = [sale1,sale2,...]
#             if i.product == product:
#                 i.seller.score(value)
#         return
#     else:
#         raise ValueError('You can only rate the products you have bought before!')