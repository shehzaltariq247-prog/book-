class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def list_patients(self):
        return self.patients

    def list_doctors(self):
        return self.doctors

    def list_appointments(self):
        return self.appointments

    def display_info(self):
        return f"Hospital: {self.name}"

    def __str__(self):
        return self.display_info()