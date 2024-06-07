contacts = []

def add_contact(name, phone_number, email):
    contact = {
        'name': name,
        'phone_number': phone_number,
        'email': email
    }
    contacts.append(contact)

def search_by_name(name):
    return list(filter(lambda c: name.lower() in c['name'].lower(), contacts))

def delete_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)

def test():
    # Test adding a contact
    add_contact('John Doe', '06876543210', 'john@hotemail.com')
    # Let's check if the function works correctly
    if len(contacts) != 1 or contacts[0]['name']!='John Doe':
    	print('Test: ERROR in add_contact()')

    # Test searching contacts
    search_results = search_by_name("John")
    # Let's check if the function works correctly
    if len(search_results) < 1:
    	print('Test: ERROR in search_by_name()')

    # Test deleting a contact
    delete_contact("John Doe")
    # CHECK HAS BEEN ADDED
    if len(contacts) != 0:
        print('Test: ERROR in delete_contact()')

    print("All tests are executed.")

test()
