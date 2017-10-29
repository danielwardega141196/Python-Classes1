from Person_Class import Person

class Trainee(Person):
    """Class containing information about particular Trainee"""

    def __init__(self, name, lastname, birth_year, guardian, scholarship):

        """Initialize a new Trainee object

           The Trainee inherits from the class 'Person'

         Args:
            name(str): The first name of a person. Only letters should be included.
            lastname (str): The last name of a person. Only letters should be included.
            birth_year (int): The birth year of a person. It must be int thereabout 1900.
            guardian (str): The name of the Trainee guardian. Only letters should be included.
            scholarship : Decision of awarding the scholarship. It must be True or False

        Raises:
            ValueError: if one of the following conditions are not met:
            1. name, lastname, guardian  doesn't consist of only letters.
            2. birth_year isn't int or is less than 1900
            3. if the value of scholarship isn't True or False
        """

        super(Trainee, self).__init__(name, lastname, birth_year)

        self._guardian = None
        self._scholarship = None

        self.guardian = guardian
        self.scholarship = scholarship

    @property
    def guardian(self):
        """The name of the Trainee guardian"""
        return self._guardian

    @guardian.setter
    def guardian(self, new_guardian):
        """Set the name of the Trainee guardian

        Args :
            new_guardian (str): new name of the Trainee guardian. Only letters should be included.
        Raises:
            ValueError: if signs except of only letters are also included
        Notes:
            If the value of new_guardian is correct, it will be assigned to the name of the Trainee guardian
        """

        if (str(new_guardian)).isalpha() == False:
            raise ValueError("A correct name of the Trainee guardian must contain only letters.")

        self._guardian = new_guardian

    @property
    def scholarship(self):
        """Indicates whether the scholarship awarded"""
        if self._scholarship == True:
            return "Przyznano stypendium"
        else:
            return "Nie przyznano stypendium"

    @scholarship.setter
    def scholarship(self, new_scholarship):

        """Decision to award a scholarship
        Args:
            new_scholarship (True or False) : Indicates whether the scholarship awarded. It must be True or False
        Raises:
            ValueError: if new_scholarship isn't True or False
        Notes:
            If the value of new_scholarship is correct, it will be assigned to the decision of awarding the scholarship.
        """

        if (new_scholarship != True and new_scholarship != False):
            raise ValueError('Value must be True or False')

        self._scholarship = new_scholarship

    @property
    def allsalary(self):
        """All monthly earnings"""
        if self._scholarship == True:
            return 800  # It could be any value becauce for all Trainee is the same
        else:
            return 0

    def __str__(self):
        """Convert this Trainee object to string."""
        return "Praktykant: \nImię: {0.name}\nNazwisko: {0.lastname}\nRok Urodzenia: {0.birth_year}\nOpiekun: {0.guardian}\nStypendium: {0.scholarship}\nPobory Miesieczne: {0.allsalary} zł".format(
            self)

    def __repr__(self):
        """Return textual representation of this Trainee object."""
        return str(self)