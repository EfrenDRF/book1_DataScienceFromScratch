"""
    Author:         Efren Del Real Frias
    FileName:       DataSciencester_Net.py
    Date:           January 1st 2022

    Chapter:        1
    ChapterName:    Introduction

    Description:    Contains DataSciencester network dump.
"""
from pprint import pprint

#-------------------------------------
# users
#-------------------------------------
# List of users, eacg reoresebted by 
# a dict that contains user's 'id'
# and user's 'name'
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Davin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

#-------------------------------------
# friendship_pairs
#-------------------------------------
# Represented a list of pairs of 'id'
friendship_pairs = [
    (0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)
]

#-------------------------------------
# interests
#-------------------------------------
#
interests = [
    (0, 'Hadoop'), (0, 'Big Data'), (0, 'HBase'), (0, 'Java'), (0, 'Spark'), (0, 'Storm'), (0, 'Cassandra'),
    (1, 'NoSQL'), (1, 'MongoDB'), (1, 'Cassandra'), (1, 'HBase'), (1, 'Postgres'),
    (2, 'Python'), (2, 'scikit-learn'), (2, 'scipy'),(2, 'numpy'), (2, 'statsmodels'), (2, 'pandas'),
    (3, 'R'), (3, 'Python'), (3, 'statistics'), (3, 'regression'), (3, 'probability'), 
    (4, 'machine learning'), (4, 'regression'), (4, 'desision trees'), (4, 'libsvm'),
    (5, 'Python'), (5, 'R'),  (5, 'Java'), (5, 'C++'), (5, 'Haskell'), (5, 'programing languages'),
    (6, 'statistics'), (6, 'probability'), (6, 'mathematics'), (6, 'theory'), 
    (7, 'machine learning'),(7, 'scikit-learn'), (7, 'Mahout'), (7, 'neural networks'),
    (8, 'neural networks'),(8, 'deep learning'), (8, 'Big Data'), (8, 'artificial intelligence'),
    (9, 'Hadoop'), (9, 'Java'), (9, 'MapReduce'), (9, 'Big Data')
]


#-------------------------------------
# salaries_and_tenures
#-------------------------------------
#
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6.0),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10.0),
                        (48000, 1.9), (63000, 4.2)]

                        

if '__main__' == __name__:
    print("users:")
    pprint(users)

    print('friendship_pairs:')
    pprint(friendship_pairs)
