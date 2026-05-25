#saree name
saree=dict(name="kanjivaram",product_code=1234,price=53334)
price={}
print(saree)
print(type(saree))
print(type(price))
price["saree"]=345224
price["rate"]=23
price["color"]="red"
print(price)
price["color1"]="green"
print(price)
price["color"]="green"
print(price)
price["color"]="green"
print(price)
print(len(price))
price["color"]="red"
print(price)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["brand"]="Volvo"
print(thisdict)
x=thisdict["model"]
print(x)
print(thisdict.get("model"))
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
if "model" in thisdict:
    print("Yes")
thisdict["color"]="red"
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())
#update
thisdict.update({"year":2028})
print(thisdict)
thisdict.update({"date":"23-4-2026"})
print(thisdict)
print(thisdict.pop("color"))
print(thisdict.popitem())
del thisdict ["brand"]
thisdict.clear()
print(thisdict)
del thisdict
# print(thisdict)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict=dict(thisdict)
print(mydict)
mydict1=thisdict.copy()
print("Mydict1:",mydict1)