import re
from phonenumbers import PhoneNumberFormat, parse as phone_parse, format_number as phone_format


class PhonesBr:
    def __init__(self,phone):
        self._common = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        if self.validate_phones(phone):
            self.number = phone
        else:
            raise ValueError("Número incorreto!")

    def validate_phones(self,phone):
        response = re.findall(self._common,phone)
        if response:
            return True
        else:
            return False
    def __str__(self) -> str:
      return phone_format(phone_parse(self.number, 'BR'), PhoneNumberFormat.NATIONAL)    
    