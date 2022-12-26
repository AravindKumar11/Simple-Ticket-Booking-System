print("\n\nWelcome! To Ticket Booking System")

print("1.Ticket Reservation")
print("2.Close")
option = int(input("\nEnter your option : "))

if option == 2:
	print("Your application is closed")
	exit(0)

elif option == 1:
	people = int(input("\nEnter number of Tickets you want : "))
	name1 = []
	age1 = []
	sex1 = []
for p in range(people):
	name = str(input("\nName : "))
	name1.append(name)
	age  = int(input("\nAge  : "))
	age1.append(age)
	sex  = str(input("\nGender : "))
	sex1.append(sex)
else :
    x = 0
    print("\nTotal Ticket : ",people)

for p in range(1,people+1):
	print("Ticket : ",p)
	print("Name : ", name1[x])
	print("Age  : ", age1[x])
	print("Sex : ",sex1[x])
	x += 1
