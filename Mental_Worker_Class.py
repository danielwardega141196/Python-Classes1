from Person_Class import Person

class Mental_worker(Person):
    """Class containing information about particular mental worker"""

    def __init__(self, name, lastname, birth_year, salary, allowance, supervisor, phone, room):
        """Initialize a new Mental_worker object

           The Mental_worker inherits from the class 'Person'

         Args:
            name(str): The first name of a person. Only letters should be included.
            lastname (str): The last name of a person. Only letters should be included.
            birth_year (int): The birth year of a person. It must be int thereabout 1900.
            salary : basic salary of a mental worker. It should be float or int and must be greater than or equal to zero.
            allowance : the percentage of a premium. It should be float or int and must be greater than or equal to zero
            supervisor: the supervisor of a mental worker. Only letters should be included.
            phone: the phone number of particular mental worker. Number should contains of digits or '+'+digits
            room : mental worker room number.
        Raises:
            ValueError: if one of the following conditions are not met:
            1. name, lastname, supervisor doesn't consist of only letters.
            2. birth_year isn't int or is less than 1900
            3. if salary or allowance isn't int or float or value <0
            4. phone number doesn't look like 'digits' or + 'digits'
        """

        super(Mental_worker, self).__init__(name, lastname, birth_year)

        self._salary = None
        self._allowance = None
        self._supervisor = None
        self._phone = None
        self._room = None

        self.salary = salary
        self.allowance = allowance
        self.supervisor = supervisor
        self.phone = phone
        self.room = room

    @property
    def salary(self):
        """ Basic Salary of a mental worker """
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        """Set the basic salary of a mental worker

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

        """Set the the Percentage of a premium

        Args:
            new_allowance (float or int) : New percentage of a premium. It should be float or int and must be greater than or equal to zero
        Raises:
            ValueError: if new_allowance isn't int or float or new_allowance <0
        Notes:
            If the value of new_allowance is correct, it will be assigned to the percentage of a premium.
        """

        if (type(new_allowance) != int and type(new_allowance) != float) or new_allowance < 0:
            raise ValueError(
                "The Percentage of a premium should be float or int and must be greater than or equal to zero")
        self._allowance = new_allowance

    @property
    def supervisor(self):
        """The supervisor of a mental worker"""
        return self._supervisor

    @supervisor.setter
    def supervisor(self, new_supervisor):
        """Set the supervisor of a mental worker

        Args:
            new_supervisor (str): new supervisor. Only letters should be included.
        Raises:
            ValueError: if signs except of only letters are also included
        Notes:
            If the value of new_supervisor is correct, it will be assigned to the supervisor.
        """

        if (str(new_supervisor)).isalpha() == False:
            raise ValueError("A correct supervisor name must contain only letters")
        self._supervisor = new_supervisor

    @property
    def phone(self):
        """The phone number of particular mental worker"""
        return self._phone

    @phone.setter
    def phone(self, new_phone):

        """Set the phone number of particular menal worker

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
    def room(self):
        """Mental worker room number"""
        return self._room

    @room.setter
    def room(self, new_room):
        """Set the mental worker room number

        Args:
            new_room : new mental worker room number.

        """
        self._room = new_room

    @property
    def allsalary(self):
        """All monthly earnings"""
        return round(self._salary + self._salary * self._allowance / 100, 2)

    def __str__(self):
        """Convert this Mental_worker object to string."""
        return "Pracownik Umysłowy:\nImię: {0.name}\nNazwisko: {0.lastname}\nRok Urodzenia: {0.birth_year}\nPensja miesieczna: {0.salary} zł\nPremia: {0.allowance} %\nPobory Miesieczne: {0.allsalary} zł\nKierownik: {0.supervisor}\nNumer telefonu: {0.phone}\nNumer pokoju: {0.room}\n".format(
            self)

    def __repr__(self):
        """Return textual representation of this Mental_worker object."""
        return str(self)