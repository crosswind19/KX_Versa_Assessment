# Versa Test Assessment
# Cheah Kah Xuan 

import json

#Declare an array
array = []

# Function to replace numbers divisible by 3 with "BANG",
# numbers divisible by 5 with "BIG", and 
# numbers divisible by 15 with "BIG BANG"
def bigBang(x,y):
    for x in range(x,y):
        if(x%15==0):
            array.append("BIG BANG")
        elif (x%3 ==0):
            array.append("BIG")
        elif (x%5 ==0 ):
            array.append("BANG")
        else:
            array.append(x)

    return array

#Output for 1 to 100
output = bigBang(1,101)
print(output)

#Write into json file
with open('output.json', 'w') as outfile:
    json.dump(output, outfile)
