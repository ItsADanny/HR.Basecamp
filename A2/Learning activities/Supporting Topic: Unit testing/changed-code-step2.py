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


def test_addcontact():
    add_contact('John Doe', '06876543210', 'john@hotemail.com')
    assert len(contacts) == 1 or contacts[0]['name'] == 'John Doe'


def test_searchcontact():
    add_contact('John Doe', '06876543210', 'john@hotemail.com')
    search_results = search_by_name("John")
    assert len(search_results) >= 1


def test_deletecontact():
    add_contact('John Doe', '06876543210', 'john@hotemail.com')
    delete_contact("John Doe")
    assert len(contacts) == 0
