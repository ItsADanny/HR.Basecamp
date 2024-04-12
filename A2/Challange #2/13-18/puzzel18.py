# Create a class in which we will store each user coin amount
class bankclient:
    def __init__(self, name):
        self.name = name
        self.astrocoin = 100
        self.belgacoin = 100
        self.chinacoin = 100
        self.deltacoin = 100
        self.extracoin = 100


# Create a Dictionary which stores the value for each coin type
dict_coinvalues = {"astrocoin": 13, "belgacoin": 17, "chinacoin": 19, "deltacoin": 11, "extracoin": 15}

# Create a list with all the unique names
unique_names = [
    'Alice', 'Bob', 'Ben', 'Carol', 'Charlie', 'Dave', 'David', 'Eve', 'Emma', 'Frank',
    'Fred', 'Grace', 'George', 'Harry', 'Helen', 'Ivan', 'Ingrid', 'Jack', 'Kate', 'Leo',
    'Mary', 'Nathan', 'Olivia', 'Paul', 'Quinn', 'Rachel', 'Sam', 'Tina', 'Ulysses', 'Victor',
    'Wendy', 'Xavier', 'Yara', 'Zach'
]

# Creat a list with all the transactions
transactions = [
    [1, "Alice", "Bob", "astrocoin", 10],
    [2, "Ben", "Carol", "belgacoin", 15],
    [3, "Charlie", "Dave", "chinacoin", 20],
    [4, "David", "Eve", "deltacoin", 8],
    [5, "Emma", "Frank", "extracoin", 12],
    [6, "Fred", "Grace", "astrocoin", 25],
    [7, "George", "Harry", "belgacoin", 18],
    [8, "Helen", "Ivan", "chinacoin", 30],
    [9, "Ingrid", "Jack", "deltacoin", 22],
    [10, "Jack", "Kate", "extracoin", 14],
    [11, "Kate", "Leo", "astrocoin", 9],
    [12, "Leo", "Mary", "belgacoin", 17],
    [13, "Mary", "Nathan", "chinacoin", 11],
    [14, "Nathan", "Olivia", "deltacoin", 20],
    [15, "Olivia", "Paul", "extracoin", 16],
    [16, "Paul", "Quinn", "astrocoin", 13],
    [17, "Quinn", "Rachel", "belgacoin", 19],
    [18, "Rachel", "Sam", "chinacoin", 10],
    [19, "Sam", "Tina", "deltacoin", 15],
    [20, "Tina", "Ulysses", "extracoin", 21],
    [21, "Ulysses", "Victor", "astrocoin", 18],
    [22, "Victor", "Wendy", "belgacoin", 23],
    [23, "Wendy", "Xavier", "chinacoin", 25],
    [24, "Xavier", "Yara", "deltacoin", 11],
    [25, "Yara", "Zach", "extracoin", 20],
    [26, "Zach", "Alice", "astrocoin", 10],
    [27, "Alice", "Carol", "belgacoin", 15],
    [28, "Ben", "Dave", "chinacoin", 20],
    [29, "Charlie", "Eve", "deltacoin", 8],
    [30, "David", "Frank", "extracoin", 12],
    [31, "Emma", "Grace", "astrocoin", 25],
    [32, "Fred", "Harry", "belgacoin", 18],
    [33, "George", "Ivan", "chinacoin", 30],
    [34, "Helen", "Jack", "deltacoin", 22],
    [35, "Ingrid", "Kate", "extracoin", 14],
    [36, "Jack", "Leo", "astrocoin", 9],
    [37, "Kate", "Mary", "belgacoin", 17],
    [38, "Leo", "Nathan", "chinacoin", 11],
    [39, "Mary", "Olivia", "deltacoin", 20],
    [40, "Nathan", "Paul", "extracoin", 16],
    [41, "Olivia", "Quinn", "astrocoin", 13],
    [42, "Paul", "Rachel", "belgacoin", 19],
    [43, "Quinn", "Sam", "chinacoin", 10],
    [44, "Rachel", "Tina", "deltacoin", 15],
    [45, "Sam", "Ulysses", "extracoin", 21],
    [46, "Tina", "Victor", "astrocoin", 18],
    [47, "Ulysses", "Wendy", "belgacoin", 23],
    [48, "Victor", "Xavier", "chinacoin", 25],
    [49, "Wendy", "Yara", "deltacoin", 11],
    [50, "Xavier", "Zach", "extracoin", 20],
    [51, "Zach", "Alice", "astrocoin", 10],
    [52, "Alice", "Bob", "belgacoin", 15],
    [53, "Ben", "Carol", "chinacoin", 20],
    [54, "Charlie", "Dave", "deltacoin", 8],
    [55, "David", "Eve", "extracoin", 12],
    [56, "Emma", "Frank", "astrocoin", 25],
    [57, "Fred", "Grace", "belgacoin", 18],
    [58, "George", "Harry", "chinacoin", 30],
    [59, "Helen", "Ivan", "deltacoin", 22],
    [60, "Ingrid", "Jack", "extracoin", 14],
    [61, "Jack", "Leo", "astrocoin", 9],
    [62, "Kate", "Leo", "belgacoin", 17],
    [63, "Leo", "Mary", "chinacoin", 11],
    [64, "Mary", "Nathan", "deltacoin", 20],
    [65, "Nathan", "Olivia", "extracoin", 16],
    [66, "Olivia", "Paul", "astrocoin", 13],
    [67, "Paul", "Quinn", "belgacoin", 19],
    [68, "Quinn", "Rachel", "chinacoin", 10],
    [69, "Rachel", "Sam", "deltacoin", 15],
    [70, "Sam", "Tina", "extracoin", 21],
    [71, "Tina", "Ulysses", "astrocoin", 18],
    [72, "Ulysses", "Victor", "belgacoin", 23],
    [73, "Victor", "Wendy", "chinacoin", 25],
    [74, "Wendy", "Xavier", "deltacoin", 11],
    [75, "Xavier", "Yara", "extracoin", 20],
    [76, "Yara", "Zach", "astrocoin", 15],
    [77, "Zach", "Alice", "belgacoin", 19],
    [78, "Alice", "Carol", "chinacoin", 14],
    [79, "Wendy", "Xavier", "deltacoin", 11],
    [80, "Xavier", "Yara", "extracoin", 20],
    [81, "Yara", "Zach", "astrocoin", 15],
    [82, "Zach", "Alice", "belgacoin", 19],
    [83, "Alice", "Carol", "chinacoin", 14],
    [84, "Carol", "Dave", "deltacoin", 11],
    [85, "Dave", "Eve", "extracoin", 20],
    [86, "Eve", "Frank", "astrocoin", 15],
    [87, "Frank", "Grace", "belgacoin", 19],
    [88, "Grace", "Harry", "chinacoin", 14],
    [89, "Harry", "Ivan", "deltacoin", 11],
    [90, "Ivan", "Jack", "extracoin", 20],
    [91, "Jack", "Kate", "astrocoin", 15],
    [92, "Kate", "Leo", "belgacoin", 19],
    [93, "Leo", "Mary", "chinacoin", 14],
    [94, "Mary", "Nathan", "deltacoin", 11],
    [95, "Nathan", "Olivia", "extracoin", 20],
    [96, "Olivia", "Paul", "astrocoin", 15],
    [97, "Paul", "Quinn", "belgacoin", 19],
    [98, "Quinn", "Rachel", "chinacoin", 14],
    [99, "Rachel", "Sam", "deltacoin", 11]
]


