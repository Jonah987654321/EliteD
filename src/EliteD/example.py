import EliteD #Importing the EliteD module

db = EliteD.Database("/home/pi/dc_bot/user.db") #Opens the exsisting table user.db at the given path

print(db.read_value("playerdata", [EliteD.AllValues()], {})) #Read out all values from the table "playerdata" without any condition
db.update_value("playerdata", "konto", 500, {"userid": 628638390203580426}) #Update the "konto" row in the "playerdata" table where the user id is the given
print(db.read_value("playerdata", [EliteD.AllValues()], {"userid": 0})) #Read out all values from the table "playerdata" with the userid 0

db2 = EliteD.create_database("user.db", "/home/pi/EliteD") #Creates the database "user.db" at the given path
db2.create_table("test", [{"type": int, "name": "test"}]) #Creates the table "test" in the database with the column "test" with integer as values
db2.delete_table("test") #Deletes the table "test"
