"""
    Author:         Efren Del Real Frias
    FileName:       main.py
    Date:           December 28th 2021

    Chapter:        1
    ChapterName:    Introduction

    Description:    Identify who the 'key connectors' are among
                    data scientits.
"""
from DataSciencester_Net import users, friendship_pairs, interests
from pprint import pprint
from collections import Counter, defaultdict


#
# KEY CONNECTORS
#

# Initialize the dict with an empty list for each user id
friendships = {user['id'] : [] for user in users}

# loop over the friendship pairs to populate it
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

print('[OUTPUT] friendships:')
pprint(friendships)
print()


#
# What is the average number of connections?
#
def number_of_friends(user):
    """ How many friends does _user_ have? """
    
    user_id = user['id']
    friend_ids = friendships[user_id]

    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)
print('[OUTPUT] total_connections: {}'.format(total_connections))

num_users = len(users)
avg_connections = total_connections / num_users
print('[OUTPUT] avg_connections: {}'.format(avg_connections))
print()

#
# Find the most connected people sorted from "most friends"
# to "least friends"
#

# Create a list of tuples (user_id, number_of_friends)
num_freinds_by_id = [(user['id'], number_of_friends(user)) for user in users]

print('[OUTPUT] num_freinds_by_id: {}'.format(num_freinds_by_id))
print('[PROCESS] sorting ....')

num_freinds_by_id.sort(                             # Sort the list
    key=lambda id_and_friends: id_and_friends[1],   # by num_friends
    reverse=True)                                   # largest to smallest

print('[OUTPUT] num_freinds_by_id: {}'.format(num_freinds_by_id))
print()


#
# DATA SCIENTICTS YOU MAY KNOW
#

def foaf_ids_bad(user):
    """ foaf is short for 'friend of a friend' """

    return [foaf_id
            for friend_id in friendships[user['id']]
            for foaf_id in friendships[friend_id]]

print('[OUTPUT] foaf_ids_bad id->{}, name->{}:'.format(users[0]['id'], users[0]['name']))
print('\t{}'.format(foaf_ids_bad(users[0])))
print()


def friends_of_friends(user):
    """ """
    user_id = user['id']

    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )

print('[OUTPUT] friends_of_friends id->{}, name->{}:'.format(users[0]['id'], users[0]['name']))
print('\t{}'.format(friends_of_friends(users[0])))
print()



def data_scientists_who_like(target_interest):
    """ Find the ids of all users who like target interest. """

    return [user_id 
        for user_id, user_interest in interests
        if user_interest == target_interest]

target_interestStr = 'Java'

print('[OUTPUT] data_scientists_who_like target_interest-> {}:'.format(target_interestStr))
print('\t{}'.format(data_scientists_who_like(target_interestStr)))
print()


# Keys are interets, values are list of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, user_interest in interests:
    user_ids_by_interest[user_interest].append(user_id)

print('[OUTPUT] user_ids_by_interest:')
pprint(user_ids_by_interest)
print()

# Another from users to interest
#keys are user_id, values are list of interest for that user_id
interests_by_user_id = defaultdict(list)

for user_id, user_interest in interests:
    interests_by_user_id[user_id]. append(user_interest)

print('[OUTPUT] interests_by_user_id:')
pprint(interests_by_user_id)
print()


def most_common_interest_with(user):
    user_id = user['id']
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user_id]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user_id
    )

print('[OUTPUT] most_common_interest_with id->{}, name->{}:'.format(users[0]['id'], users[0]['name']))
print('\t{}'.format(most_common_interest_with(users[0])))
print()


#
# SALARIES AND EXPERIENCE
#