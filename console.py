#!/usr/bin/python3
"""creating a console command interpreter"""

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
