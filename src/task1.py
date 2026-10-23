class InvalidSalaryError(Exception):
    pass

def bonus( amount, rate=0.1, *extra, **options):
    salary_bonus=(amount*rate)+sum(extra)
    if 'cap' in options:
        salary_bonus = min(salary_bonus, options["tax"])
    return salary_bonus

class Employee:
    def __init__(self, name, amount):
        if amount < 0:
            raise InvalidSalaryError(f"InvalidSalaryError: {amount}")
        self.name = name
        self.amount = amount

    def annual_salary(self):
        return self.amount* 12
    
    def get_details(self):
        return f"Name: {self.name}, amount:{self.amount}"
    
class Manage(Employee):
    def __init__(self, name, amount,team_size):
        super().__init__(name, amount) 
        self.team_size = team_size

    def get_details(self):
        return f"{super().get_details()}, Team Size:{self.team_size}"
    
employees_data = [
        {"id":1, "name": "arun", "department":"Sales", "amount":30000, "city":"chennai"},
        {"id":2, "name": "Priya", "department":"Hr", "amount":45000, "city":"chennai"},
        {"id":3, "name": "rahul", "department":"It", "amount":60000, "city":"banglore"},
        {"id":4, "name": "divyaa", "department":"Engineering", "amount":75000, "city":"salem"},
        {"id":5, "name": "karthick", "department":"Hr", "amount":90000, "city":"dharumpuri"},
        {"id":6, "name": "meena", "department":"Sales", "amount":52000, "city":"chennai"},
        {"id":7, "name": "suresh", "department":"Sales", "amount":68000, "city":"chennai"},
        {"id":8, "name": "anitha", "department":"It", "amount":48000, "city":"mumbai"}
]


above_50k = [emp["name"] for emp in  employees_data if emp["amount"] > 50000]
print (above_50k)


salaries_with_raise = list(map(lambda emp: {**emp,"amount": emp["amount"]*1.1}, employees_data ))

chennai_employees = list( filter(lambda emp : emp["city"] == "chennai", employees_data ))
chennai_names = [emp["name"] for emp in chennai_employees]
print (chennai_names)

for emp in employees_data:
    if emp["amount"] == 0:
        continue 
    if emp["amount"] > 85000:
        break


try:
    invalid_emp = Employee("Test", -500)
except InvalidSalaryError as e :
    print(f"Error: {e}")

finally:
    print("Transaction Finished")