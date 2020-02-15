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
    def __init__(self, name, message, useage, strict_dosage):
        self.name = name
        self.message = message
        self.useage = useage
        self.strict_dosage = strict_dosage

def add():
    global ID_COUNT
    patient_name = input("Please input patient's first name and last name: ").lower()
    patient_birthday = input("Please input patient's birthday as MMDDYYYY: ")
    patient_phone = input("Please input patient's phone number: ")
    new_patient = Patient(patient_name, patient_birthday, patient_phone)
    patients.append(new_patient)
    ID_COUNT += 1

def prescribe(current_doctor):
    global drugs, prescribed
    patient_name = input("Please input patient's first name and last name: ").lower()
    patient_birthday = input("Please input patient's birthday as MMDDYYYY: ")
    current_patient = "NA"
    for i in patients:
        patient_name_split = patient_name.split(" ")
        if (i.firstname == patient_name_split[0] and i.lastname == patient_name_split[1] and i.birthday == patient_birthday):
            current_patient = i
    if current_patient == "NA":
        print("Invalid Patient")
    else:
        not_exist = True
        current_drug = "NA"
        while (not_exist):
            drug = input("Please input prescription name: ").lower()
            for i in drugs:
                if (i == drug):
                    not_exist = False
                    current_drug = i
            if (not_exist):
                print("Prescription does not exist!")
        message = input("Message to be included with text reminder: ")
        usage = 2
        strict_dosage = False
        drug_object = Drug(current_drug,message,usage,strict_dosage)
        current_patient.assign_drug(drug_object)
        prescribed[current_doctor.name] = current_patient.firstname + " " + current_patient.lastname

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

if __name__ == '__main__':

    new_doctor = Doctor("John Smith","John", "Smith", "5555555555")
    doctors.append(new_doctor)

    new_patient = Patient("Kyle Bui", "11111111", "5555555555")
    patients.append(new_patient)
    ID_COUNT += 1

    
    current_doctor = doctor_login()
    while True:
        to_do = input("Please input what you would like to do 'prescribe' or 'add': ").lower()
        if to_do == "prescribe":
            prescribe(current_doctor)
        elif to_do == "add":
            add()
        else:
            print("Invalid choice!")


