#!/usr/bin/python3
"""creating a console command interpreter"""

import cmd
import shlex
from models import storage
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        "Quit command to exit the program"
        return True

    def do_EOF(Self, args):
        "End Of File"
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if args:
            args = shlex.split(args)
            try:
                new_object = globals()[args[0]]()
                new_object.save()
                print(new_object.id)
            except:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """ Prints the string representation of
        an instance based on the class name and id"""
        if args:
            args = shlex.split(args)
            if len(args) < 2:
                print("** instance id missing **")
            elif args[0] not in globals():
                print("** class doesn't exist **")
            else:
                show = storage.all()
                key = args[0]+"."+args[1]
                if key in show:
                    print(show[key])
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        """Deletes an instance based
        on the class name and id"""
        if args:
            args = shlex.split(args)
            if len(args) < 2:
                print("** instance id missing **")
            elif args[0] not in globals():
                print("** class doesn't exist **")
            else:
                key = args[0]+"."+args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class name missing **")

    def do_all(self, args):
        """ Prints all string representation of all
        instances based or not on the class name."""
        new_list = []
        if args:
            args = shlex.split(args)
            if args[0] in globals():
                for k, v in storage.all().items():
                    if v.__class__.__name__ == args[0]:
                        new_list.append(v.__str__())
                    print(new_list)
            else:
                print("** class doesn't exist **")
        else:
            for a in storage.all().values():
                new_list.append(a.__str__())
            print(new_list)

    def do_update(self, args):
        """Updates an instance based on the class
        name and id by adding or updating attribute"""
        if args:
            args = shlex.split(args)
            if args[0] not in globals():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            elif args[0]+'.'+args[1] not in storage.all():
                print("** no instance found **")
            else:
                key = args[0] + '.' + args[1]
                new_obj = storage.all()[key]
                new_obj.__dict__[args[2]] = args[3]
                new_obj.save()
        else:
            print("** class name missing **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
