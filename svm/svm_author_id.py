#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from class_vis import prettyPicture

features_train, features_test, labels_train, labels_test = preprocess()

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
#########################################################
clf = SVC(kernel="rbf", C=1000)

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

t0 = time()
clf.fit(features_train, labels_train)
print ("training time:"), round(time()-t0, 3), "s"

t1 = time()
pred = clf.predict(features_test)
print ("prediction time:"), round(time()-t1, 3), "s"

accuracy = accuracy_score(labels_test, pred)
print ("accuracy: "), accuracy 


#########################################################

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass