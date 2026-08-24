#doctor receptionist program

class Person:

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

    def setFirstName(self, first_name):
        self.first_name = first_name

    def setLastName(self, last_name):
        self.last_name = last_name

    def getPhoneNumber(self):
        return self.phone_number

    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number

    def __str__(self):
        return 'Person: ' + self.first_name + ' ' + \
               self.last_name + '\t' + \
               self.phone_number


# Doctor subclass

class Doctor(Person):

    def __init__(self, first_name, last_name, phone_number, specialty):
        super().__init__(first_name, last_name, phone_number)
        self.__specialty = specialty

    def getSpecialty(self):
        return self.__specialty

    def setSpecialty(self, specialty):
        self.__specialty = specialty

    def __str__(self):
        return 'Dr. ' + self.first_name + ' ' + \
               self.last_name + '\t' + \
               self.phone_number + '\t' + \
               self.__specialty


# Patient subclass

class Patient(Person):

    def __init__(self, first_name, last_name, phone_number, reason_for_visit):
        super().__init__(first_name, last_name, phone_number)
        self.__reason_for_visit = reason_for_visit

    def getReasonForVisit(self):
        return self.__reason_for_visit

    def setReasonForVisit(self, reason_for_visit):
        self.__reason_for_visit = reason_for_visit

    def __str__(self):
        return 'Patient: ' + self.first_name + ' ' + \
               self.last_name + '\t' + \
               self.phone_number + '\t' + \
               self.__reason_for_visit


# Main

def find_doctor(name, doctors):
    # look through doctor list, match by full name
    for doctor in doctors:
        full_name = f"{doctor.getFirstName()} {doctor.getLastName()}"
        if full_name.lower() == name.lower():
            return doctor
    return None


def find_patient(name, patients):
    # look through patient list, match by full name
    for patient in patients:
        full_name = f"{patient.getFirstName()} {patient.getLastName()}"
        if full_name.lower() == name.lower():
            return patient
    return None


def main():

    # create patients
    p1 = Patient("John", "Doe", "555-123-4567", "Chest pain")
    p2 = Patient("Maria", "Garcia", "555-234-5678", "Skin rash")
    p3 = Patient("Liam", "Brown", "555-345-6789", "Fever")
    p4 = Patient("Priya", "Nair", "555-456-7890", "Knee pain")

    # create doctors
    d1 = Doctor("Sarah", "Smith", "555-999-0000", "Cardiology")
    d2 = Doctor("Raj", "Patel", "555-888-1111", "Dermatology")
    d3 = Doctor("Emily", "Chen", "555-777-2222", "Pediatrics")
    d4 = Doctor("Marcus", "Johnson", "555-666-3333", "Orthopedics")

    # update phone number
    d4.setPhoneNumber("908-273-8826")

    # store doctors in list
    doctors = [d1, d2, d3, d4]

    # print doctors
    for d in doctors:
        print(str(d))

    # store patients in list
    patients = [p1, p2, p3, p4]

    # print patients
    for p in patients:
        print(str(p))

    # find doctor
    d = find_doctor("Raj Patel", doctors)
    print("Doctor found:", d)

    # find patient
    p = find_patient("John Doe", patients)
    print("Patient found:", p)


# run program
main()
