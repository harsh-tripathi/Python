# Python File1 Code

from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())


import file2
print(file2.a)

file2.printjoke("This is me")
  
# Python File2 Code

a =7
def printjoke(str):
    print(f"this function is a joke {str}")
  
# Some Extra Knowledge

import sys
print( sys.path)
import sklearn
from flask import Flask
import pandas as pd