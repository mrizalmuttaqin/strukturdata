name=""
guests=[]
while name.upper()!="DONE":
    name = input("Enter guest name (enter DONE if no more names): ")
    if name.upper()!="DONE":
        guests.append(name)
        
guests.sort()
for guest in guests:
    print(guest)