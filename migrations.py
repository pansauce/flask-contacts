from models import db, Contact
from faker import Factory
import csv

fake = Factory.create()

# Reload tables
db.drop_all()
db.create_all()
# Make 100 fake contacts
# for num in range(100):
#     fullname = fake.name().split()
#     name = fullname[0]
#     surname = ' '.join(fullname[1:])
#     email = fake.email()
#     phone = fake.phone_number()
#     # Save in database
#     contact = Contact(name=name, surname=surname, email=email, phone=phone)
#     db.session.add(contact)
with open('static/csv/contacts.csv') as f:
    contacts = csv.reader(f)
    for contact in contacts:
        company = contact[1]
        new_contact = Contact(fname=contact[2], lname=contact[3], title=contact[4], email=contact[5], phone=contact[6],
                              company=company.title())
        print("Adding: {0} {1}".format(contact[2], contact[3]))
        db.session.add(new_contact)
db.session.commit()
