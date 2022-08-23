import requests
from csv import reader

### Simple Passwords ###
url = "https://www.dinopass.com/password/simple"

### Strong Passwords ###
#url = "https://www.dinopass.com/password/strong"

# open file in read mode
with open('users.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        resp = requests.get(url)
        password = resp.content.decode("utf-8")
        user = row[0]
        print(password)