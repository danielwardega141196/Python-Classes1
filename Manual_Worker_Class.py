from Person_Class import Person

class Manual_Worker(Person):
    """Class containing information about particular Manual Worker"""

    def __init__(self, name, lastname, birth_year, hourly_rate, hours, extra_hours, supervisor, skills):
        super(Manual_Worker, self).__init__(name, lastname, birth_year)

        """Initialize a new Manual Worker object

           The Manual_Worker inherits from the class 'Person'

         Args:
            name(str): The first name of a person. Only letters should be included.
            lastname (str): The last name of a person. Only letters should be included.
            birth_year (int): The birth year of a person. It must be int thereabout 1900.
            hourly_rate (float or double): hourly rate of particular manual worker. It should be float or int and must be greater than or equal to zero
            hours (float or int): the number of working hours. It should be float or int and must be greater than or equal to zero
            extra_hours (float or int): the number of extra working hours. It should be float or int and must be greater than or equal to zero
            supervisor (str): the supervisor of a manual worker. Only letters should be included.
            skills: skills of particular manual worker


        Raises:
            ValueError: if one of the following conditions are not met:
            1. name, lastname, supervisor  doesn't consist of only letters.
            2. birth_year isn't int or is less than 1900
            3. if hourly_rate, hours or extra_hours isn't int or float or value <0

        """

        self._hourly_rate = None
        self._hours = None
        self._extra_hours = None
        self._supervisor = None
        self._skills = None

        self.hourly_rate = hourly_rate
        self.hours = hours
        self.extra_hours = extra_hours
        self.supervisor = supervisor
        self.skills = skills

    @property
    def hourly_rate(self):
        """The hourly rate of particular manual worker"""
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, new_hourly_rate):

        """Set the hourly rate of particular manual worker

        Args:
            new_hourly_rate (float or int): new hourly rate of particular manual worker. It should be float or int and must be greater than or equal to zero
        Raises:
            ValueError: if new_hourly_rate isn't int or float or new_hourly_rate < 0
        Notes:
            If the value of new_hourly_rate is correct, it will be assigned to the hourly rate of particular manual worker.

        """

        if (type(new_hourly_rate) != int and type(new_hourly_rate) != float) or new_hourly_rate < 0:
            raise ValueError("The hourly rate should be float or int and must be greater than or equal to zero")

        self._hourly_rate = round(new_hourly_rate, 2)

    @property
    def hours(self):
        """Number of working hours"""
        return self._hours

    @hours.setter
    def hours(self, new_hours):

        """Set the number of working hours

        Args:
            new_hours (float or int): new number of working hours. It should be float or int and must be greater than or equal to zero
        Raises:
            ValueError: if new_hours isn't int or float or new_hours < 0
        Notes:
            If the value of new_hours is correct, it will be assigned to the the number of working hours.

        """

        if (type(new_hours) != int and type(new_hours) != float) or new_hours < 0:
            raise ValueError(
                "The number of working hours should be float or int and must be greater than or equal to zero")

        self._hours = new_hours

    @property
    def extra_hours(self):
        """Number of extra working hours"""
        return self._extra_hours

    @extra_hours.setter
    def extra_hours(self, new_extra_hours):

        """Set the number of extra working hours

        Args:
            new_extra_hours (float or int): new number of extra working hours. It should be float or int and must be greater than or equal to zero
        Raises:
            ValueError: if new_extra_hours isn't int or float or new_extra_hours < 0
        Notes:
            If the value of new_extra_hours is correct, it will be assigned to the the number of extra working hours.

        """

        if (type(new_extra_hours) != int and type(new_extra_hours) != float) or new_extra_hours < 0:
            raise ValueError(
                "The number of extra working hours should be float or int and must be greater than or equal to zero")

        self._extra_hours = new_extra_hours

    @property
    def supervisor(self):
        """The supervisor of a manual worker"""
        return self._supervisor

    @supervisor.setter
    def supervisor(self, new_supervisor):
        """Set the supervisor of a manual worker

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
    def skills(self):
        """Skills of particular Manual_Worker"""
        return ', '.join(self._skills)

    @skills.setter
    def skills(self, new_skills):
        """Set the skills of manual worker

        Args:
            new_skills : new set of manual worker skills

        """
        self._skills = new_skills

    @property
    def allsalary(self):
        """All monthly earnings"""
        return round(self._hourly_rate * self._hours + 1.5 * self._hourly_rate * self._extra_hours, 2)

    def __str__(self):
        """Convert this Manual_Worker object to string."""
        return "Pracownik fizyczny: \nImię: {0.name}\nNazwisko: {0.lastname}\nRok Urodzenia: {0.birth_year}\nStawka godzinowa: {0.hourly_rate} zł\nLiczba Przepracowanych Godzin: {0.hours}\nLiczba nadgodzin: {0.extra_hours}\nPobory Miesieczne: {0.allsalary} zł\nKierownik: {0.supervisor}\nUmiejętności: {0.skills}".format(
            self)

    def __repr__(self):
        """Return textual representation of this Manual_Worker object."""
        return str(self)