def preform_transaction(fromuser, touser, cointype, amount):
    if cointype == "astrocoin":
        fromuser.astrocoin -= amount
        touser.astrocoin += amount
    if cointype == "belgacoin":
        fromuser.belgacoin -= amount
        touser.belgacoin += amount
    if cointype == "chinacoin":
        fromuser.chinacoin -= amount
        touser.chinacoin += amount
    if cointype == "deltacoin":
        fromuser.deltacoin -= amount
        touser.deltacoin += amount
    if cointype == "extracoin":
        fromuser.extracoin -= amount
        touser.extracoin += amount


# Create a List variable in which we will store the bankclients
bankclients = []
# Loop over all the unique names and create a new bankclient object for each unique name
for user in unique_names:
    new_bankclient = bankclient(user)
    bankclients.append(new_bankclient)

# Loop through all the transactions
for transaction in transactions:
    # Retriev the transaction information
    from_user = transaction[1]
    to_user = transaction[2]
    cointype = transaction[3]
    amount = transaction[4]

    from_user_bankclient = None
    to_user_bankclient = None

    # retriev the bankclient (from_user)
    for bankclient in bankclients:
        if from_user == bankclient.name:
            from_user_bankclient = bankclient

    # retriev the bankclient (to_user)
    for bankclient in bankclients:
        if to_user == bankclient.name:
            to_user_bankclient = bankclient

    # TEMP DEBUGGING - LINE 173
    # print(f"from_user : {from_user}")
    # print(f"to_user   : {to_user}")
    # print(f"cointype  : {cointype}")
    # print(f"amount    : {amount}")

    preform_transaction(from_user_bankclient, to_user_bankclient, cointype, amount)

most_money_user = ""
most_money_amount = 0
for bankclient in bankclients:

    bankclient_name = bankclient.name
    bankclient_astrocoin = bankclient.astrocoin
    bankclient_belgacoin = bankclient.belgacoin
    bankclient_chinacoin = bankclient.chinacoin
    bankclient_deltacoin = bankclient.deltacoin
    bankclient_extracoin = bankclient.extracoin

    euro_amount = 0

    for i in range(bankclient_astrocoin):
        coin_value = dict_coinvalues["astrocoin"]
        euro_amount += coin_value

    for i in range(bankclient_belgacoin):
        coin_value = dict_coinvalues["belgacoin"]
        euro_amount += coin_value

    for i in range(bankclient_chinacoin):
        coin_value = dict_coinvalues["chinacoin"]
        euro_amount += coin_value

    for i in range(bankclient_deltacoin):
        coin_value = dict_coinvalues["deltacoin"]
        euro_amount += coin_value

    for i in range(bankclient_extracoin):
        coin_value = dict_coinvalues["extracoin"]
        euro_amount += coin_value

    # TEMP DEBUGGING - LINE 214
    # print("coin values")
    # print(f"astrocoin : {dict_coinvalues["astrocoin"]}")
    # print(f"belgacoin : {dict_coinvalues["belgacoin"]}")
    # print(f"chinacoin : {dict_coinvalues["chinacoin"]}")
    # print(f"deltacoin : {dict_coinvalues["deltacoin"]}")
    # print(f"extracoin : {dict_coinvalues["extracoin"]}")
    # print("bankclient info")
    # print(f"bankclient_name      : {bankclient_name}")
    # print(f"bankclient_astrocoin : {bankclient_astrocoin}")
    # print(f"bankclient_belgacoin : {bankclient_belgacoin}")
    # print(f"bankclient_chinacoin : {bankclient_chinacoin}")
    # print(f"bankclient_deltacoin : {bankclient_deltacoin}")
    # print(f"bankclient_extracoin : {bankclient_extracoin}")
    # print(f"euro_amount          : {euro_amount}")

    if euro_amount > most_money_amount:
        most_money_user = bankclient_name
        most_money_amount = euro_amount

print(f"most_money_user   : {most_money_user}")
print(f"most_money_amount : {most_money_amount}")