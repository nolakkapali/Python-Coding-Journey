# data_structure
product_catalog = {1234: {"name": "book", "price": 234},
                   1223: {"name": "dress", "price": 2354},
                   2324: {"name": "clock", "price": 3354}
                   }

# product id is key and quantity is value
shopping_cart = {1234: 11, 1223: 4, 4343: 56}


# gives the full detail info of product catalog
def view_product_catalog(catalog):
    print("\n=============Product Catalog=====================")
    count = 1

    for product_id, product_name_price in catalog.items():
        print(f"\nProduct{count} Information")
        print("\nProduct ID:", product_id)

        for product_name in product_name_price:
            print("Product", product_name, ":",
                  product_name_price[product_name])
        count = count+1


# add product to cart
# what does this function do:
# check first if the product is available in the product list
# if it available then it checks if it is already exist in the cart list
# A) if it exists, adds the current quantity to the list
# B) if it does not exists, then it is added to the shopping cart
# if the item not availble in the product list then this information is shown to the user
def add_to_cart(catalog, cart):
    product_id = int(input("Enter Product ID:"))
    Quantity = int(input("Enter Quantity:"))

    if product_id in catalog:
        print("product is available in product catalog", catalog.get(
            product_id, 0))  # to check if the product already exists

        if product_id in cart:  # this will check if product id is already in shopping cart
            # shopping_cart.update({productID:shopping_cartproduct_id]+Quantity})
            cart[product_id] += Quantity
            print("cart updated", cart[product_id])
        else:
            print("product is not avaliable in shopping cart!")
            cart.update({product_id: Quantity})
            print("cart updated", cart)
    else:
        print("Sorry! No Result!!!")

# view the cart


def view_shopping_cart(catalog, cart):
    print("\n===============Shopping Cart=================")
    sum = 0

    for product_id in cart:
        print("Product ID:", product_id,
              "\nProduct Quantity:", cart[product_id])

        if product_id in catalog:
            product_info = catalog[product_id]
            print("Product Name:", product_info["name"])
            print("Unit Price:", product_info["price"])
            total = product_info["price"] * cart[product_id]
            print(f'Total Price of {product_info["name"]}:{total}\n')
            sum = sum+total
        else:
            print(f'{product_id} ID not available to Product Catalog!')

    print("Final Total Price of All the Added Product:", sum)


# update the quantity of the product
# changes total price and indivisual summation of price when quantity changes
def update_quantity(catalog, cart):
    view_shopping_cart(catalog, cart)
    product_id = int(
        input("\nwhich product ID's quantity do you want to change:"))

    if product_id in cart:
        product_quantity = int(input("Enter Quantity:"))

        if product_quantity > 0:
            cart[product_id] = product_quantity
        else:
            print(
                f'Sorry quantity number can not be {product_quantity}.It should be bigger than 0')
            # print(f'Sorry quantity number can not be {"product_quantity"}')
    else:
        print("\nSorry Product not available in cart!!")

    view_shopping_cart(catalog, cart)


# remove values from cart
def remove_from_cart(catalog, cart):
    view_shopping_cart(catalog, cart)
    product_id = int(input("Enter Product ID:"))

    if product_id in cart:
        del cart[product_id]
        print("Succcessfully Deleted!")
        view_shopping_cart(catalog, cart)
    else:
        print("Not Available!")


# Main Program
while True:
    print("\n=============================================")
    print("           Welcome to Shopping Cart!")
    print("=============================================\n")
    print("[1] View Product Catalog\n[2] Add Product to Cart\n[3] View Shopping Cart & Total\n[4] Update Product Quantity in Cart\n[5] Remove Product from Cart\n[0] Exit")

    choice = int(
        input("===========================================\nEnter Your Choice (0-5):"))

    if choice == 0:
        break
    elif choice == 1:
        view_product_catalog(product_catalog)
    elif choice == 2:
        add_to_cart(product_catalog, shopping_cart)
    elif choice == 3:
        view_shopping_cart(product_catalog, shopping_cart)
    elif choice == 4:
        update_quantity(product_catalog, shopping_cart)
    elif choice == 5:
        remove_from_cart(product_catalog, shopping_cart)

