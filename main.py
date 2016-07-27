from tbay import User, Item, Bid, session

beyonce = User()
beyonce.username = "bknowles"
beyonce.password = "uhohuhohuhohohnana"
beyonce.id = "78"
session.add(beyonce)
session.commit()

jayz = User()
jayz.username = "jayz"
jayz.password = "99problems"
jayz.id = "56"
session.add(jayz)
session.commit()

solange = User()
solange.username = "solange"
solange.password = "sister"
solange.id = "1234"
session.add(solange)
session.commit()

crown = Item()
crown.name = "crown"
crown.description = "a beautiful crown"
crown.seller_id = solange.id
session.add(crown)
session.commit()

baseball = Item()
baseball.name = "baseball"
baseball.description = "a beautiful golden baseball"
baseball.seller_id = solange.id
session.add(baseball)
session.commit()

jayzbid = Bid()
jayzbid.price = 3
jayzbid.bidder_id = jayz.id
jayzbid.bidded_item = baseball.id
session.add(jayzbid)
session.commit()

beyoncebid = Bid()
beyoncebid.price = 5
beyoncebid.bidder_id = beyonce.id
beyoncebid.bidded_item = baseball.id
session.add(beyoncebid)
session.commit()

solange.auctioned_items.append = baseball 
jayz.bids_made.append = jayzbid
beyonce.bids_made.append = beyoncebid
baseball.bids_received.append(beyoncebid)
baseball.bids_received.append(jayzbid)
session.commit()

#Perform a query to find out which user placed the highest bid
if beyoncebid.price > jayzbid.price:
    print("Beyonce wins the item!")
elif beyoncebid.price == jayzbid.price:
    print("It's a tie!")
else:
    print("Jayz wins the item!")
    
session.commit()

# do you have to commit one at a time? http://stackoverflow.com/questions/974596/what-is-a-database-transaction/974611#974611

# Returns a list of all of the user objects
# Note that user objects won't display very prettily by default -
# you'll see their type (User) and their internal identifiers.
#print(session.query(User).all()) # Returns a list of all of the user objects

# Returns the first user
#print(session.query(User).first())

# Returns the first item
#print(session.query(Item).first())

# Finds the user with the primary key equal to 1
#print(session.query(User).get(1))

# Returns a list of all of the usernames in ascending order
#print(session.query(User.username).order_by(User.username).all())

# Returns a list of all of the items
#print(session.query(Item.name).order_by(Item.name).all())

