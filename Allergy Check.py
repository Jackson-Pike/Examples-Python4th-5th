#Allergy Check | Practice 1b Jupyter | Sept 2018 | Jackson Pike

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# Warning, This code is made        #
# Custom By Jack Pike. And is more  #
# complex than Needed.              #
#                                   #
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#

#Define Usr Input
input_test = input("Enter some things eaten in the last 24 hours: ")

#Define Arrays
allgns = ["seafood", "nut", "nuts", "dairy"]
other = ["Seafood", "Dairy", "Nuts"]
usrinput = input_test.split(",")
#Setup Loop and execute allergen search

i = 0
while i < len(usrinput):
