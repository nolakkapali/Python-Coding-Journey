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


def remove_from_cart(productID):
    if productID in shopping_cart:
        del shopping_cart[productID]
        print(shopping_cart)

def update_quantity():
    print("which product quantity do you want to change:")



print("=============================================")
print("           Welcome to Shopping Cart!")
print("=============================================\n")
print("[1] View Product Catalog\n[2] Add Product to Cart\n[3] View Shopping Cart & Total\n[4] Update Product Quantity in Cart\n[5] Remove Product from Cart\n[0] Exit")
choice=int(input("===========================================\nEnter Your Choice (0-5):"))

if choice==0:

elif choice==1:
    add_to_cart(1223,3)
elif choice==2:
elif choice==3:
elif choice==4:
elif choice ==5:

print(shopping_cart)
remove_from_cart(1234)
update_quantity()