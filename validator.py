import re

class ValidationStrategy:
    def validate(self, data):
        raise NotImplementedError

class EmailValidator(ValidationStrategy):
    def validate(self, data):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, data))

class PasswordValidator(ValidationStrategy):
    def validate(self, data):
        return (
            len(data) >= 8 and
            any(c.isdigit() for c in data) and
            any(c.isupper() for c in data)
        )

class Validator:
    def __init__(self, strategy: ValidationStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: ValidationStrategy):
        self.strategy = strategy

    def validate(self, data):
        return self.strategy.validate(data)


validator = Validator(EmailValidator())
print(validator.validate("test@gmail.com"))

validator.set_strategy(PasswordValidator())
print(validator.validate("Pass1234"))