#!/usr/bin/python3
"""
    a module for the console of the program
    from which we can update, delete, add and show users
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """command class"""

    prompt = "(hbnb) "

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

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        # $ destroy BaseModel 1234-1234-1234
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return

        # Unpacking all storage date to classes name.
        all_objects = storage.all()  # all keys
        all_classes = []  # # contains all classes name

        for key in all_objects.keys():
            class_name, class_id = key.split(".")
            all_classes.append(class_name)

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
