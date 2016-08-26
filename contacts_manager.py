import contact

def main():
	contacts = []
	new_contact_first = raw_input("What is your first name?") 
	new_contact_last = raw_input("what is your last name?")
	new_contact_phone = raw_input("what is your phone number?")
	new_contact_email = raw_input("what is your email?")
	new_contact_birthday = raw_input("what is your birthday?")
	new_contact = contact.Contact(new_contact_first, new_contact_last, new_contact_phone, new_contact_email, new_contact_birthday)

	contacts.append(new_contact)

	for person in contacts:
		print person.first_name, person.last_name, person.email, person.birthday, person.phone_number

if __name__ == '__main__':
	main()