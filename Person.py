from hazelcast.serialization.api import Portable
from BankAccount import BankAccount
class Person():
    """ Person Klasse """

    def __init__(self):
        """
        Standardkonstruktor der Person Klasse

        :param self: LOLKEK
        """
        self.bankAcc = BankAccount()
        self.name = "mr Blank"
        self.age = 88
    def __init__(self,name:str,age:int):
        """Konstruktor der Person Klasse

        :param age: (int) Alter der Person muss >=0 sein.
        """
        self.bankAcc = BankAccount()
        self.name = name
        self.age = age
    def factor_age(self,factor:[float,int]):
        """
        Verdoppelt das Alter der Person

        :param factor: Der Faktor mit dem das Alter multipliziert wird.

        :return: Neues Alter.

        """
        self.age = self.age * factor
        return self.age
    # def read_portable(self, reader):
    #     self.name =   reader.read_utf("name")
    #     self.age = reader.read_int("age")
    #     self.bankAcc.credit = reader.read_int("bankAcc.credit")
    # def write_portable(self, writer):
    #     writer.write_utf("name",self.name)
    #     writer.write_int("age",self.age)
    #     writer.write_int("bankAcc.credit",self.bankAcc.credit)
    #s
    # def get_class_id(self):
    #     return 100
    #
    # def get_factory_id(self):
    #     return 1000
