# Jupyter Notebook | Sept 2018 | Jackson Pike

#User Input For Animal Names
animals_input = input("Enter Some Animals, seperated with a ',' : ")

#Format Input To All Lowercase
animals_input = animals_input.lower()

#Split Input into an Array
anarr = animals_input.split(',')

#Get Number Of Animals In Array
numOfAnimals = len(anarr)

i = 0

while i < numOfAnimals:
    if  "cat" in anarr[i]:
        catfound = True
    else
        catfound = False
    i+=1
if catfound:
    print(catfound)
else:
    print(catfound)
