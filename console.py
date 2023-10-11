#!/usr/bin/python3
"""
    a module for the console of the program
    from which we can update, delete, add and show users
"""
import cmd
import os
import platform
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """command class"""

    prompt = "(hbnb) "

    def preloop(self):
        print("hello to our AirBnb clone")
        print("to clear the terminal press ctrl+l")

    def postloop(self):
        print("thank you for using our service, see you soon!")

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """exits the program"""
        return True

    def emptyline(self):
        """when user press enter with empty line"""
        # do nothing
        pass

    def do_create(self, class_name):
        """creates a new instance of BaseModel,
        saves it to json file,
        and prints the id"""
        if not class_name or class_name == "":
            print("** class name missing **")
        elif class_name not in ("BaseModel",):
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ("BaseModel",):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            flag = False
            all_obj = storage.all()
            for obj_id in all_obj.keys():
                if args[1] == obj_id.split(".")[1]:
                    print(all_obj[obj_id])
                    flag = True
                    break
            if flag == False:
                print("** no instance found **")

    def unpacking_storage(self):
        """Unpacking storage to classes name"""
        all_objects = storage.all()  # all keys
        all_classes = []  # contains all classes name

        for key in all_objects.keys():
            class_name, class_id = key.split(".")
            all_classes.append(class_name)

        return all_classes

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        # $ destroy BaseModel 1234-1234-1234
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        # Unpacking all storage date to classes name.
        all_classes = self.unpacking_storage()

        if args[0] not in all_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        args = arg.split()
        all_instances = []

        # $ all
        if not arg:
            for value in storage.all().values():
                all_instances.append(str(value))
            print(all_instances)
            return

        # Unpacking all storage date to classes name.
        all_classes = self.unpacking_storage()

        if args[0] not in all_classes:
            print("** class doesn't exist **")
            return

        # $ all BaseModel
        for key, value in storage.all().items():
            if key.startswith(f"{args[0]}."):
                all_instances.append(str(value))

        if all_instances:
            print(all_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        # update <class name> <id> <attribute name> "<attribute value>"
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        # Unpacking storage to classes name.
        all_classes = self.unpacking_storage()
        if args[0] not in all_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:  # if no id entered
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        # If user entered all arguments
        value_obj = all_objects[key]
        attr_name = args[2]
        attr_value = args[3]

        # Check if the attribute exists in the object's class definition
        # Or attribute name doesn't exist, add it to the object
        setattr(value_obj, attr_name, attr_value)
        storage.save()

    def do_clear(self, arg):
        """Clear the screen"""
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def do_ls(self, arg):
        """Display the storage instances name"""
        print(self.unpacking_storage())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
