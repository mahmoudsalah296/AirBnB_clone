# AirBnB clone - The console

<p align="center">
  <img src="airBnB.png" alt="airBnB" width="40%">
</p>


### Welcome to the AirBnB clone project!

#### First step: a command interpreter to manage our AirBnB objects.
This is the first step towards building our first full web application: the **AirBnB clone**.


- first we created a BaseModel class that defines all common attributes/methods for other classes, and takes care of the initialization, serialization and deserialization of your future instances

- we created a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file

- then we created all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel

- in this first stip we used json files as our storage engine

- because until now we don't have a GUI, we used the console / command interpreter (cmd module) to manipulate our storage engine

#### How to start it

- first clone the repository to your local machine

- then run the console.py file (note that: you have to be in the same directory as the console.py file and have python3 installed)

- now you can use the console to create, update, destroy, show, and all other CRUD operations on our objects
  exaplme: create User, create State, show User, destroy User, update User, all User, all State, etc...

- every time you create an object, it will be saved in a json file in the models directory called file.json

- available commands:  
  1.**create** {class name} - creates an object of the class name
  2. **show** {class name} {id} - shows the object of the class name with the id
  3. **destroy** {class name} {id} - destroys the object of the class name with the id
  4. **all** {class name} - shows all objects of the class name
  5. **update** {class name} {id} {attribute name} "{attribute value}"
      updates the attribute of the object of the class name with the id
  6. **quit** or **EOF** - exits the console
  7. **ls** - lists all classes names
  8. **help** or **?** - shows the help message
