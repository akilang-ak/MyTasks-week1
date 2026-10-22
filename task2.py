import csv
import json
import os
import requests
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")

employees = []
high_earners = []

with open("employees.csv", "r",newline="", encoding="utf-8") as f:
    reader = list(csv.DictReader(f))
    for row in reader:
        employees.append(row)
        
        if int(row["salary"]) > 50000:
            high_earners.append(row)


with open("employees.json",mode="w", encoding="utf-8") as f:
    json.dump(employees, f, indent=4)


if high_earners:
    with open("high_earners.csv", mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=row[0].keys())
        writer.writeheader()
        writer.writerows(high_earners)

print(f"Rows read: {len(employees)} | High earners: {len(high_earners)}")


def load_dotkey():
    load_dotenv
    key = os.getenv("api_key")
    if not key:
        print("Warning: api_key not found in .env")
    else:
        print("api_key loaded successfully")
        return key




base_url = "https://jsonplaceholder.typicode.com/users"

try:
    
    response = requests.get(base_url, timeout=5)
    response.raise_for_status()
    users = response.json()
    
    
    if users:
        first_user = users[0]
        name = first_user.get("name")
        email = first_user.get("email")
        uid = first_user.get("id")
        print(f"{uid} - {name} -> {email}")
        
    
    with open("users.json", mode="w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

except requests.exceptions.Timeout:
    print("Error: The request timed out.")
except requests.exceptions.ConnectionError:
    print("Error: A connection error occurred.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error occurred: {e}")

try:
    url_404 = f"{base_url}/9999"
    res_404 = requests.get(url_404, timeout=5)
    
    if res_404.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        res_404.raise_for_status()
        
except requests.exceptions.Timeout:
    print("Error: The request timed out.")
except requests.exceptions.ConnectionError:
    print("Error: A connection error occurred.")
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error occurred: {e}")
