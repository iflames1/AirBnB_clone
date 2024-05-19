#!/usr/bin/python3
"""
The `HBNBCommand` class is the main entry point for the command-line interface
(CLI) of the AirBnB clone project. It inherits from the `cmd.Cmd` class, which
provides a basic framework for building interactive command-line applications.

The class defines several methods that handle various commands that can be
executed from the CLI, such as `do_all`, `do_create`, `do_show`, `do_destroy`,
and `do_update`. These methods interact with the storage system to perform
CRUD (Create, Read, Update, Delete) operations on the different classes of
the AirBnB clone project.

The `default` method is used to handle any unrecognized commands, and it
attempts to match the command to a specific class and method using a regular
expression. If a match is found, the corresponding method is called with the
provided arguments.

The `do_count` method is used to count the number of instances of a specific
class that are stored in the storage system.

The `do_quit` and `do_EOF` methods are used to exit the CLI application.
"""

import cmd
import re
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNB Console entry
    """
    prompt = "(hbnb) "
    CLASSES = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def default(self, line: str) -> None:
        """
        The `default` method is used to handle any unrecognized commands, and
        it attempts to match the command to a specific class and method using
        a regular expression. If a match is found, the corresponding method is
        called with the provided arguments.

        Parameters:
            line (str): The command line input.

        Returns:
            None
        """
        method_mapping = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "create": self.do_create
        }
        match = re.match(r"(\w+)\.(\w+)\((.*)\)", line)
        if match:
            class_name, method_name, args = match.groups()
            args = args.strip('"\'')
            if class_name in self.CLASSES and method_name in method_mapping:
                method = method_mapping[method_name]
                method(f"{class_name} {args}".strip())
            else:
                print("** class doesn't exist **" if class_name not in
                      self.CLASSES else "*** Unknown syntax **")
        else:
            print("*** Unknown syntax:", line)

    def do_count(self, arg):
        """
        Counts the number of instances of a specific class that are stored in
        the storage system.
        Usage: count <class name>
            <class name>.count()

        Parameters:
            arg (str): The name of the class to count the instances of.

        Returns:
            None
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name in self.CLASSES:
            count = sum(1 for key in storage.all().keys()
                        if key.startswith(class_name + "."))
            print(count)
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Retrieves all instances of a specific class from the storage system
        and prints them as a list.
        Usage: all (optional: <class name>)

        Parameters:
            arg (str): The name of the class to retrieve instances of. If not
            provided, retrieves all instances from the storage system.

        Returns:
            None

        Raises:
            None
        """
        obj_list = []
        if arg:
            class_name = arg.split()[0]
            if class_name not in self.CLASSES:
                print("** class doesn't exist **")
                return
            obj_dict = storage.all()
            for key, value in obj_dict.items():
                if class_name == key.split('.')[0]:
                    obj_list.append(str(value))
        else:
            obj_dict = storage.all()
            for value in obj_dict.values():
                obj_list.append(str(value))
        print(obj_list)

    def do_create(self, arg):
        """
        Creates a new instance of a class and saves it to the storage system.
        Usage: create <class name>

        Parameters:
            arg (str): The name of the class to create an instance of.

        Returns:
            None

        Raises:
            None
        """
        if not arg:
            print("** class name missing **")
            return
        class_name = arg.split()[0]
        if class_name in self.CLASSES:
            new_instance = self.CLASSES[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Displays the details of an instance of a class.
        Usage: show <class name> <id>
        Parameters:
            arg (str): The name of the class followed by the instance ID
            separated by a space.

        Returns:
            None

        Raises:
            None
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = class_name + '.' + args[1].strip('"\'')
        obj_dict = storage.all()
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance of a class from storage.
        Usage: destroy <class name> <id>

        Parameters:
            arg (str): The name of the class followed by the instance ID
            separated by a space.

        Returns:
            None

        Raises:
            None
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = class_name + '.' + args[1].strip('"\'')
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        del obj_dict[key]
        storage.save()

    def do_update(self, arg):
        """
        Updates an attribute of an instance of a class in storage.

        Usage: update <class name> <id> <attribute name> "<attribute value>"

        Parameters:
            arg (str): The name of the class followed by the instance ID,
            attribute name, and new value separated by spaces.

        Returns:
            None

        Raises:
            ValueError: If there is an error parsing the argument string.
            ValueError: If the class name is missing.
            ValueError: If the instance ID is missing.
            ValueError: If the attribute name is missing.
            ValueError: If the value is missing.
            ValueError: If the class does not exist.
            ValueError: If no instance is found.
            ValueError: If the attribute does not exist.
            ValueError: If the value is of an invalid type.
        """
        try:
            args = shlex.split(arg)
        except ValueError:
            print("** value error **")
            return

        obj_dict = storage.all()
        re_quote = '"\''
        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            elif args[0] not in self.CLASSES:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif f"{args[0]}.{args[1].strip(re_quote)}" not in obj_dict:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            return

        class_name = args[0]
        obj_id = args[1].strip('"\'')
        obj_attr = args[2]
        obj_value = args[3].strip('"\'')

        obj_dict = storage.all()
        obj_key = f"{class_name}.{obj_id}"

        obj = obj_dict[obj_key]
        if hasattr(obj, obj_attr):
            attr_type = type(getattr(obj, obj_attr))
            try:
                obj_value = attr_type(obj_value)
            except ValueError:
                print("** invalid value type **")
                return
        else:
            try:
                obj_value = eval(obj_value)
            except (NameError, SyntaxError):
                pass

        setattr(obj, obj_attr, obj_value)
        storage.save()

    def do_quit(self, arg):
        """Quit command to exit the program \n"""
        return True

    def do_EOF(self, arg):
        """To exit the program using EOF \n"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
