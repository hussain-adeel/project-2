import pandas as pd
import random as rand
import time

def driver():
    print("Welcome To The Feature Select Algorithim.")
    file = str(input("Type in the name of the file you want to test: "))

    data = pd.read_csv(file, sep="  ", engine='python', header=None)

    print("Which algorithim would you like to run?")
    print("\t1) Forward Selection\n\t2) Backward Elimination")
    algo = int(input("Select: "))

    feature_search(data)

def leave_one_out_validation(data, current_set, feature_to_add):
    return rand.randint(0, 100)

def feature_search(data):
    for i in range(len(data)):
        print("on the " + str(data[0][i]) + " lvl")

driver()