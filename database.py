class Patient:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.patient_id = ""
        self.age = ""
        self.test = []

    def full_name(self):
        return " {} {}".format(self.first_name, self.last_name)


def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = Patient()
    new_patient.first_name = patient_name.split(' ')[0]
    new_patient.last_name = patient_name.split(' ')[1]
    new_patient.patient_id = patient_id
    new_patient.Age = patient_age
    return new_patient


def get_full_name(patient):
    full_name = " {} {}".format(patient["First Name"], patient["Last Name"])
    return full_name


def print_database(db):
    for patient_key in db:
        print(patient_key)
        print("Name: {}, id:{}, age:{}".format(get_full_name(db[patient_key]),
                                               db[patient_key]["Id"],
                                               db[patient_key]["Age"]))
    for patient in db.values():
        print("Name: {}, id: {}, age: {}".format(get_full_name(patient),
                                                 patient["Id"],
                                                 patient["Age"]))


def find_patient(db, id_no):
    patient = db[id_no]
    return patient


def add_test_to_patient(db, id_no, test_name, test_value):
    patient = find_patient(db, id_no)
    patient["Tests"].append((test_name, test_value))


def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"


def main():
    x = Patient()
    x.first_name = "David"
    x.last_name = "Ward"
    print(x.last_name)
    print(type(x))
    y = Patient()
    y.first_name = "Edward"
    y.last_name = "Smith"
    print(y.full_name())
    exit()
    db = {}
    db[11] = create_patient_entry("Ann Ables", 1, 30)
    db[22] = create_patient_entry("Bob boyles", 2, 34)
    db[3] = create_patient_entry("Chris Chou", 3, 25)
    print_database(db)


if __name__ == "__main__":
    a = main()
