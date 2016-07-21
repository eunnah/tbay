from tbay import User, Item, Bid, session

beyonce = User()
beyonce.username = "bknowles"
beyonce.password = "uhohuhohuhohohnana"
session.add(beyonce)
session.commit()

jayz = User()
jayz.username = "jayz"
jayz.password = "99problems"
session.add(jayz)
session.commit()

crown = Item()
crown.name = "crown"
crown.description = "a beautiful crown"
session.add(crown)
session.commit()

shoe = Item()
shoe.name = "shoe"
shoe.description = "a beautiful golden shoe"
session.add(shoe)
session.commit()

user = session.query(User).first()
user.username = "solange"
session.commit()

item = session.query(Item).first()
item.name = "piggybank"
session.commit()

item = session.query(Item).get(2)
item.name = "toothbrush"
session.commit()

# do you have to commit one at a time? http://stackoverflow.com/questions/974596/what-is-a-database-transaction/974611#974611

# Returns a list of all of the user objects
# Note that user objects won't display very prettily by default -
# you'll see their type (User) and their internal identifiers.
print(session.query(User).all()) # Returns a list of all of the user objects

# Returns the first user
print(session.query(User).first())

# Returns the first item
print(session.query(Item).first())

# Finds the user with the primary key equal to 1
print(session.query(User).get(1))

# Returns a list of all of the usernames in ascending order
print(session.query(User.username).order_by(User.username).all())

# Returns a list of all of the items
print(session.query(Item.name).order_by(Item.name).all())


session.query(User).delete()
session.commit()

session.query(Item).delete()
session.commit()
