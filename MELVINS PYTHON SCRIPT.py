import os
import time
import subprocess

print("(1)Network search tool \n(2)Bitlocker Search tool \n(3)Open System updates \n(4)Bitlocker Search tool, for a host in a different domain\n")
softChoice = int(input("Please enter the software you would like to Run:"))
print(softChoice)

if softChoice == 1:
    print("Running the Network Search tool")
    subprocess.call([r'C:\MULTI SCRIPT RUN TOOL\nettoolstarter.bat'])
    print("Thank you, for using the network search tool")

elif softChoice == 2:
    print("Running the Bitlocker Search tool")
    subprocess.call([r'C:\MULTI SCRIPT RUN TOOL\BITLOCKER RECOVERY.bat'])
    print("Thank you, for using the Bitlocker Search tool")
elif softChoice == 3:
    print("Running the Open System Updates")
    subprocess.call([r'C:\MULTI SCRIPT RUN TOOL\OPEN SYSTEM UPDATES.bat'])
    print("Thank you, for using the Open System Updates tool")

elif softChoice == 4:
    print("Running the Bitlocker Search tool for hosts on a different domain")
    subprocess.call([r'C:\MULTI SCRIPT RUN TOOL\BITLOCKER.bat'])
    print("Thank you, for using the Bitlocker Search tool for hosts on a different domain tool")

else:
    print("Your entry was not valid. Please re-run the scrip\nand enter a valid number.")

print("(1)Network search tool \n(2)Bitlocker Search tool \n(3)Open System updates \n(4)Bitlocker Search tool, for a host in a different domain\n")
softChoice = int(input("Please enter the software you would like to Run:"))
print(softChoice)

