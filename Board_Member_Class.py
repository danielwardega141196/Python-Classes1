from Person_Class import Person

class Board_member(Person):
    """Class containing information about particular Board_member"""

    def __init__(self, name, lastname, birth_year, salary, assistant, board, pay_bo):
        """Initialize a new Board_member object

           The Board_member inherits from the class 'Person'

         Args:
            name(str): The first name of a person. Only letters should be included.
            lastname (str): The last name of a person. Only letters should be included.
            birth_year (int): The birth year of a person. It must be int thereabout 1900.
            salary : basic salary of a board member. It should be float or int and must be greater than or equal to zero.
            assistant : The name of board member assistant. Only letters should be included.
            board : How many times particular board member attended in the supervisory board meetings. It must be int greater than or equal to zero
            pay_bo : amount awarded for the board meeting. It should be float or int and must be greater than or equal to zero

        Raises:
            ValueError: if one of the following conditions are not met:
            1. name, lastname,assistant  doesn't consist of only letters.
            2. birth_year isn't int or is less than 1900
            3. if salary or pay_bo isn't int or float or value <0
            4. if board isn't int or is less than zero
        """

        super(Board_member, self).__init__(name, lastname, birth_year)

        self._salary = None
        self._assistant = None
        self._board = None
        self._pay_bo = None

        self.salary = salary
        self.assistant = assistant
        self.board = board
        self.pay_bo = pay_bo

    @property
    def salary(self):
        """ Basic Salary of a Board_member"""
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        """Set the basic salary of a Board member

        Args:
            new_salary (float or int) : new basic salary. It should be float or int and must be greater than or equal to zero
        Raises:
            ValueError: if new_salary isn't int or float or new_salary < 0
        Notes:
            If the value of new_salary is correct, it will be assigned to the basic salary.
        """

        if (type(new_salary) != int and type(new_salary) != float) or new_salary < 0:
            raise ValueError("The Salary should be float or int and must be greater than or equal to zero")

        self._salary = round(new_salary, 2)

    @property
    def assistant(self):
        """The name of board member assistant"""
        return self._assistant

    @assistant.setter
    def assistant(self, new_assistant):
        """Set name of board member assistant

        Args :
            new_assistant (str): new name of board member assistant. Only letters should be included.
        Raises:
            ValueError: if signs except of only letters are also included
        Notes:
            If the value of new_assistant is correct, it will be assigned to the name of board member assistant
        """

        if (str(new_assistant)).isalpha() == False:
            raise ValueError("A correct name of board member assistant must contain only letters.")

        self._assistant = new_assistant

    @property
    def board(self):
        """How many times particular board member attended in the supervisory board meetings"""
        return self._board

    @board.setter
    def board(self, new_board):
        """Set How many times particular board member attended in the supervisory board meetings

        Args :
            new_board (int): new number of participation. It must be int greater than or equal to zero
        Raises:
            ValueError: if isn't int or is less than zero
        Notes:
            If the value of new_board is correct, it will be assigned to the number of participation.

        """
        if (str(new_board)).isdigit() == False:
            raise ValueError("Isn't int or is less than zero")

        self._board = new_board

    @property
    def pay_bo(self):
        """Amount awarded for the board meeting"""
        return self._pay_bo

    @pay_bo.setter
    def pay_bo(self, new_pay_bo):

        """Set the amount awarded for the board meeting

        Args:
            new_pay_bo (float or int) : new amount awarded for the board meeting. It should be float or int and must be greater than or equal to zero
        Raises:
            ValueError: if new_pay_bo isn't int or float or new_pay_bo <0
        Notes:
            If the value of new_pay_bo is correct, it will be assigned to amount awarded for the board meeting.
        """

        if (type(new_pay_bo) != int and type(new_pay_bo) != float) or new_pay_bo < 0:
            raise ValueError(
                "The amount awarded for the board meeting should be float or int and must be greater than or equal to zero")

        self._pay_bo = round(new_pay_bo, 2)

    @property
    def allsalary(self):
        """All monthly earnings"""
        return round(self._salary + self._board * self._pay_bo, 2)

    def __str__(self):
        """Convert this board member object to string."""
        return "Członek Zarządu:\nImię: {0.name}\nNazwisko: {0.lastname}\nRok Urodzenia: {0.birth_year}\nPensja miesieczna: {0.salary} zł\nPobory Miesieczne: {0.allsalary} zł\nIle razy uczestniczył w spotkaniach rady nadzorczej: {0.board}\nKwota przyznana za uczestnictwo w spotkaniu rady nadzorczej: {0.pay_bo} zł\nAsystent: {0.assistant}".format(
            self)

    def __repr__(self):
        """Return textual representation of this Board_member object."""
        return str(self)