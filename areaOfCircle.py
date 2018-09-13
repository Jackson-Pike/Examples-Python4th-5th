#Jackson Pike | September 2018 | Python 4th/5th

#Calculate Area Of  Circle

#Define Function
def getArea():
    #Prompt user for the circle's radius
    radius = input("What is the radius?: ")
    #Convert user input from string to float
    radius = float(radius)
    #Calculate Area
    pi = 3.141592653
    area = radius*radius*pi
    #Display the area
    print("The area of your circle is: ", area)

#Run getArea() function

getArea()
