from operator import itemgetter, attrgetter
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]
print (users)
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    # possible parceque user[i] est l'utilisateur dont l'id est i
    users[i]["friends"].append(users[j])  # ajoute j comme ami de i
    users[j]["friends"].append(users[i])  # ajoute i comme ami de j

def number_of_friends(user):
    """combien d'amis l'utilisateur  _user_ a-t-il ?"""
    return len(user["friends"]) # longueur de la liste friends_ids

total_connections = sum(number_of_friends(user)
                        for user in users)
num_users = len(users)
avg_connections = total_connections / num_users

print("Le nombre moyen de connexions est :", avg_connections)

#créer une liste (user_id,number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

namy = sorted(num_friends_by_id,
              key=itemgetter(1),
              reverse=True)

print(*namy, sep="\n")


