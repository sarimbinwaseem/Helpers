import vobject

ORGANIZATION = "ORG"

newcontactfile = ""
mainloop = True
while mainloop:
	contact = vobject.vCard()
	contact.add("n")
	contact.add("fn")
	contact.add("org")
	contact.add("tel")

	name = str(input("Name: "))

	if name == "quit":
		mainloop = False
		continue

	if " " not in name:
		name += f" ({ORGANIZATION})"


	numberFlag = True
	while numberFlag:
		number = str(input("Number: "))
		if len(number) != 13 and number != "quit":
			print("Length of number is not correct. AGAIN!!!")
			continue
		else:
			numberFlag = False

	if number == "quit":
		mainloop = False
		continue

	# family is last name (I think)
	contact.n.value = vobject.vcard.Name(family = "", given = name)
	contact.fn.value = name
	contact.tel.value = number
	contact.org.value = [ORGANIZATION]

	newcontactfile += contact.serialize()

print(newcontactfile)

with open("newcontacts.vcf", "w") as d:
	d.write(newcontactfile)
