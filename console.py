#!/usr/bin/python3
"""
    a module for the console of the program
    from which we can update, delete, add and show users
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
        else:
            try:
                new_instance = globals()[class_name]()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id"""

        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.unpacking_storage():
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
            if flag is False:
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
        # print(args)

        # $ all
        if not arg:
            for value in storage.all().values():
                all_instances.append(str(value))
            print(all_instances)
            return

        # Checks if user entered '<class name>.all()'
        if len(args) == 1:
            class_name = arg
        else:
            class_name = args[1]

        # Unpacking all storage date to classes name.
        all_classes = self.unpacking_storage()

        if class_name not in all_classes:
            print("** class doesn't exist **")
            return

        # $ all BaseModel
        for key, value in storage.all().items():
            if key.startswith(f"{class_name}."):
                all_instances.append(str(value))

        if all_instances:
            print(all_instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        # update <class name> <id> <attribute name> "<attribute value>"
        args = arg.split()
        # print(*args)

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

    def do_ls(self, arg):
        """Display the storage instances name"""
        print(self.unpacking_storage())

    def default(self, line):
        """Method called on an input line when the command prefix is not recognized.
        If this method is not overridden, it prints an error message and returns.
        """
        args = line.split(".")
        class_name = args[0]

        if len(args) >= 2 and args[1] == "all()":
            self.do_all(class_name)
        elif len(args) >= 2 and args[1] == "count()":
            print(self.unpacking_storage().count(class_name))
        elif len(args) >= 2 and (args[1].startswith("show(") or
                                 args[1].startswith("destroy(")):
            func_body = args[1].split('(')
            # print(func_body)
            class_id = func_body[1][1:-2]
            # print(class_id)
            if args[1].startswith("show("):
                self.do_show(f"{class_name} {class_id}")
            else:
                self.do_destroy(f"{class_name} {class_id}")
        elif len(args) >= 2 and args[1].startswith("update("):
            func_body = args[1].split(')')
            # print(func_body)
            func_content = func_body[0].split("(")
            # print(func_content)
            attributes_list = func_content[1].split(",")
            # print(attributes_list)

            class_id = attributes_list[0][1:-1]
            attribute_name = attributes_list[1][2:-1]
            attribute_value = attributes_list[2]
            # print(attribute_value)
            # print(type(attribute_value))
            try:
                attribute_value = int(attribute_value)
            except ValueError:
                attribute_value = attributes_list[2][2:-1]
            # print (type(attribute_value))
            # print(class_name, class_id, attribute_name, attribute_value)
            self.do_update(f"{class_name} {class_id} {attribute_name} {attribute_value}")
        else:
            print("*** Unknown syntax: {line}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
