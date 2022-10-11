#!/usr/bin/python3
"""The `cmd` module.
It defines one class, `HBNBCommand(),
which sub-classes the `Cmd()` class.`
"""

import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class inheriting the Cmd class
    """
    prompt = "(hbnb)"

    def do_help(self, arg):
        """parses argument into superclass help function
        to get information about the argument.
        """
        return super().do_help(arg)

    def do_quit(self, argument):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, argument):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Neglects an empty line"""
        return

    def do_create(self, argument):
        """create Creates new instance of class, saves it and prints the id
        """
        args = argument.split()
        if self.ValidArgs(args, False, False):
            created_obj = storage.classes()[args[0]]()
            created_obj.save()
            print(created_obj.id)

    def do_show(self, argument):
        """show Prints the string representation of an instance
        based on the class name and id
        """
        args = argument.split()
        if self.ValidArgs(args):
            key = args[0] + "." + args[1]
            print(storage.all()[key])

    def do_destroy(self, argument):
        """destroy Destroys an instance of class
        Updates the json file
        """
        args = argument.split()
        if self.ValidArgs(args):
            key = args[0] + "." + args[1]
            del storage.all()[key]
            storage.save()

    def do_all(self, argument):
        """all prints all string repr of all instances based or not on the
        class name
        """
        args = argument.split()
        if len(args) == 0:
            print([str(value) for key, value in storage.all().items()])
        elif args[0] in storage.classes():
            print(
                [str(value) for key, value in storage.all().items()
                    if type(value).__name__ == args[0]])
        else:
            print("** class doesn't exist **")

    def do_update(self, argument):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        (save the change into the JSON file)
        """
        args = argument.split()
        if self.ValidArgs(args):
            if len(args) == 0:
                print("** class name missing **")
                return
            elif len(args) == 1:
                print("** instance id missing **")
                return
            elif len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return
            elif args[0] not in storage.classes():
                print("** class doesn't exist **")
                return
            key = args[0] + '.' + args[1]
            obj = storage.all()[key]
            args[3] = args[3].strip('"')
            if args[3].isdigit():
                args[3] = float(args[3])
                if args[3].is_integer():
                    args[3] = int(args[3])
                else:
                    args[3]
            setattr(obj, args[2], args[3])
            storage.save()

    def ValidArgs(self, args, valid_id=True, exist_inst=True):
        """Validates the arguments to be passed to our console
        """
        if len(args) < 1:
            print("** class name missing **")
            return False
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return False
        if len(args) < 2 and valid_id:
            print("** instance id missing **")
            return False
        if exist_inst and args[0] + "." + args[1] not in storage.all():
            print("** no instance found **")
            return False
        return True


console = HBNBCommand()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
