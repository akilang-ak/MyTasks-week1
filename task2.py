class InvalidSalaryError(Exception):
   
    pass

def bonus(salary, rate=0.1, *extras, **options):
    total_bonus = (salary * rate) + sum(extras)
    if 'cap' in options:
        total_bonus = min(total_bonus, options['cap'])
    return total_bonus


class Employee:
    def __init__(self, name, salary):
        if salary < 0:
            raise InvalidSalaryError(f"Invalid salary: {salary}")
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def get_details(self):
        return f"Name: {self.name}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()}, Team Size: {self.team_size}"



employees_data = [
    {"id": 1, "name": "Arun", "department": "Sales", "salary": 30000, "city": "Chennai"},
    {"id": 2, "name": "Priya", "department": "HR", "salary": 45000, "city": "Chennai"},
    {"id": 3, "name": "Rahul", "department": "IT", "salary": 60000, "city": "Bangalore"},
    {"id": 4, "name": "Divya", "department": "IT", "salary": 75000, "city": "Chennai"},
    {"id": 5, "name": "Karthik", "department": "Finance", "salary": 90000, "city": "Mumbai"},
    {"id": 6, "name": "Meena", "department": "Sales", "salary": 52000, "city": "Bangalore"},
    {"id": 7, "name": "Suresh", "department": "IT", "salary": 68000, "city": "Chennai"},
    {"id": 8, "name": "Anitha", "department": "HR", "salary": 48000, "city": "Mumbai"},
]

above_50k = [emp["name"] for emp in employees_data if emp["salary"] > 50000]
print(f"Above 50000: {above_50k}")

salaries_with_raise = list(map(lambda emp: {**emp, "salary": emp["salary"] * 1.1}, employees_data))


chennai_employees = list(filter(lambda emp: emp["city"] == "Chennai", employees_data))
chennai_names = [emp["name"] for emp in chennai_employees]
print(f"Chennai: {chennai_names}")



for emp in employees_data:
    if emp["salary"] == 0:
        continue
    if emp["salary"] > 85000:
        break



try:
    
    invalid_emp = Employee("Test", -500)
except InvalidSalaryError as e:
    print(f"Error: {e}")
finally:
    print("Transaction finished")
