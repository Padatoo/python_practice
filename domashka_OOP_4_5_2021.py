# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from string import digits

class User:

    def __init__(self, login, password):
        self.login = login
        self.__password = password

    @property
    def password(self):
        print('getter called')
        return self.__password

    @staticmethod
    def is_include_number(password):
        for digit in digits:
            if digit in password:
                return True
        return False

    @staticmethod
    def is_in_pw_dict(password):
        with open('practice_pw_dict.txt') as f:
            lst = [i.strip("\n") for i in f]
            if password in lst:
                return True
            else:
                return False

    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError("пароль должен быть строкой")
        if len(value) < 4:
            raise ValueError("Длина пароля слишком мала, минимум должно быть 4")
        if len(value) > 12:
            raise ValueError("длина пароля слишком велика, максимум должно быть 12 символов")
        if not User.is_include_number(value):
            raise ValueError("пароль должен иметь хотя бы одну цифру")
        if User.is_in_pw_dict(value):
            raise ValueError("пароль в списке паролей")
        self.__password = value

x = User('abc', 'qwerty1')
#x.password = '1234567q'