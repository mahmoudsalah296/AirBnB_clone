#!/usr/bin/python3
"""
    a module for the console of the program
    from which we can update, delete, add and show users
"""
import cmd
from models.base_model import BaseModel
from models import storage


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
