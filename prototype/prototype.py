import copy


class Address:
    def __init__(self, street_address, city, country):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives in {self.address}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('SB Road', '0', 'Pune'))
    aux_office_employee = Employee('', Address('Baner', '0', 'Pune'))

    @staticmethod
    def __new_employee(proto, name, suite):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee,
            name,
            suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee,
            name,
            suite
        )

address1 = Address('10 jm road', 'Pune', 'India')

john = Person('John', address1)
print(john)
jane = Person('Jane', address1)
jane.name = 'Jane'
print('*********************************')
print(john)
print(jane)
print('*********************************')
jane.address.street_address = '11 MG Road'
print(john)
print(jane)
print('*********************************')
akshay = Person('Akshay', Address('Shyam Nagar', 'Yadrav', 'India'))
snehal = copy.deepcopy(akshay)
snehal.name = 'Snehal'
snehal.address.street_address = 'Chaundeshwari Colony'
snehal.address.city = 'Ichalkaranji'
print(akshay)
print(snehal)

print('*********************************')
a = EmployeeFactory.new_aux_office_employee('ak', '10')
print(a)