#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand class"""

    def setUp(self):
        """Set up for the tests"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Tear down for the tests"""
        storage.reload()

    def test_help(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = f.getvalue()
        self.assertIsNotNone(output)

    def test_all(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            output = f.getvalue().strip()
        self.assertIn(user_id, output)

    def test_all_v2(self):
        """Test all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.all()")
            output = f.getvalue().strip()
        self.assertIn(user_id, output)

    def test_all_invalid_class(self):
        """Test all command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all NonExistentClass")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_all_invalid_class_v2(self):
        """Test all command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("NonExistentClass.all()")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_create(self):
        """Test create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertTrue(len(user_id) > 0)

    def test_create_missing_class(self):
        """Test create command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class(self):
        """Test create command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create NonExistentClass")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show(self):
        """Test show command"""
        # Create a User instance first
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn(user_id, output)

    def test_show_v2(self):
        """Test show command"""
        # Create a User instance first
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"User.show({user_id})")
            output = f.getvalue().strip()
        self.assertIn(user_id, output)

    def test_show_missing_class(self):
        """Test show command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_show_missing_id(self):
        """Test show command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_missing_id_v2(self):
        """Test show command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show()")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_invalid_class(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show NonExistentClass 1234")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_invalid_class_v2(self):
        """Test show command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("NonExistentClass.show(1234)")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_no_instance(self):
        """Test show command with non-existing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User 1234")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_show_no_instance_v2(self):
        """Test show command with non-existing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.show(1234)")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        """Test destroy command"""
        # Create a User instance first
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy User {user_id}")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        # Try to show the destroyed instance
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_v2(self):
        """Test destroy command"""
        # Create a User instance first
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"destroy User {user_id}")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        # Try to show the destroyed instance
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"User.show({user_id})")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_missing_class(self):
        """Test destroy command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_destroy_missing_id(self):
        """Test destroy command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_missing_id_v2(self):
        """Test destroy command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.destroy()")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_destroy_invalid_class(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy NonExistentClass 1234")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_invalid_class_v2(self):
        """Test destroy command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("NonExistentClass.destroy('1234')")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_no_instance(self):
        """Test destroy command with non-existing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User 1234")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_destroy_no_instance_v2(self):
        """Test destroy command with non-existing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.destroy('1234')")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_count(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id1 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id2 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count User")
            output = f.getvalue().strip()
        count = sum(1 for key in storage.all().keys()
                    if key.startswith("User" + "."))
        self.assertEqual(output, str(count))

    def test_count_v2(self):
        """Test count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id1 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id2 = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User.count()")
            output = f.getvalue().strip()
        count = sum(1 for key in storage.all().keys()
                    if key.startswith("User" + "."))
        self.assertEqual(output, str(count))

    def test_count_missing_class(self):
        """Test count command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_count_invalid_class(self):
        """Test count command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count NonExistentClass")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_count_invalid_class_v2(self):
        """Test count command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("NonExistentClass.count()")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'update User {user_id} first_name "John"')
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn("'first_name': 'John'", output)

    def test_update_integer(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'update User {user_id} age 7')
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn("'age': 7", output)

    def test_update_v2(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.update("{}", "first_name", "John")'
                                .format(user_id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn("'first_name': 'John'", output)

    def test_update_integer_v2(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.update("{}", "age", 30)'
                                .format(user_id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn("'age': 30", output)

    def test_update_dict(self):
        """Test update command with a dictionary"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.update("{}", '
                                '{{"first_name": "John", "age": 30}})'
                                .format(user_id))
            output = f.getvalue().strip()
        self.assertEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn("'first_name': 'John'", output)
        self.assertIn("'age': 30", output)

    def test_update_missing_class(self):
        """Test update command with missing class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class name missing **")

    def test_update_invalid_class(self):
        """Test update command with invalid class name"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update NonExistentClass 1234")
            output = f.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_missing_id(self):
        """Test update command with missing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            output = f.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_update_no_instance(self):
        """Test update command with non-existing instance id"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 1234")
            output = f.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_update_missing_attr_name(self):
        """Test update command with missing attribute name"""
        # create a User
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update User {user_id}")
            output = f.getvalue().strip()
        self.assertEqual(output, "** attribute name missing **")

    """This test was intentional made to fail."""
    def test_update_missing_value(self):
        """Test update command with missing value"""
        # create a User
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"update User {user_id} first_name")
            output = f.getvalue().strip()
        self.assertNotEqual(output, "** value missing **")


if __name__ == "__main__":
    unittest.main()
