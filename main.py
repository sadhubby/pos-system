potato = 50
qty_potato = 0
apple = 35
qty_apple = 0
orange = 40
qty_orange = 0
banana = 25
qty_banana = 0
popcorn = 120
qty_popcorn = 0
water = 20 
qty_water = 0
cola = 45
qty_cola = 0
submenu_choice = 8

while submenu_choice == 8:
  submenu_choice = 0
  submenu1Loop = True
  mainmenu_choice = int(input("\n1. Show Menu\n2. Proceed to Payment\n3. Exit\nEnter selection: "))
  if mainmenu_choice == 1:
    while submenu1Loop == True:
      submenu_choice = int(input("\n1. Potato - 50.00 pesos\n2. Apple - 35.00 pesos\n3. Orange - 40.00 pesos\n4. Banana - 25.00 pesos\n5. Popcorn - 120.00 pesos\n6. Bottled Water - 20.00 pesos \n7. Cola - 45.00 pesos\n8. Back to main screen\nEnter selection: "))
      if submenu_choice == 1:
        qty_potato = qty_potato + int(input("\nSelected item: Potato\nQuantity: "))
      elif submenu_choice == 2:
        qty_apple = qty_apple + int(input("\nSelected item: Apple\nQuantity: "))
      elif submenu_choice == 3:
        qty_orange = qty_orange + int(input("\nSelected item: Orange\nQuantity: "))
      elif submenu_choice == 4:
        qty_banana = qty_banana + int(input("\nSelected item: Banana\nQuantity: "))
      elif submenu_choice == 5:
        qty_popcorn = qty_popcorn + int(input("\nSelected item: Popcorn\nQuantity: "))
      elif submenu_choice == 6:
        qty_water = qty_water + int(input("\nSelected item: Bottled Water\nQuantity: "))
      elif submenu_choice == 7: 
        qty_cola = qty_cola + int(input("\nSelected item: Cola\nQuantity: "))  
      elif submenu_choice == 8:
        submenu_choice = 8
        submenu1Loop = False
      ###else:
       ### print("Invalid option.")

  if mainmenu_choice == 2:
    print("\nYou're purchasing:\nPotatoes     :",qty_potato,"\nApples       :",qty_apple,"\nOranges      :",qty_orange,"\nBananas      :",qty_banana,"\nPopcorn      :",qty_popcorn,"\nBottled Water:",qty_water,"\nCola Cans    :",qty_cola)
    subtotal = (potato * qty_potato) + (apple * qty_apple) + (orange * qty_orange) + (banana * qty_banana) + (popcorn * qty_popcorn) + (water * qty_water) + (cola * qty_cola)
    print("Your subtotal is:",subtotal,"\nAmount paid:",end=" ")
    user_pay = float(input())
    ###discounts
    YesNo_Senior = int(input("Birthyear: "))
    YesNo_PWD = input("Are you a PWD?\nY or N: ")
    if YesNo_Senior <= 1959 and (YesNo_PWD == "Y" or YesNo_PWD == "y"):
      newtotal = subtotal * 0.85
      print("The original subtotal without Senior Citizen and PWD discounts is:", subtotal)
      print("The new subtotal with Senior Citizen and PWD discounts applied is:",newtotal)
    elif YesNo_Senior > 1959 and (YesNo_PWD == "N" or YesNo_PWD == "n"):
      newtotal = subtotal
      print("No discounts are applied.\n Subtotal is:", subtotal)
    elif YesNo_Senior <= 1959 and (YesNo_PWD == "N" or YesNo_PWD == "n"):
      newtotal = subtotal * 0.90
      print("The original subtotal without Senior Citizen is:", subtotal)
      print("The new subtotal with Senior Citizen discount is:", newtotal)
    elif YesNo_Senior > 1959 and (YesNo_PWD == "Y" or YesNo_PWD == "y"):
      newtotal = subtotal * 0.95
      print("The original subtotal without PWD is: ", subtotal)
      print("The new subtotal with PWD discount is:", newtotal)
    ###else:
      ###  print("Invalid option.")  
    change = user_pay - newtotal
    if change < 0:
      while change < 0:
        print("\nInsufficient amount.\nAdd to payment:",end="")
        user_payAdd = float(input())
        user_pay = user_pay + user_payAdd
        change = user_pay - newtotal
      print("Your change is:", change)
    else:
      print("Your change is:", change)
    print("Thank you so much for your patronage!")

  ###exitprogram
  if mainmenu_choice == 3:
    quit("Thank you so much for your patronage!")
  