from project import get_info()

def main():
    name_check()
    date_validation()
    destination_confirm()
    validate_email()


def name_check():
    assert list_creator("Yugo Iwamoto") == True

def date_validation():
    assert list_creator("11/22/2024") == True


def destination_confirm():
    assert list_creator("Rochester") == True

def validate_email():
    assert list_creator("yu5.july8@gmail.com") == True


if __name__ == "__main__":
    main()

