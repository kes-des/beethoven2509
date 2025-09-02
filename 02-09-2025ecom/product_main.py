from product_manager import create_product, read_all, read_by_id
from product_manager import update, delete_by_id
from product import Product





def menu():
    message = '''




The menu choices are
1 - Create Product
2 - Read All Products
3 - Read By id
4 - Update 
5 - Delete 
6 - Exit/ Logout 
Your choice:'''
    choice = int(input(message))
    if choice == 1:
        name = input('Name:')
        description = input('Description:')
        category = input('category:')
        tags = input('tags')
        stock = int(input('stock:'))
        price = int(input('price:'))
        id = -1




        product = Product(id,name, description, category, tags, stock, price)




        create_product(product)
        print('Product created successfully.')



    elif choice == 2:
        products = read_all()
        print('products:')
        for product in products:
            print(product)



    elif choice == 3:
        id = int(input('ID'))
        product = read_by_id(id)
        if product == None:
            print('product not found')
        else:
            print(product)



    elif choice == 4:
        id = int(input('ID'))
        old_product = read_by_id(id)
        if old_product == None:
            print('Product not found')
        else:
            print(old_product)
        name = input('Name:')
        description = input('Description:')
        category = input('category:')
        tags = input('tags')
        stock = int(input('stock:'))
        price = int(input('price:'))
        new_product = Product(id,name, description, category, tags, stock, price)
        update(new_product)
        print('product updated successfully')





    elif choice == 5:
        id = int(input('ID'))
        old_product = read_by_id(id)
        if old_product == None:
            print('Product not found')
        else:
            print(old_product)
            if input('are you sure to delete(y/n?') == 'y':
                delete_by_id(id)
                print('product deleted successfuly') 
    return choice
def menus():
    print('Product Management App')
    choice = menu()
    while choice != 6:
        choice = menu ()
    print('Thank You for using app')
menus()