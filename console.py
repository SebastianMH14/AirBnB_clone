#!/usr/bin/python3
"""print prompt"""
"""environ cmd"""
"""print Quit command to exit the program whit help quit NO FUNCIONA AUN"""


import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb): "
    """Quit command to exit the program"""
    def do_quit(self, args):

        return True


    def do_EOF(Self, args):

        return True


    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
