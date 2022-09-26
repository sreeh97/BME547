def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = {"First Name":patient_name.split(' ')[0],
                    "Last Name":patient_name.split(' ')[1], 
                    "Id":patient_id, "Age":patient_age, 
                    "Tests":[]}
    return new_patient
    


def find_patient(db, id_no):
    for patient in db:
        if patient["Id"] == id_no:
            return patient
    return False
   
 
def add_test_to_patient(db, id_no, test_name, test_value):
   patient = find_patient(db, id_no)
   patient["Tests"].append((test_name, test_value))
 

def adult_or_minor(patient):
    if patient["Age"] >= 18:
        return "adult"
    else:
        return "minor"
 
 
def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    #linebyline(db)
    #x = find(db,1)
    #print(db)
    #print_database(db)
    add_test_to_patient(db, 3, "HDL", 100)
    print(db)
    
    '''
    test_results(db, 1, "glucose", 100)
    print(db,3)
    room_list = ["Room 1", "Room 2", "Room 3"]
    
    for i, patient in enumerate(db):
        print("Name = {}, Room = {}".format(patient[0], room_list[i]))
        
    for patient, room in zip(db, room_list):
        print("Name = {}, Room = {}".format(patient[0], room))
    
    '''
    
if __name__ == "__main__":
    a = main()