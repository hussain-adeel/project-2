from cmath import inf
import pandas as pd
import numpy as np
import random as rand
import time

def driver():
    print("Welcome To The Feature Select Algorithim.")
    file = str(input("Type in the name of the file you want to test: "))

    data = pd.read_csv(file, sep="  ", engine='python', header=None) # USING PANDAS TO READ FILE EASILY
    data = data.to_numpy() # CONVERT TO NUMPY FOR PERFORMANCE REASONS

    print("Which algorithim would you like to run?")
    print("\t1) Forward Selection\n\t2) Backward Elimination")
    algo = int(input("Select: "))

    start =  time.time()
    if algo == 1:
        print("This dataset has " + str(len(data[0]) - 1) + " features (not including class) with " + str(len(data)) + " instances.")
        full = []
        for i in range(2, len(data[0])):
            full.append(i)
        print("Running nearest neighbor (using 'leave-one-out' evaluation) with all " + str(len(data[0]) - 1) + " features, I get an accuarcy of: " + str(leave_one_out_validation(data, full, 1) * 100) + "%")
        feature_search(data)
    elif algo == 2:
        print("This dataset has " + str(len(data[0]) - 1) + " features (not including class) with " + str(len(data)) + " instances.")
        full = []
        for i in range(2, len(data[0])):
            full.append(i)
        print("Running nearest neighbor (using 'leave-one-out' evaluation) with all " + str(len(data[0]) - 1) + " features, I get an accuarcy of: " + str(leave_one_out_validation(data, full, 1) * 100) + "%")
        backwards_feature_elimination(data)
    end = time.time()
    total = round(end - start, 1)
    print("This attempt took: " + str(total) + " seconds.")

def leave_one_out_validation(data, current_set, feature_to_add):

    correctly_classified = 0
    full_set = list(current_set)
    full_set.append(feature_to_add)

    for i in range(len(data)):
        otc = data[i][1:]
        label_otc = data[i][0]
        c = 0
    
        nn_distance = inf
        nn_location = inf


        for k in range(len(data)):
            if not k == i:
                total = 0
                for j in full_set:

                    total += np.power(otc[j-1] - data[k][j], 2)

                distance = np.sqrt(total)

                if distance < nn_distance:
                    nn_distance = distance
                    nn_location = k
                    nn_label = data[nn_location][0]
                
        if label_otc == nn_label:
            correctly_classified += 1


    accuracy = correctly_classified / len(data)

    return accuracy

def feature_search(data):
    current_features = []
    best_overall = 0
    best_features = []

    print("Beginning Search...")
    for i in range(1, len(data[0])):
        feature_to_add = 0
        best_accuracy = 0
        for k in range(1, len(data[0])):
            if not current_features.count(k) > 0:
                acc = leave_one_out_validation(data, current_features, k)
                full_set = list(current_features)
                full_set.append(k)
                print("\tUsing feature(s) " + str(full_set) + " accuracy is " + str(acc * 100) + "%")
                if acc > best_accuracy:
                    best_accuracy = acc
                    feature_to_add = k
                    
        if feature_to_add > 0:
            current_features.append(feature_to_add)
            print("Feature set " + str(current_features) + " was the best, with accuracy " + str(best_accuracy * 100) + "%")
            if best_accuracy > best_overall:
                best_overall = best_accuracy
                best_features = list(current_features)


    print("Search Finished...")
    print("The best overall set of features was " + str(best_features) + " with accuarcy " + str(best_overall * 100) + "%")

def backwards_feature_elimination(data):
    current_features = []
    best_overall = 0
    best_features = []

    print("Beginning Search...")
    for i in range(1, len(data[0])):
        feature_to_add = 0
        best_accuracy = 0
        for k in range(1, len(data[0])):
            if not current_features.count(k) > 0:
                acc = leave_one_out_validation(data, current_features, k)
                full_set = list(current_features)
                full_set.append(k)
                print("\tUsing feature(s) " + str(full_set) + " accuracy is " + str(acc * 100) + "%")
                if acc > best_accuracy:
                    best_accuracy = acc
                    feature_to_add = k
                    
        if feature_to_add > 0:
            current_features.append(feature_to_add)
            print("Feature set " + str(current_features) + " was the best, with accuracy " + str(best_accuracy * 100) + "%")
            if best_accuracy > best_overall:
                best_overall = best_accuracy
                best_features = list(current_features)


    print("Search Finished...")
    print("The best overall set of features was " + str(best_features) + " with accuarcy " + str(best_overall * 100) + "%")

driver()