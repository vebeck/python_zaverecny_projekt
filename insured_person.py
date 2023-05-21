class InsuredPerson:

    def __init__(self, name, surname, age, phone):
        # konstruktor třídy
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def __str__(self):
        # vrací textovou reprezentaci pojištěných osob
        return f"{self.name}    {self.surname}    {self.age} let    {self.phone}"