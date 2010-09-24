from gen.lib.person import Person
from gen.lib.name import Name

def convert_sex(fs_gender):
    gender = Person.UNKNOWN
    if fs_gender == "Male":
        gender = Person.MALE
    if fs_gender == "Female":
        gender = Person.FEMALE
    return gender

def fs_person_to_gramps(fs_person):
    name = fs_person.assertions.names[0].value.forms[0].fullText
    gramps_person = Person(None,name,"")
    fs_gender = fs_person.assertions.genders[0].value.type
    gramps_person.gender = convert_sex(fs_gender)
    return gramps_person
    