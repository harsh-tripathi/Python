"""
i=0
while True :
    if i+1<5:
        i=i+1
        continue
    print(i+1, end=" ")
    if i == 44:
        break #Stop the loop
    i = i+1
"""
#Yaha Par

#Enter a number greater than 100 or keep giving input

while True :
    x = int(input("Enter a number : "))
    if x > 100:
        break
    else:
        continue
print("Thanks for playing")