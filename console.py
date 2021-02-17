#!/usr/bin/python3
""" This module contains a class HBNBCommand that inherits from CMD
    and contains the entry point of the command interpreter """

import cmd
import sys
import shlex
from models import storage
from models.engine.file_storage import FileStorage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User

classes = {"BaseModel": BaseModel, "City": City, "Place": Place, "Amenity":
           Amenity, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand class
    """
    prompt = '(hbnb) '
    count = 0

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
        ex.  $ create BaseModel
        """
        self.non_interactive_mode()
        if not arg:
            print("** class name missing **")
        elif arg in classes:
            for key, value in classes.items():
                if key == arg:  # find correct class name
                    newobj = classes[key]()  # create instance of correct class
            storage.save()  # saves it (to the JSON file)
            print(newobj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """show method - Prints the string representation of
        an instance based on the class name and id
        ex.  $ show BaseModel 1234-1234-1234
        """
        #  arg_array:
        #  [0] - class name
        #  [1] - instance id
        self.non_interactive_mode()
        arg_array = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif arg_array[0] not in classes:
            print("** class doesn't exist **")
        elif arg_array[0] in classes and len(arg_array) == 1:
            print("** instance id missing **")
        elif len(arg_array) == 2:
            key = "{}.{}".format(arg_array[0], arg_array[1])
            local_objects = storage.all()
            if key not in local_objects:
                print("** no instance found **")
            else:
                print(local_objects[key])

    def do_destroy(self, arg):
        """destroy method - Deletes an instance based on the class name and id
        (change is saved into the JSON file)
        ex.  $ destroy BaseModel 1234-1234-1234
        """
        #  arg_array:
        #  [0] - class name
        #  [1] - instance id
        self.non_interactive_mode()
        arg_array = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif arg_array[0] not in classes:
            print("** class doesn't exist **")
        elif arg_array[0] in classes and len(arg_array) == 1:
            print("** instance id missing **")
        elif len(arg_array) == 2:
            key = "{}.{}".format(arg_array[0], arg_array[1])
            local_objects = storage.all()
            if key not in local_objects:
                print("** no instance found **")
            else:
                del(local_objects[key])
                storage.save()

    def do_all(self, arg):
        """all method - Prints all string representation of all instances
        based or not on the class name.
        ex.  $ all
             $ all BaseModel
        """
        #  arg_array:
        #  [0] - class name
        #  [1] - instance id
        self.non_interactive_mode()
        arg_array = arg.split(" ")
        result_list = []
        local_objects = storage.all()
        if not arg or (arg and arg_array[0] in classes):
            for each in local_objects:
                result = local_objects[each].__str__()
                result_list.append(result)
                print(result_list)
        elif arg and arg_array[0] not in classes:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """update method - Updates an instance based on the class name
        and id by adding or updating attribute.
        Saves the change into the JSON file.
        ex. $ update BaseModel <valid id> email "aibnb@holbertonschool.com" """
        #  arg_array:
        #  [0] - class name
        #  [1] - instance id
        #  [2] - attribute name
        #  [3] - attribute value
        self.non_interactive_mode()
        arg_array = shlex.split(arg)
        if not arg:
            print("** class name missing **")
            return
        elif arg_array[0] not in classes:
            print("** class doesn't exist **")
            return
        elif arg_array[0] in classes and len(arg_array) == 1:
            print("** instance id missing **")
            return
        elif len(arg_array) == 2:
            key = "{}.{}".format(arg_array[0], arg_array[1])
            local_objects = storage.all()
            if key not in local_objects:
                print("** no instance found **")
                return
            elif len(arg_array) == 2 and key in local_objects:
                print("** attribute name missing **")
                return
        elif len(arg_array) == 3:
            print("** value missing **")
            return
        key = "{}.{}".format(arg_array[0], arg_array[1])
        local_objects = storage.all()
#        str(arg_array[3]).replace("\\", "")
        setattr(local_objects[key], arg_array[2], arg_array[3])
        storage.save()

    @staticmethod
    def count(arg):
        """ count method to retrieve the number of instances of a class """
        local_objects = storage.all()
        for each, obj in local_objects.items():
            if each == arg:
                HBNBCommand.count += 1
                print(HBNBCommand.count)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
