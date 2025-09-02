my_dict = {
    "first_name": "Jack",
    "last_name": "Kohli",
    "address": "never you mind"
}

customers = []

exit = False

print("type names to add to customer list or exit to stop")

while not exit:
    first_name = input("first name: ")
    if first_name == "exit":
        break
    last_name = input("last name: ")
    if last_name == "exit":
        break
    customers.append({"first_name": first_name, "last_name": last_name})

if len(customers):
    print(customers)
else:
    print("no customers entered")

search = {}
search["first_name"] = input("enter the first name you want to find: ")
search["last_name"] = input("enter the last name you want to find: ")

results = []

for c in customers:
    if search["first_name"] and search["last_name"]:
        if search == c:
            results.append(c)
    elif search["first_name"]:
        if search["first_name"] == c["first_name"]:
            results.append(c)
    elif search["last_name"]:
        if search["last_name"] == c["last_name"]:
            results.append(c)
    else:
        break

if len(results):
    print(results)
else:
    print("no matching customers found")


# Create an LIST of customer in a dictionaries - Empty when initilised

# prnt out instructions, enter customer details and type exit to quit 

# when loop starts will always be True

# Loop based on user input

# if user types exit, stop the loop

# Store the inputs as first_name, last_name

# add the user inputs into the dictionary


# Print the LIST of dictionaries when the user exits

#EXTENSTION

# search or filter customers by first or last name

# create a second input for name to search for

# find matching customers

# display the results or print no customers found