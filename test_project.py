from project import name, date, destination, email

def main():
    name_check()
    date_validation()
    destination_confirm()
    validate_email()


def name_check():
    assert name("Stephen Jacob Smith Tom")== False
    assert name("Yugo Iwamoto") == True

def date_validation():
    assert date("11/22/2024") == True
    assert date("November 22, 2024")== True
    assert date("121122")== False


def destination_confirm():
    assert destination("Rochester") == True
    assert destination("Chicago")== True

def validate_email():
    assert email("yu5.july8@gmail.com") == True
    assert email("sample@brockport.edu")== True
    assert email("1234567") == False


if __name__ == "__main__":
    main()