#data_structure
product_catalog={1234:{"name":"book","price":234},
                 1223:{"name":"dress","price":2354},
                 2324:{"name":"clock","price":3354}
}

shopping_cart={1234:11,1223:4,4343:56}#product id is key and quantity is value


def view_product_catalog(catalog):
    print("\n=============Product Catalog=====================")
    count=1
    for product_id,product_name_price in catalog.items():
            print(f"\nProduct{count} Information")
            print("\nProduct ID:",product_id)
            for product_name in product_name_price:
                print("Product",product_name,":",product_name_price[product_name])
            count=count+1


#add product to cart
#what does this function do:
#check first if the product is available in the product list
#if it available then it checks if it is already exist in the cart list
#A) if it exists, adds the current quantity to the list
#B) if it does not exists, then it is added to the shopping cart
#if the item not availble in the product list then this information is shown to the user
def add_to_cart(catalog,cart):
    product_id=int(input("Enter Product ID:"))
    Quantity=int(input("Enter Quantity:"))
    if product_id in catalog:
        print ("product is available in product catalog",catalog.get(product_id,0))# to check if the product already exists
        if product_id in cart:#this will check if product id is already in shopping cart
            #shopping_cart.update({productID:shopping_cartproduct_id]+Quantity})
            cart[product_id]+=Quantity
            print("cart updated",cart[product_id])
        else:
            print("product is not avaliable in shopping cart!")
            cart.update({product_id:Quantity})
            print("cart updated",cart)
    else:
        print("Sorry! No Result!!!")


def view_shopping_cart(catalog,cart):
    print("\n===============Shopping Cart=================")
    sum=0
    for product_id in cart:
        print("Product ID:",product_id,"\nProduct Quantity:",cart[product_id])
        if product_id  in catalog:
            product_info=catalog[product_id]
            print("Product Name:",product_info["name"])
            print("Unit Price:",product_info["price"])
            total=product_info["price"] * cart[product_id]
            print(f'Total Price of {product_info["name"]}:{total}\n')
            sum=sum+total
        else:
            print(f'{product_id} ID not available to Product Catalog!')
    print("Final Total Price of All the Added Product:",sum)


#update the quantity of the product
#changes total price and indivisual summation of price when quantity changes
def update_quantity(catalog,cart):
    view_shopping_cart(catalog,cart)
    product_id=int(input("\nwhich product ID's quantity do you want to change:"))
    if product_id in cart:
        product_quantity=int(input("Enter Quantity:"))
        if product_quantity>0:
            cart[product_id]=product_quantity
        else:
            print(f'Sorry quantity number can not be {product_quantity}.It should be bigger than 0')
            # print(f'Sorry quantity number can not be {"product_quantity"}')
    else:
        print("\nSorry Product not available in cart!!")
    view_shopping_cart(catalog,cart)

#remove values from cart
def remove_from_cart(catalog,cart):
    view_shopping_cart(catalog,cart)
    product_id=int(input("Enter Product ID:"))
    if product_id in cart:
        del cart[product_id]
        print("Succcessfully Deleted!")
        view_shopping_cart(catalog,cart)
    else:
        print("Not Available!")


while True:
    print("\n=============================================")
    print("           Welcome to Shopping Cart!")
    print("=============================================\n")
    print("[1] View Product Catalog\n[2] Add Product to Cart\n[3] View Shopping Cart & Total\n[4] Update Product Quantity in Cart\n[5] Remove Product from Cart\n[0] Exit")
    choice=int(input("===========================================\nEnter Your Choice (0-5):"))

    if choice==0:
        break
    elif choice==1:
        view_product_catalog(product_catalog)
    elif choice==2:
        add_to_cart(product_catalog,shopping_cart)
    elif choice==3:
        view_shopping_cart(product_catalog,shopping_cart)
    elif choice==4:
        update_quantity(product_catalog,shopping_cart)
    elif choice ==5:
        remove_from_cart(product_catalog,shopping_cart)



