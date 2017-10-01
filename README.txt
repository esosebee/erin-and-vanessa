----------------------------------
Project 1: ID3 Decision Tree
Authors: Erin Sosebee, Vanessa Job
----------------------------------

* PROGRAM EXECUTION *

The program's entry point is src/main.py. To execute the program, do the following:
    python main.py -train path/to/training-file.csv -test path/to/testing-file.csv

If the program is run without the -train and -test parameters, like the following:
    python main.py
it will use the training.csv and testing.csv files provided for the project by 
default.

Please note that the paths must be the exact location of the files. For example, on my local machine I run the following:
    
    python main.py -train /Users/ems/School/Fall 2017/CS 529/Project 1/Data/training.csv -test /Users/ems/School/Fall 2017/CS 529/Project 1/Data/testing.csv

Also note that the program can be run from the project's main directory too. 
To do this, use 'python src/main.py' instead of 'python main.py'.

* FILES IN THIS PROJECT *

Project main directory:
- Data: contains the data files provided on Kaggle. 
    * training.csv 
    * testing.csv
- src: where the project's source files are located
    * main.py: the program's entry point. 
    * get_data.py: gets all the needed information from the training and testing files.
    * build_tree.py: builds the decision tree and is used to access information from each tree's node.
    * information_gain.py: contains all the functions needed for information gain, entropy, gini index, and dataset splitting

