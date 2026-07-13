class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor

        
        self.date = date
        self.time = time

    def display_info(self):
        return (
            f"Appointment ID: {self.appointment_id}\n"
            f"Patient: {self.patient.name}\n"
            f"Doctor: {self.doctor.name}\n"
            f"Date: {self.date}\n"
            f"Time: {self.time}"
        )

    def update_info(self, date=None, time=None):
        if date is not None:
            self.date = date
        if time is not None:
            self.time = time

    def __str__(self):
        return self.display_info()
