import time

patients = []
doctors = []
prescribed = {}
ID_COUNT = 0

drugs_txt = open("drugs.txt",'r')
drugs = [(line.lower()).rstrip("\n") for line in drugs_txt.readlines()]


class Doctor:
    def __init__(self, name, username, password, phone):
        self.name = name
        self.username = username
        self.password = password
        self.phone = phone

class Patient:
    def __init__(self, name, birthday, phone):
        name_split = name.split(" ")
        self.firstname = name_split[0].lower()
        self.lastname = name_split[1].lower()
        self.birthday = birthday
        self.phone = phone
        self.ID = ID_COUNT

    def assign_drug(self, drug):
        self.drug = drug

class Drug:
    def __init__(self, name, message, usage):
        self.name = name
        self.message = message
        self.usage = usage
        self.strict_dosage = False
    
    def change_strict(self):
        self.strict_dosage = True

def add(patient_name, patient_birthday, patient_phone):
    global ID_COUNT
    new_patient = Patient(patient_name, patient_birthday, patient_phone)
    patients.append(new_patient)
    ID_COUNT += 1
    

def patient_exist(name, birthday):
    current_patient = "NA"
    patient_name_split = name.split(" ")
    for i in patients:
        if (i.firstname == patient_name_split[0].lower() and i.lastname == patient_name_split[1].lower() and i.birthday == birthday):
            return i
    if current_patient == "NA":
        return False

def prescribe(current_doctor, patient, drug, message):
    not_exist = True
    current_drug = "NA"
    while (not_exist):
        for i in drugs:
            if (i == drug.lower()):
                not_exist = False
                current_drug = i
        if (not_exist):
            print("Prescription does not exist!")
    usage = time.time()
    # strict_dosage = input("Please indicate whether patient has a strict dosage (True/False): ")

    drug_object = Drug(current_drug,message,usage)

    # if (bool(strict_dosage)):
    #     drug_object.change_strict()
    patient.assign_drug(drug_object)
    prescribed[patient.firstname + " " + patient.lastname] = current_doctor.name

def doctor_login():
    t = True
    while (t):
        doctor_username = input("Please input your username: ")
        doctor_password = input("Please input your password: ")
        for i in doctors:
            if i.username == doctor_username and i.password == doctor_password:
                return i
                t = False
            else:
                print("Invalid login credentials!")

def check_message():
    for p in prescribed.keys():
        for i in patients:
            if p.split(" ")[0] == i.firstname and p.split(" ")[1] == i.lastname:
                current = i
                if (time.time() - i.drug.usage) >= 30:
                    print("Sent Text Message")
                    i.drug.usage = time.time()


if __name__ == '__main__':

    new_doctor = Doctor("John Smith","John", "Smith", "5555555555")
    doctors.append(new_doctor)

    new_patient = Patient("Kyle Bui", "11111111", "5555555555")
    patients.append(new_patient)
    ID_COUNT += 1

    
    current_doctor = doctor_login()



