import os
import shutil

source=r"{}".format(input("Enter the location of the file you want to copy"))

inf = False
i = int(0)
add = 1
m = int(input("How many times would you like to copy the file? - Enter 0 for infinite"))

if m <= 0:
    inf = True


location = input("Enter the location you want the file to be copied to")
name = input("Enter the desired name of the copied file(s)")
extension = input("Enter the desired file extension of the copied files")


while i < m or inf == True:
    i = i + add
    print("{}/{}".format(i,m))
    dest = "{}\{}{}{}".format(location,name,i,extension)
    path=shutil.copy2(source,dest)
    if i >= m and inf == False:
        print("DONE!")
        break
