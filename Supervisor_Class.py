from Person_Class import Person

class Supervisor(Person):
    """Class containing information about particular Supervisor"""

    def __init__(self, name, lastname, birth_year, salary, allowance, sup_all, phone, mphone, room, section):
        super(Supervisor, self).__init__(name, lastname, birth_year)
        """Initialize a new Supervisor object

           The Supervisor inherits from the class 'Person'

         Args:
            name(str): The first name of a person. Only letters should be included.
            lastname (str): The last name of a person. Only letters should be included.
            birth_year (int): The birth year of a person. It must be int thereabout 1900.
            salary : basic salary of a supervisor. It should be float or int and must be greater than or equal to zero.
            allowance : the percentage of a premium. It should be float or int and must be greater than or equal to zero
            sup_all : Amount of the allowance steering. It should be float or int and must be greater than or equal to zero
            phone: The phone number of particular supervisor. Number should contains of digits or '+'+digits
            mphone: The mobile phone number of particular supervisor. Number should contains of digits or '+'+digits
            room : Supervisor worker room number.
            section : Name of the Supervisor's department


        Raises:
            ValueError: if one of the following conditions are not met:
            1. name, lastname doesn't consist of only letters.
            2. birth_year isn't int or is less than 1900
            3. if salary or allowance, sup_all isn't int or float or value <0
            4. if phone, mphone doesn't look like 'digits' or + 'digits
        """

        self._salary = None
        self._allowance = None
        self._sup_all = None
        self._phone = None
        self._mphone = None
        self._room = None
        self._section = None

        self.salary = salary
        self.allowance = allowance
        self.sup_all = sup_all
        self.phone = phone
        self.mphone = mphone
        self.room = room
        self.section = section

    @property
    def salary(self):
        """ Basic Salary of a supervisor"""
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        """Set the basic salary of a supervisor

        Args:
            new_salary (float or int) : new basic salary. It should be float or int and must be greater than or equal to zero
        Raises:
            ValueError: if new_salary isn't int or float or new_salary <0
        Notes:
            If the value of new_salary is correct, it will be assigned to basic salary.
        """

        if (type(new_salary) != int and type(new_salary) != float) or new_salary < 0:
            raise ValueError("Basic salary should be float or int and must be greater than or equal to zero")

        self._salary = round(new_salary, 2)

    @property
    def allowance(self):
        """The Percentage of a premium"""
        return self._allowance

    @allowance.setter
    def allowance(self, new_allowance):
        """Set the the percentage of a premium

        Args:
            new_allowance (float or int) : New percentage of a premium. It should be float or int and must be greater than or equal to zero
        Raises:
            ValueError: if new_allowance isn't int or float or new_allowance <0
        Notes:
            If the value of new_allowance is correct, it will be assigned to the percentage of a premium.
        """

        if (type(new_allowance) != int and type(new_allowance) != float) or new_allowance < 0:
            raise ValueError(
                "The percentage od a premium should be float or int and must be greater than or equal to zero")

        self._allowance = new_allowance

    @property
    def sup_all(self):
        """Amount of the allowance steering"""
        return self._sup_all

    @sup_all.setter
    def sup_all(self, new_sup_all):

        """Set the amount of the allowance steering
        Args:
            new_sup_all (float or int) : new amount of the allowance steering. It should be float or int and must be greater than or equal to zero
        Raises:
            ValueError: if new_sup_all isn't int or float or new_sup_all < 0
        Notes:
            If the value of new_sup_all is correct, it will be assigned to the amount of the allowance steering.
        """

        if (type(new_sup_all) != int and type(new_sup_all) != float) or new_sup_all < 0:
            raise ValueError(
                "The amount of the allowance steering  should be float or int and must be greater than or equal to zero")

        self._sup_all = round(new_sup_all, 2)

    @property
    def allsalary(self):
        """All monthly earnings"""
        return round(self._salary + self._allowance / 100 * self._salary + self._sup_all, 2)

    @property
    def phone(self):
        """The phone number of particular supervisor"""
        return self._phone

    @phone.setter
    def phone(self, new_phone):
        """Set the phone number of particular supervisor

            Args:
                new_phone : new phone number. Number should contains of digits or '+'+digits
            Raises:
                ValueError: if phone number doesn't look like 'digits' or + 'digits'
            Notes:
                If the value of new_phone is correct, it will be assigned to the pone number.
        """

        blank = (str(new_phone)).replace(" ", "")

        if blank[0] == '+':
            if (blank[1:]).isdigit() == False:
                raise ValueError("Number should contains of digits or '+'+digits")
        else:
            if blank.isdigit() == False:
                raise ValueError("Number should contains of digits or '+'+digits")

        self._phone = blank

    @property
    def mphone(self):
        """The mobile phone number of particular supervisor"""
        return self._mphone

    @mphone.setter
    def mphone(self, new_mphone):

        """Set the mobile phone number of particular supervisor

            Args:
                new_phone : new phone number. Number should contains of digits or '+' + digits
            Raises:
                ValueError: if phone number doesn't look like 'digits' or + 'digits'
            Notes:
                If the value of new_phone is correct, it will be assigned to the mobile phone number.
        """

        blank = (str(new_mphone)).replace(" ", "")

        if blank[0] == '+':
            if (blank[1:]).isdigit() == False:
                raise ValueError("Number should contains of digits or '+'+digits")
        else:
            if blank.isdigit() == False:
                raise ValueError("Number should contains of digits or '+'+digits")

        self._mphone = blank

    @property
    def room(self):
        """Supervisor room number"""
        return self._room

    @room.setter
    def room(self, new_room):
        """Set the supervisor room number

        Args:
            new_room : new supervisor room number.

        """
        self._room = new_room

    @property
    def section(self):
        "Name of the Supervisor's department"
        return self._section

    @section.setter
    def section(self, new_section):
        """Set the name of the Supervisor's department

        Args:
            new_section: new name of the Supervisor's department

        """
        self._section = new_section

    def __str__(self):
        """Convert this Supervisor object to string."""
        return "Kierownik:\nImię: {0.name}\nNazwisko: {0.lastname}\nRok Urodzenia: {0.birth_year}\nPensja miesieczna: {0.salary} zł\nProcent Premii: {0.allowance} %\nKwota dodatku kierowniczego: {0.sup_all} zł\nPobory Miesieczne: {0.allsalary} zł\nNumer telefonu: {0.phone}\nNumer telefonu kierunkowego: {0.mphone}\nNumer pokoju: {0.room}\nNazwa działu: {0.section}".format(
            self)

    def __repr__(self):
        """Return textual representation of this Supervisor object."""
        return str(self)