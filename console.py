#!/usr/bin/python3
"""print prompt"""
"""environ cmd"""
"""print Quit command to exit the program whit help quit"""
"""emtyline whit enter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """command interpreter"""
    prompt = "(hbnb) "
    """Quit command to exit the program"""
    def do_quit(self, args):
        'Quit command to exit the program'
        return True


    def do_EOF(Self, args):
        'End Of File'
        return True


    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
