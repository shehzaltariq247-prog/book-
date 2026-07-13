class Doctor:
    def __init__(self, doctor_id, name, specialty, phone_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.phone_number = phone_number

    def display_info(self):
        return (
            f"Doctor ID: {self.doctor_id}\n"
            f"Name: {self.name}\n"
            f"Specialty: {self.specialty}\n"
            f"Phone Number: {self.phone_number}"
        )

    def update_info(self, name=None, specialty=None, phone_number=None):
        if name is not None:
            self.name = name
        if specialty is not None:
            self.specialty = specialty
        if phone_number is not None:
            self.phone_number = phone_number

    def __str__(self):
        return self.display_info()
