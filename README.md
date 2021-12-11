# EliteD
EliteD is a package to make database usage easier!
Create database easily and read and update them.\n
PyPi Page: https://pypi.org/project/EliteD/

### Installing
To install the package you just need to execute the following in your command line:

    pip3 install EliteD


## Using the package
This is how you create and setup a Database
 ```py
 import EliteD #importing the package
database = EliteD.create_database(name="user.db", path="/path/to/db")
database.create_table(name="test", columns=[{"type": int, "name": "test"}]) 
```
The second line would create the database "user.db" at the given path
The last line creates the table "test" in the database with the column "test" with integer as values. You can add as many columns as you want

If you already have a database, you can open the database like this: 
```py
import EliteD #import the module
database = EliteD.Database("/path/to/db") #Opens the database
```
If you need to delete a created table, you can do it like this:
```py
import EliteD
database = EliteD.Database(path="/path/to/db")
database.delete_table("name of the table")
```

### Writing values in a database
To add new values, you can use the `insert_value` method:
```py
import EliteD
database = EliteD.Database(path="/path/to/db")
database.insert_value(table="test", values=("001", "bread"))
```
This would insert the values `001` and `bread` in the table `test`.

### Reading, deleting and changing values of a database
To read a value of a database, you can use the `read_value` method:
```py
import EliteD
database = EliteD.Database(path="/path/to/db")
read = database.read_value(table="test", values=["test"], conditions={"test": 0})
print(read)
```
`values` is the row you want to read from the table. You can give multiple values. To read out all values, you can use the `EliteD.AllValues()` class. Conditions can be specified when you only want to read out the values when a row (`test` in this case)  has the specified value (`0` in this case).

To delete database values you can use the `delete_value` method:
```py
import EliteD
database = EliteD.Database(path="/path/to/db")
database.delete_value(table="test", row="trees", new_value=2, conditions={"floof": 1})
```
This would delete every value of the row `trees` from the table `test` if the value of `floof` is `1`

To change database values, you can use `update_value` method:
```py
import EliteD
database = EliteD.Database(path="/path/to/db")
database.update_value(table="test", row="roaw", new_value=2, conditions={"roawaaa": 1})
```
This would change every value of the row `roaw` from the table `test` to `2` if the value of `roawaaa` is `1`
