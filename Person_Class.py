# coding: utf-8
class Person(object):
    """ Class containing information about particular employee """
    def __init__(self, name, lastname, birth_year):

        """Initialize a new Person object.
        Args:

            name(str): The first name of a person. Only letters should be included.

            lastname (str): The last name of a person. Only letters should be included.

            birth_year (int): The birth year of a person. It must be int thereabout 1900.
        Raises:

            ValueError: if one of the following conditions are not met:

            1. name or lastname doesn't consist of only letters.

            2. birth_year isn't int or is less than 1900
        """

        self._name = None

        self._lastname = None

        self._birth_year = None

        self.name = name

        self.lastname = lastname

        self.birth_year = birth_year

    @property
    def name(self):

        """The first name of a person"""

        return self._name

    @name.setter
    def name(self, new_name):

        """Set first name of a person


        Args :

            new_name (str): new first name. Only letters should be included.

        Raises :

            ValueError: if signs except of only letters are also included

        Notes:

            The name will be automatically capitalize

        """

        if (str(new_name)).isalpha() == False:
            raise ValueError("A correct first name must contain only letters.")

        self._name = new_name.capitalize()

    @property
    def lastname(self):
        """The last name of a person"""
        return self._lastname

    @lastname.setter
    def lastname(self, new_lastname):
        """Set the last name of a person

        Args :
            new_lastname (str): new last name. Only letters should be included.
        Raises:
            ValueError: if signs except of only letters are also included
        Notes:
            The lastname will be automatically capitalize
        """

        if (str(new_lastname)).isalpha() == False:
            raise ValueError("A correct last name must contain only letters.")

        self._lastname = new_lastname.capitalize()

    @property
    def birth_year(self):
        """Birth year of a person """
        return self._birth_year

    @birth_year.setter
    def birth_year(self, new_birth_year):
        """Set the birth year of a person

        Args:
            new_birth_year (int): new birth year. It must be int thereabout 1900.
        Raises:
            ValueError: if new_birth_year isn't int or the date is too early
        Notes:
            If the value of new_birth_year is correct, it will be assigned to birth year.

        """
        if (str(new_birth_year)).isdigit() == False or int(new_birth_year) < 1900:
            raise ValueError("A correct birth year must be int greater than 1900.")

        self._birth_year = new_birth_year




