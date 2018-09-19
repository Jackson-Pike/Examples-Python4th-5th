# Format Input Jupyter Notebook | Jackson Pike | Sept 2018


#Get String To Input
string_form = input("Enter a string to reformat: ")
#Define Helper Arrays
f = [string_form.upper(), string_form.lower(), string_form.swapcase(), string_form.capitalize()]
p = ["Uppercase: ", "Lowercase: ", "Swapped Case: ", "Capitalized: "]
#Print Formatted Strings Using Helper Arrays  
i = 0
while i < 4:
         print(p[i], f[i])
         i+=1
         
