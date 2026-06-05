#data_structure
product_catalog={1234:{"name":"book","price":234},
                 1223:{"name":"dress","price":2354},
                 2324:{"name":"clock","price":3354}
}

shopping_cart={1234:11,1223:4}#product id is key and quantity is value


def view_product_catalog():
    print("\n=============Product Catalog=====================")
    count=1
    for i,j in product_catalog.items():
            print(f"\nProduct{count} Information")
            print("\nProduct ID:",i)
            for k in j:
                print("Product",k,":",j[k])
                count=count+1


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


def view_shopping_cart():
    print("\n===============Shopping Cart=================")
    sum=0
    for i in shopping_cart:
        print("Product ID:",i,"\nProduct Quantity:",shopping_cart[i])
        for j,k in product_catalog.items():
            if i==j:
                print("Product Name:",k["name"],"\nUnit Price:",k["price"])
                total=k["price"]*shopping_cart[i]
                print(f"Total Price of {k["name"]}:{total}\n")
        sum=sum+total
    print("Final Total Price of All the Added Product:",sum)



def update_quantity():
    print("which product ID's quantity do you want to change:")
    product_quantity=int(input("Enter Quantity:"))

def remove_from_cart(productID):
    if productID in shopping_cart:
        del shopping_cart[productID]
        print(shopping_cart)


while True:
    print("\n=============================================")
    print("           Welcome to Shopping Cart!")
    print("=============================================\n")
    print("[1] View Product Catalog\n[2] Add Product to Cart\n[3] View Shopping Cart & Total\n[4] Update Product Quantity in Cart\n[5] Remove Product from Cart\n[0] Exit")
    choice=int(input("===========================================\nEnter Your Choice (0-5):"))

    if choice==0:
        break
    elif choice==1:
        view_product_catalog()
    elif choice==2:
        add_to_cart(1223,3)
    elif choice==3:
        view_shopping_cart()
    elif choice==4:
        update_quantity()
    elif choice ==5:
        remove_from_cart(1234)


