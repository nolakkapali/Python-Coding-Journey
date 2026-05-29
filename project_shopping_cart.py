#data_structure
product_catalog={1234:{"name":"book","price":234},
                 1223:{"name":"dress","price":2354},
                 2324:{"name":"clock","price":3354}
}

shopping_cart={1234:11,1223:4}#product id is key and quantity is value

#add product to cart
#what does this function do:
#check first if the product is available in the product list
#if it available then it checks if it is already exist in the cart list
#A) if it exists, adds the current quantity to the list
#B) if it does not exists, then it is added to the shopping cart
#if the item not availble in the product list then this information is shown to the user
def add_to_cart(productID,Quantity):
    if productID in product_catalog:
        print ("product is available in product catalog",product_catalog.get(productID,0))# to check if the product already exists
        if productID in shopping_cart:#this will check if product id is already in shopping cart
            #shopping_cart.update({productID:shopping_cart[productID]+Quantity})
            shopping_cart[productID]+=Quantity
            print("cart updated",shopping_cart[productID])
        else:
            print("product is not avaliable in shopping cart!")
            shopping_cart.update({productID:Quantity})
            print("cart updated",shopping_cart)
    else:
        print("Sorry! No Result!!!")


print("Welcome to shopping cart!")
add_to_cart(1223,1)
