Name = ["Trapper Wolf", "Cara Dune", "Bo-Katan Kryze", "Paul Sun-Hyung Lee", "Dee Bradley Baker"]
for i in Name:

    names =i.split()
    if len(names) ==2 :
        first_name = names[0]
        last_name = names[1]
        print(f"First name: {first_name}\nMiddle name -\nLast name: {last_name}\n")
    elif len(names) == 3:
        first_name = names[0]
        middle_name = names[1]
        last_name = names[2]
        print(f"First name: {first_name}\nMiddle name: {middle_name} \nLast name: {last_name}\n")