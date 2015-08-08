from store import db
import peewee
from contact import Contact
from group import Group

class GroupContact(db.get_base_model()):
    contact = peewee.ForeignKeyField(Contact)
    group = peewee.ForeignKeyField(Group)