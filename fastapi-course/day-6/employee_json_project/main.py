import json

def save_employee(employee: list[dict]) -> None:

    with open("employee.json", "w", encoding = "utf-8") as file:
        json.dump(employee, file, indent=4)

    print("Employee data save successfully")

def load_employee() -> list[dict]:
    try:
        with open("employee.json", "r", encoding="utf-8") as file:
            employee = json.load(file)
            return employee

    except FileNotFoundError:
        print("Employee file not found !!")
        return []

    except json.JSONDecodeError:
        print("Invalid json file !!")
        return []


employee = [
    {
        "id":101,
        "name":"Abhinav",
        "department":"IT",
        "salary":55000
    },
    {
        "id":102,
        "name":"Sahil",
        "department":"HR",
        "salary":40000
    }
]

save_employee(employee)

data = load_employee()

print("\nEmployee Records :-")

for emp in data:
    print("ID = ", emp["id"])
    print("Name = ", emp["name"])
    print("Department = ", emp["department"])
    print("Salary = ", emp["salary"])
    print("-----------------------------------")

