# Jackson Pike | Sept 2018 

#Get Vehicle Name From User
usrv = input("Enter Vehicle Name: ")

#Test Strings

#Define Arrays
s= ["Alphabetical: ", "Alphanumerical: ", "Capitalized: ", "Lowercase: "]
t = [usrv.isalpha(), usrv.isalnum(), usrv.istitle(), usrv.islower()]

#While Loop
i=0
while i < 4:
    if t[i]:
        print(s[i], "True")
    else:
        print(s[i], "False")
    i+=1

