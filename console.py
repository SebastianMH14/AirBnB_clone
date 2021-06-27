#!/usr/bin/python3
"""print prompt"""
"""environ cmd"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Interprete de comandos"""
    prompt = "(hbnb): "
    def do_quit(self, args):

        return True


    def do_EOF(Self, args):

        return True


    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
