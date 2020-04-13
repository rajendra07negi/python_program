av = 5
x = int(input("How much candies you want? "))
i = 1
while i <= x:
    if i > av:
        print("Out of Stock")
        break
    print("Candy ",i)
    i+=1
