import math
print("hey there! \n ***find the area of polygon***")
f=1
while f: 
    
    choice= int(input("enter your choice :\n circle-1\n triangle-2\n square-3\n rectangle-4\n hexagon-5\nparallelogram-6\n trapezoid-7\n rhombus-8\n pentagon-9\nexit-10\n "))
    if choice==1:
        r= int(input("enter the radius of circle:"))
        ac=math.pi*r*r
        print("area of circle is: ",round(ac,2))
    
    elif choice==2:
        a= int(input("enter the first side: "))
        b= int(input("enter the second side: "))
        c= int(input("enter the third side: "))
        s=(a+b+c)/2
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print("area of a triangle is: ",round(area,2))
    elif choice==3:
        a=int(input("enter the side :"))
        area=a*a
        print("area of a square is: ",round(area,2))
    elif choice==4:
        a=int(input("enter the height :"))
        b=int(input("enter the width :"))
        area=a*b
        print("area of a rectangle is: ",round(area,2))
    elif choice==6:
        a=int(input("enter the height :"))
        b=int(input("enter the base :"))
        area=a*b
        print("area of a parallelogram is: ",round(area,2))
    elif choice==7:
        a=int(input("enter the height :"))
        b=int(input("enter the value of a parallel side :"))
        c=int(input("enter the value of another parallel side :"))
        area=1/2*(b+c)*a
        print("area of a trapezoid is: ",round(area,2))
    elif choice==8:
        a=int(input("enter the value of diagonal :"))
        b=int(input("enter the value of other diagonal:"))
        area=1/2*a*b
        print("area of a rhombus is: ",round(area,2))
    elif choice==5:
        a=int(input("enter the side :"))
        area=3*math.sqrt(3)/2*a*a
        print("area of a hexagon is: ",round(area,2))
    elif choice==9:
        a=int(input("enter the height :"))
        area=1/4*math.sqrt(5*(5+2*math.sqrt(5)))*a*a
        print("area of a pentagon is: ",round(area,2))    
    elif choice==10:
        f=0
    else :
            print("enter a valid number!")
print("thankyou***********")
