# import csv
# # f1 = "C:\Users\user\states.txt"
# # f2 = "C:\Users\user\capitals.txt"

# states_list = open(r"C:\Users\user\states.txt", "r")
# states = states_list.read().split('\n')
# capital_list = open(r"C:\Users\user\capitals.txt", "r")
# capitals = capital_list.read().split('\n')
# data = {}
# # if len(states) == len(capitals):
# #     for i in range(0, len(states)):
# #         data[states[i]] = capitals[i]
# #     print('')
# for i, capital in enumerate(capitals):
#     data[states[i]] = capitals[i]

# with open(r"C:\Users\user\dict.csv", "w") as target_file:
#     fieldnames = ['state', 'capital']
#     writerow = csv.DictWriter(target_file, fieldnames = fieldnames)
#     writerow.writeheader()
#     for d, v in data.items():
#         writerow.writerow({fieldnames[0] : d, fieldnames[1]: v})
# print('')

# def write_csv(file_name, data, fieldnames):
#     with open(f"{filename}") as target_file:
#         writerow = csv.DictWriter(target_file, fieldnames = fieldnames)
#         writerow.writeheader()
#         for d, v in data.items():
#             writerow.writerow({fieldnames[0] : d, fieldnames[1]: v})


# def find_employee(e_name, employees):
#     for employee in employees:
#         if e_name.casefold() == employee['Name'].casefold():
#             output = f"This is the field with matched name : {employee}"
#             return output
#     return "There is no field with matching name"

# employees = [{'Name' : 'Anu', 'age' : 21, 'des': "Junior Developer", "Exp_in_years":1}, {'Name' : 'Pooja', 'age' : 25, 'des': "Senior Developer", "Exp_in_years":4},
#             {'Name' : 'Sam', 'age' : 28, 'des': "Senior Developer", "Exp_in_years":8}, {'Name' : 'Priya', 'age' : 27, 'des': "Senior Developer", "Exp_in_years":7},
#             {'Name' : 'James', 'age' : 22, 'des': "Junior Developer", "Exp_in_years":2}, {'Name' : 'Ajay', 'age' : 26, 'des': "Senior Developer", "Exp_in_years":5}]



# status= 'Y'
# while status == 'Y':
#     e_name = input("Enter Employee Name : ")
#     output = find_employee(e_name, employees)
#     print(output)
#     status = input("Do you want to continue Y/N :")
import re

data = 'SAMSUNG Galaxy F13 (Waterfall Blue, 64 GB) ₹9,499'
splitted_data = re.split(r'[()]', data)
mobile = {}
mobile['Model'] = splitted_data[0].strip()
mobile['Configuration'] = splitted_data[1]
mobile['Price'] = splitted_data[2].strip()
print(mobile)
