from insured_person import InsuredPerson


class Evidence:
    def __init__(self):
        # list pro uložení pojištěnců
        self.evidence = []

    def add_new_person_to_evidence(self):
        # metoda pro vytvoření nového pojištěného do listu, obsahuje také ošetření případných chyb při zadávání údajů

        while True:
            name = input("Zadejte jméno pojištěné osoby:\n").strip().capitalize()
            if not name.isalpha():
                print("Bylo zadáno neplatné jméno. Jméno smí obsahovat pouze písmena, zadejte prosím znovu:\n")
            else:
                break

        while True:
            surname = input("Zadejte příjmení pojištěné osoby:\n").strip().capitalize()
            if not surname.isalpha():
                print("Bylo zadáno neplatné příjmení. Příjmení smí obsahovat pouze písmena, zadejte prosím znovu: \n")
            else:
                break

        while True:
            age = input("Zadejte věk pojištěné osoby:\n").strip()
            if not age.isdigit() or not 0 <= int(age) <= 100:
                print("Byl zadán neplatný věk. Zadejte prosím znovu opravdový věk pojištěné osoby: \n")
            else:
                break

        while True:
            phone = input("Zadejte telefonní číslo pojištěné osoby: \n").strip()
            if not phone.isnumeric() or len(phone) != 9:
                print("Bylo zadáno telefonní číslo neplatného tvaru. Zadejte prosím telefon v 9ti místném formátu:\n")
            else:
                break

        print("Nová pojištěná osoba byla úspěšně uložena do evidence.")

        insured_person = InsuredPerson(name, surname, age, phone)
        self.evidence.append(insured_person)

    def search_for_insured_person(self):
        # metoda hledá konkrétní pojištěné osoby na základě jména a příjmení
        # pokud se jméno ani příjmení neshoduje s žádným ze záznamů, tak metoda vypíše, že pojištěný nebyl nalezen

        search_name = input("Zadejte jméno: ")
        search_surname = input("Zadejte příjmení: ")

        for insured_person in self.evidence:
            if insured_person.name == search_name and insured_person.surname == search_surname:
                print(str(insured_person))
                break
        else:
            print("Pojištěný nenalezen, zkuste to prosím znovu.")

    def list_of_insured_persons(self):

        # metoda vypisuje všechny záznamy pojištěných v evidenci, též kontroluje, zda je nějaký záznám vůbec obsažen

        if len(self.evidence) == 0:
            print("Evidence je prázdná.")
        for insured_person in self.evidence:
            print(str(insured_person))

    def main(self):

        # hlavní část aplikace, která uživateli vypisuje možnosti ke zvolení a zároveň volá metodu pro volbu akce
        # while cyklus zajišťuje opakování zadávání příkazů, dokud uživatel nezvolí ukončení programu

        while True:
            print("**************************\nEvidence pojištěných osob\n**************************\n")
            choice = input("Zvolte akci:\n"
                           "[1] Přidání nové pojištěné osoby\n"
                           "[2] Vyhledání pojištěné osoby dle jména a příjmení\n"
                           "[3] Výpis všech pojištěných osob\n"
                           "[4] Konec aplikace\n"
                           "\n"
                           "Zadejte svou volbu: ")

            if choice == "1":
                Evidence.add_new_person_to_evidence(self)
            elif choice == "2":
                Evidence.search_for_insured_person(self)
            elif choice == "3":
                Evidence.list_of_insured_persons(self)
            elif choice == "4":
                print("Konec aplikace.\n")
                break
            else:
                print("\nNeplatná volba, zvolte prosím možnost ve tvaru: 1, 2, 3, 4.\n")
