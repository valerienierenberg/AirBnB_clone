#!/usr/bin/python3
""" This module contains a class HBNBCommand that inherits from CMD
    and contains the entry point of the command interpreter """

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program
        """
        sys.exit(101)

    def do_EOF(self, arg):
        """ EOF command to exit the program
        """
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