# data_structure
product_catalog = {1234: {"name": "book", "price": 234},
                   1223: {"name": "dress", "price": 2354},
                   2324: {"name": "clock", "price": 3354}
                   }

# product id is key and quantity is value
shopping_cart = {1234: 11, 1223: 4, 4343: 56}


# gives the full detail info of product catalog
def view_product_catalog(catalog):
    print("\n=============Product Catalog=====================")
    count = 1

    for product_id, product_name_price in catalog.items():
        print(f"\nProduct{count} Information")
        print("\nProduct ID:", product_id)

        for product_name in product_name_price:
            print("Product", product_name, ":",
                  product_name_price[product_name])
        count = count+1


# add product to cart
# what does this function do:
# check first if the product is available in the product list
# if it available then it checks if it is already exist in the cart list
# A) if it exists, adds the current quantity to the list
# B) if it does not exists, then it is added to the shopping cart
# if the item not availble in the product list then this information is shown to the user
def add_to_cart(catalog, cart):
    product_id = int(input("Enter Product ID:"))
    Quantity = int(input("Enter Quantity:"))

    if product_id in catalog:
        print("product is available in product catalog", catalog.get(
            product_id, 0))  # to check if the product already exists

        if product_id in cart:  # this will check if product id is already in shopping cart
            # shopping_cart.update({productID:shopping_cartproduct_id]+Quantity})
            cart[product_id] += Quantity
            print("cart updated", cart[product_id])
        else:
            print("product is not avaliable in shopping cart!")
            cart.update({product_id: Quantity})
            print("cart updated", cart)
    else:
        print("Sorry! No Result!!!")

# view the cart


def view_shopping_cart(catalog, cart):
    print("\n===============Shopping Cart=================")
    sum = 0

    for product_id in cart:
        print("Product ID:", product_id,
              "\nProduct Quantity:", cart[product_id])

        if product_id in catalog:
            product_info = catalog[product_id]
            print("Product Name:", product_info["name"])
            print("Unit Price:", product_info["price"])
            total = product_info["price"] * cart[product_id]
            print(f'Total Price of {product_info["name"]}:{total}\n')
            sum = sum+total
        else:
            print(f'{product_id} ID not available to Product Catalog!')

    print("Final Total Price of All the Added Product:", sum)


# update the quantity of the product
# changes total price and indivisual summation of price when quantity changes
def update_quantity(catalog, cart):
    view_shopping_cart(catalog, cart)
    product_id = int(
        input("\nwhich product ID's quantity do you want to change:"))

    if product_id in cart:
        product_quantity = int(input("Enter Quantity:"))

        if product_quantity > 0:
            cart[product_id] = product_quantity
        else:
            print(
                f'Sorry quantity number can not be {product_quantity}.It should be bigger than 0')
            # print(f'Sorry quantity number can not be {"product_quantity"}')
    else:
        print("\nSorry Product not available in cart!!")

    view_shopping_cart(catalog, cart)


# remove values from cart
def remove_from_cart(catalog, cart):
    view_shopping_cart(catalog, cart)
    product_id = int(input("Enter Product ID:"))

    if product_id in cart:
        del cart[product_id]
        print("Succcessfully Deleted!")
        view_shopping_cart(catalog, cart)
    else:
        print("Not Available!")


# Main Program
while True:
    print("\n=============================================")
    print("           Welcome to Shopping Cart!")
    print("=============================================\n")
    print("[1] View Product Catalog\n[2] Add Product to Cart\n[3] View Shopping Cart & Total\n[4] Update Product Quantity in Cart\n[5] Remove Product from Cart\n[0] Exit")

    choice = int(
        input("===========================================\nEnter Your Choice (0-5):"))

    if choice == 0:
        break
    elif choice == 1:
        view_product_catalog(product_catalog)
    elif choice == 2:
        add_to_cart(product_catalog, shopping_cart)
    elif choice == 3:
        view_shopping_cart(product_catalog, shopping_cart)
    elif choice == 4:
        update_quantity(product_catalog, shopping_cart)
    elif choice == 5:
        remove_from_cart(product_catalog, shopping_cart)

