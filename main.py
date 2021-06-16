from salary import salary
from people import people
import datetime

DateCreation = datetime.datetime.today().strftime("%d-%m-%Y")

print("Local Date: ", DateCreation, "\n")

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
print("Закончено выполнение if __name__ == '__main__'")