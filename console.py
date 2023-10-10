#!/usr/bin/python3
"""
    a module for the console of the program
    from which we can update, delete, add and show users
"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
