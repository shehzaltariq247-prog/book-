class Patient:
    def __init__(self, patient_id, name, age, gender, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def display_info(self):
        return (
            f"Patient ID: {self.patient_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Gender: {self.gender}\n"
            f"Disease: {self.disease}"
        )

    def update_info(self, name=None, age=None, gender=None, disease=None):
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if gender is not None:
            self.gender = gender
        if disease is not None:
            self.disease = disease

    def __str__(self):
        return self.display_info()
