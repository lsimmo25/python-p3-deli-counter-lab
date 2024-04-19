katz_deli=["Lyle", "Joe"]

def line(deli_line):
    if deli_line == []:
        print("The line is currently empty.")
    else:
        print("The line is currently:", end="")
        for i in range(len(deli_line)):
            print(f" {i + 1}. {deli_line[i]}", end="")
        print("")

def take_a_number(deli_line, name):
    if name in deli_line:
        position = deli_line.index(name) + 1
        print(f"Welcome, {name}. You are number {position} in line.")
    else:
        deli_line.append(name)
        position = len(deli_line)
        print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(deli_line):
    if len(deli_line) == 0:
        print("There is nobody waiting to be served!")
    else:
        person_served = deli_line.pop(0)
        print(f"Currently serving {person_served}.")