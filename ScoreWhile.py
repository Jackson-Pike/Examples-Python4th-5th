numOfTests = input("How many scores are you entering?: ")
numOfTests = int(numOfTests)
sum1 = 0
i=0
while i != numOfTests:
    score = input("Enter Score: "
    score = int(score)
    sum1 += score
    i = i+1
average = sum1/numOfTests
print("You averaged", average, "%")
 