#data_structure
product_catalog={1234:{"name":"book","price":234},
                 1223:{"name":"dress","price":2354},
                 2324:{"name":"clock","price":3354}
}

shopping_cart={1234:11,1223:4,4343:56}#product id is key and quantity is value


def view_product_catalog(catalog):
    print("\n=============Product Catalog=====================")
    count=1
    for product_id,product_name_price in catalog.items():
            print(f"\nProduct{count} Information")
            print("\nProduct ID:",product_id)
            for product_name in product_name_price:
                print("Product",product_name,":",product_name_price[product_name])
            count=count+1


#add product to cart
#what does this function do:
#check first if the product is available in the product list
#if it available then it checks if it is already exist in the cart list
#A) if it exists, adds the current quantity to the list
#B) if it does not exists, then it is added to the shopping cart
#if the item not availble in the product list then this information is shown to the user
def add_to_cart(catalog,cart):
    product_id=int(input("Enter Product ID:"))
    Quantity=int(input("Enter Quantity:"))
    if product_id in catalog:
        print ("product is available in product catalog",catalog.get(product_id,0))# to check if the product already exists
        if product_id in cart:#this will check if product id is already in shopping cart
            #shopping_cart.update({productID:shopping_cartproduct_id]+Quantity})
            cart[product_id]+=Quantity
            print("cart updated",cart[product_id])
        else:
            print("product is not avaliable in shopping cart!")
            cart.update({product_id:Quantity})
            print("cart updated",cart)
    else:
        print("Sorry! No Result!!!")


def view_shopping_cart(catalog,cart):
    print("\n===============Shopping Cart=================")
    sum=0
    for product_id in cart:
        print("Product ID:",product_id,"\nProduct Quantity:",cart[product_id])
        if product_id  in catalog:
            product_info=catalog[product_id]
            print("Product Name:",product_info["name"])
            print("Unit Price:",product_info["price"])
            total=product_info["price"] * cart[product_id]
            print(f'Total Price of {product_info["name"]}:{total}\n')
            sum=sum+total
        else:
            print(f'{product_id} ID not available to Product Catalog!')
    print("Final Total Price of All the Added Product:",sum)


#update the quantity of the product
#changes total price and indivisual summation of price when quantity changes
def update_quantity(catalog,cart):
    view_shopping_cart(catalog,cart)
    product_id=int(input("\nwhich product ID's quantity do you want to change:"))
    if product_id in cart:
        product_quantity=int(input("Enter Quantity:"))
        if product_quantity>0:
            cart[product_id]=product_quantity
        else:
            print(f'Sorry quantity number can not be {product_quantity}.It should be bigger than 0')
            # print(f'Sorry quantity number can not be {"product_quantity"}')
    else:
        print("\nSorry Product not available in cart!!")
    view_shopping_cart(catalog,cart)

#remove values from cart
def remove_from_cart(catalog,cart):
    view_shopping_cart(catalog,cart)
    product_id=int(input("Enter Product ID:"))
    if product_id in cart:
        del cart[product_id]
        print("Succcessfully Deleted!")
        view_shopping_cart(catalog,cart)
    else:
        print("Not Available!")


while True:
    print("\n=============================================")
    print("           Welcome to Shopping Cart!")
    print("=============================================\n")
    print("[1] View Product Catalog\n[2] Add Product to Cart\n[3] View Shopping Cart & Total\n[4] Update Product Quantity in Cart\n[5] Remove Product from Cart\n[0] Exit")
    choice=int(input("===========================================\nEnter Your Choice (0-5):"))

    if choice==0:
        break
    elif choice==1:
        view_product_catalog(product_catalog)
    elif choice==2:
        add_to_cart(product_catalog,shopping_cart)
    elif choice==3:
        view_shopping_cart(product_catalog,shopping_cart)
    elif choice==4:
        update_quantity(product_catalog,shopping_cart)
    elif choice ==5:
        remove_from_cart(product_catalog,shopping_cart)



