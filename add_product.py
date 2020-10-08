#adding products to the warehouse


doc = open("prodfiles.txt", "x") #Please delete this line after running the program once.

class Product_Features:
    print(">>>>>>>>>>>>>>>>>>>Welcome to the inventory application!<<<<<<<<<<<<<<<<<<<")
    product_cat_price = []
    while True:
        choose = (input("please select the action you want to do\n 1-Add Product\n 2-Product Extraction\n 3-Show Products\n Press exit to q\n what is your choice? : "))
        if choose == "q":
            print("leaving...")
            break
        else:
            if choose == "1":
                name = input("please add to name :")
                prices = int(input("please add to price :"))
                product_cat_price+= [[name,prices]]
                print("product successfully added")
                doc = open("prodfiles.txt", "w")
                doc.write(str(product_cat_price))
            elif choose == "2":
                name = input("Enter the product you want to unlist :")
                prices = int(input("Enter the price of the item you want to unlist :"))
                product_cat_price.remove([name,prices])
                print("product successfully removed")
                doc.write(str(product_cat_price))
            elif choose == "3":
                doc = open("prodfiles.txt","r")
                print(doc.read())   
            else:
                print("Incorrect value try again!")
    
                    

                    
                    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
