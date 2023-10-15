# AirBnB clone - The console

<p align="center">
  <img src="airBnB.png" alt="airBnB" width="40%">
</p>


## Welcome to the AirBnB clone project

### First step: a command interpreter to manage our AirBnB objects.
This is the first step towards building our first full web application: the **AirBnB clone**.


- First we created a `BaseModel` class that defines all common attributes/methods for other classes, and takes care of
the initialization, serialization and deserialization of your future instances.

- We created a simple flow of serialization/deserialization: ```Instance <-> Dictionary <-> JSON string <-> file```.

- Then we created all classes used for AirBnB (`User`, `State`, `City`, `Place`, …) that inherit from `BaseModel`.

- We used json files as our storage engine because until now we don't have a GUI, we used the console / command
interpreter (`cmd` module) to manipulate our storage engine.

### How to start it

- First clone the repository to your local machine.
  ```bash
  git clone https://github.com/mahmoudsalah296/AirBnB_clone.git
  ```

- Run the `console.py` file
 (*note: you have to be in the same directory as the `console.py` file and have python3 installed*)
  ```bash
  python3 console.py
  ```

- Now you can use the console to *create*, *update*, *destroy*, *show*, and all other CRUD operations on our objects.

- Every time you create an object, it will be saved in a json file in the models directory called `file.json`

- Available commands:  
  - **create**: creates an object of the class name.
     ```bash
     $ create <class name>
     ```
  - **show**: shows the object of the class name with the id.
     ```bash
    # There are 2 ways to do that
    
     $ show <class name> <class id>
     $ <class name>.show(<class id>)
     ```
  - **destroy**: destroys the object of the class name with the id.
     ```bash
     # There are 2 ways to do that
    
     $ destroy <class name> <clas id>
     $ <class name>.destroy(<class id>)
     ```
  - **all** - shows all objects of the class name.
     ```bash
     # There are many ways to do that
     
     $ all  # If you want show all instances.
     $ all <class name>
     $ <class name>.all()
     ```
  - **update**: Updates an instance based on the class name and `id` by adding or updating attribute.
     ```bash
     # There are many ways to do that
    
     $ update <class name> <class id> <attribute name> "<attribute value>"
     $ <class name>.update(<id>, <attribute name>, <attribute value>)
     $ <class name>.update(<id>, <dictionary representation>)
     ```
  - **count** - retrieve the number of instances of a class.
    ```bash
     <class name>.count()
    ```
  - **quit** or **EOF** - exits the console  
  
  - **ls** - lists all classes names  
  
  - **help** or **?** - shows the help message  
