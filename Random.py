import random
import sys
import os

# Defines the restart command
def restart():
        
        print("argv was",sys.argv)
        print("sys.executable was", sys.executable)
        print("restart now")
        os.execv(sys.executable, ['python'] + sys.argv)

# Defines the list of names
# Input the names in the following format 'name', etc.
nameList = ['Andrew', 'Hunter']

# User input's number
num = float(input("Number of names in list >>>"))

# If the user's inputed number does not == the amount of names in the list
# restart's the program until the inputed number is the same number of names on the list
if num != len(nameList):
    print("Wrong number of names in this list")
    restart()
else:
    print ("Randomly selcted name from list is - ", random.choice(nameList))
    input("Press Enter to continue")
