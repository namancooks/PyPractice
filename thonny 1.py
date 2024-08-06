import sys
print("Menu")
print("1.Calculate area of circle")
print("2.Calculate circumfrence of circle")
print("3.Calculate surface area and lateral surface area of cone")
print("4.close the program")
while True:
    ch=int(input("Enter the choice"))
    if ch==1:
        print("you have choosen to Calculate area of circle")
        r=eval(input("Enter radius"))
        print("Area of cicle of radius",r,"is",3.14*r*r)
    elif ch==2:
        print("you have choosen to Calculate perimeter of circle")
        r=eval(input("Enter radius"))
        print("circumfrence of cicle of radius",r,"is",2*3.14*r)
    elif ch==3:
        print("you have choosen to Calculate surface area and lateral surface area of cone")
        r=eval(input("Enter radius"))
        l=eval(input("Enter lateral height of cone"))
        print("Total surface area of cone radius",r,"and lateral height",l, "is",(3.14*r*(l+r)))
        print("Lateral surface area of cone radius",r,"and lateral height",l, "is",3.14*r*l)
    elif ch==4:
        print("you have choosen to close the program")
        sys.exit
    else:
        print("invalid choice")
    answer = input('Run again? (y/n): ')
    if answer == 'n':
        print('Goodbye')
        break
    elif answer == 'y':
        continue
    else:
        print('Invalid input. Please enter y or n...')
print("Made by Naman Jain XII-A")


        
