#!/usr/bin/python3
""" This module contains a class HBNBCommand that inherits from CMD
    and contains the entry point of the command interpreter """

import cmd
import sys
# from models import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        sys.exit(101)

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        self.non_interactive_mode()
        return True

    @staticmethod
    def non_interactive_mode():
        """ Checks if interactive or noninteractive mode """
        if sys.stdin.isatty() is False:
            print("")

    def emptyline(self):
        """ an empty line + ENTER does not execute anything """
        self.non_interactive_mode()
        pass

    def do_help(self, *args):
        """ help method """
        self.non_interactive_mode()
        cmd.Cmd.do_help(self, *args)

    def do_create(self, arg):
        """create method - Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        myobj = BaseModel()
        myobj.save()
        print(myobj.id)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
