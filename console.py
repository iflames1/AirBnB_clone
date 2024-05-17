#!/usr/bin/python3

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    CLASSES = {"BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Review": Review}

    def do_all(self, arg):
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
        if not arg:
            print("** class doesn't exist **")
            return
        class_name = arg.split()[0]
        if class_name in self.CLASSES:
            new_instance = self.CLASSES[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
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
        key = class_name + '.' + args[1]
        obj_dict = storage.all()
        if key in obj_dict:
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
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
        key = class_name + '.' + args[1]
        obj_dict = storage.all()
        if key not in obj_dict:
            print("** no instance found **")
            return
        del obj_dict[key]
        storage.save()

    def do_update(self, arg):
        args = arg.split()
        if len(args) < 4:
            if len(args) == 0:
                print("** class name missing **")
            elif len(args) == 1:
                print("** instance id missing **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            return

        class_name = args[0]
        if class_name not in self.CLASSES:
            print("** class doesn't exist **")
            return
        obj_id = args[1]
        obj_attr = args[2]
        obj_value = args[3]

        obj_dict = storage.all()
        obj_key = f"{class_name}.{obj_id}"
        if obj_key not in obj_dict:
            print("** no instance found **")
            return

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
        return True

    def emptyine(self):
        """Do nothing on empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
