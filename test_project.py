from project import name, date, destination, email

def main():
    name_check()
    date_validation()
    destination_confirm()
    validate_email()


def name_check():
    assert name("Yugo Iwamoto") == "Name Check Passed"
    try:
        assert name("Stephen Jacob Smith Tom")== "Too Many Inputs"
    except Exception as error:
        print(error)

    try:
        assert name("")== "Not Enough Inputs"
    except Exception as error:
        print(str(error))
    print("Name Check Succeeded")



def date_validation():
    try:
        assert date("11/22/2024") == "2024-11-22"
        assert date("November 22, 2024")== "2024-11-22"
        assert date("121122")== ()
        print("Date Validation Succeeded")
    except Exception as error:
        print(str(error))


def destination_confirm():
    assert destination("Rochester") == "Destination Confirmed"
    assert destination("Chicago")== "Destination Confirmed"
    try:
        assert destination("")== "Invalid Destination. Try replacing spaces (' ') with a dash ('-')"
    except Exception as error:
        print(str(error))
    try:
        assert destination("Rochester Chicago Denver")== "Invalid Destination. Try replacing spaces (' ') with a dash ('-')"
    except Exception as error:
        print(str(error))
    print("Destination Confirmation Succeeded")
def validate_email():
    try:
        assert email("yu5.july8@gmail.com") == "Valid"
        assert email("sample@brockport.edu")== "Valid"
        assert email("1234567") == "Invalid"
    except Exception as error:
        print(str(error))
    print("Email Validation Succeeded")


if __name__ == "__main__":
    main()
