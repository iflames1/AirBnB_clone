#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program \n"""
        return True

    def do_EOF(self, arg):
        """To exit the program using EOF \n"""
        return True

    def emptyine(self):
        """Do nothing on empty line"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')


if __name__ == "__main__":
    HBNBCommand().cmdloop()
