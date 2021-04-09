import time

dashes = 1
spaces = 9
count = 0

for i in range(10):
    print("Loading[", end="")
    for x in range(dashes):
         print("#", end="")
    for y in range(spaces):
        print(end=" ")
    time.sleep(1)
    #clear()
    dashes += 1
    spaces -= 1
    count += 10
    print("] ", count, "%")
