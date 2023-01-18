print("--------------------------------------------------------------------")
n=int(input("No. of items\n"))
#you can add last four digits of barcode here
cart={1881:["Chocolate",10],6151:["Rusk",20],7209:["Maggi",14]}
result=[]
itemname=[]
print("--------------------------------------------------------------------")
for i in range (1,n+1):
    b=int(input(f"Input last 4 digits of the barcode of product {i}\n"))
    nd=len(result)
    if b in cart.keys():
        result.append(cart[b][1])
        itemname.append(cart[b][0])
    else:
        print(f"You entered wrong barcode. So your cart consists of {nd} products")
total=0
leng=len(result)
print("--------------------------------------------------------------------")
print("Order List")
for jk in range (leng):
    print(itemname[jk],"-->",result[jk])
print("--------------------------------------------------------------------")
for j in result:
    total+=j
print(f"Your kart contains {leng} products")
print("The total for your order is",total)
print("--------------------------------------------------------------------")
ask=input("Press 'y' if you want to remove any item or 'n' for nothing\n")
if ask=='n':
    print("--------------------------------------------------------------------")
    print("So the final bill of your order is",total)
elif ask=='y':
    print("--------------------------------------------------------------------")
    bc=int(input("How many items you want to remove from the cart?\n"))
    for jkk in range (bc):
        bcc=int(input("Input last 4 digits of the barcode of the product\n"))
        if bcc in cart.keys():
            result.remove(cart[bcc][1])
            itemname.remove(cart[bcc][0])
        else:
            print("You didn't added this product in your cart")
lengg=len(result)
total1=0
for jkk in range (lengg):
    print(itemname[jkk],"-->",result[jkk])
for jj in result:
    total1+=jj
print("The total for your order is",total1)



