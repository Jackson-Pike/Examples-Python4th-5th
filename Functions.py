#Jackson Pike | September 2018

#Get A Users Name

def getName():
    #Ask for user's name, assign it to the variable 'name'
    name = input("Please Enter Your Name: ")
    #Display entered name, ask if it's correct
    correct = input("Is this name correct?: "+name+" ")
    #If their response (parsed to all uppercase) is yes, run this
    if correct.upper() == "YES":
        print("Yay!")
    #If their response was anything other then Yes or yes, run this,
    else:
        print("Shoot! Try again!")
        #Re-Run function
        getName()
#Run getName() function
getName()
