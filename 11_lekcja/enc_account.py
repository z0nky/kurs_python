class Account:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__account_number = '12 4530 0000 1001 2345 3213'

    def show_number(self):
        print("Current account number: {}".format(self.__account_number))

    def set_new_number(self, number):
        self.__account_number = number


user = Account('Maria', 'Kowalczyk')
user.show_number()
print(user.first_name)
print(user.last_name)
# print(user.__account_number)  -  to nie zadziała
user.set_new_number('123')
user.show_number()