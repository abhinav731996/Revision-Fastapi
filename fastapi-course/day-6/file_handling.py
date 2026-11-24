# # create file(write) --------------------------------------

# file = open("employee.txt", "w")

# file.write("Abhinav\n")
# file.write("Dinesh\n")
# file.write("Kaushik\n")

# file.close()



# # read file ----------------------------------------

# file = open("employee.txt", "r")

# data = file.read()
# print(data)
# file.close



# # add data on created file(append) ----------------------------

# file = open("employee.txt", "a")
# file.write("Nazir\n")
# print("successfully added!!")
# file.close()




# # Professional Way ------------------------------------------

# with open("employee.txt", "r") as file:
#     data = file.read()
#     print(data)




# # JSON – JavaScript Object Notation -----------------------------

import json

# employee = {
#     "id":101,
#     "name":"Abhinav",
#     "age":29,
#     "department":"IT",
#     "salary":55000
# }

# with open("employee.json", "w") as file:
#     json.dump(employee, file, indent=4)

# print("data save successfully !!!")
# print("-------------------------------------")

# with open("employee.json", "r") as file:
#     data = json.load(file)

# print(data)
# print(data["name"])
# print(data["salary"])

# note:---------
# json.load() file se JSON read karke Python dictionary mein convert karta hai.
# C. dump() vs dumps() aur load() vs loads()
# Ye difference yaad rakhiye:
# Function	Purpose
# json.dump()	Python data → JSON file
# json.dumps()	Python data → JSON string
# json.load()	JSON file → Python data
# json.loads()	JSON string → Python data


import json

employee = {
    "name" : "Abhinav",
    "salary" : "55000"
}

json_string = json.dumps(employee)

print(json_string)

read_data = json.loads(json_string)

print(read_data["name"])

