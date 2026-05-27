product_catalog={"product1":{"ID":1234,"name":"book","price":234},
                 "product2":{"ID":1223,"name":"dress","price":2354},
                 "product3":{"ID":2324,"name":"clock","price":3354}
}

shopping_cart={"UserID":11,"Quantity":4,
               "UserID2":46,"Quantity2":45,}

#add product to cart
def add_to_cart(productID,Quantity):
    if productID in product_catalog:


add_to_cart(product_catalog["product1"],shopping_cart["Quantity"])