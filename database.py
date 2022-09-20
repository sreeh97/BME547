def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age, []]
    return new_patient
   
def linebyline(a):
    for i in a:
        print(i[0], i[1], i[2])

def find(db, id_no):
    for patient in db:
        if patient[1] == id_no:
            return patient
    return False
   

def test_results(db, id_no, test_name, test_value):
    patient = find(db, id_no)
    patient[3].append((test_name,test_value))
     
   
   
def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    linebyline(db)
    x = find(db,1)
    print(x)
    test_results(db, 1, "glucose", 100)
    print(db,3)
    room_list = ["Room 1", "Room 2", "Room 3"]
    
    for i, patient in enumerate(db):
        print("Name = {}, Room = {}".format(patient[0], room_list[i]))
        
    for patient, room in zip(db, room_list):
        print("Name = {}, Room = {}".format(patient[0], room))
    

    
if __name__ == "__main__":
    a = main()