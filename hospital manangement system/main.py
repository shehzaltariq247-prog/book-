from patient import Patient
from doctor import Doctor
from appointment import Appointment
from hospital import Hospital


# Create hospital
hospital = Hospital("City Hospital")

# Create patients
patient1 = Patient(1, "Ali Khan", 30, "Male", "Flu")
patient2 = Patient(2, "Sara Ahmed", 25, "Female", "Fever")

# Create doctors
doctor1 = Doctor(101, "Dr. John", "Cardiology", "0300-1234567")
doctor2 = Doctor(102, "Dr. Maria", "Pediatrics", "0312-7654321")

# Add to hospital
hospital.add_patient(patient1)
hospital.add_patient(patient2)
hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

# Create appointment
appointment1 = Appointment(1001, patient1, doctor1, "2026-07-15", "10:00 AM")
hospital.add_appointment(appointment1)

# Display information
print(hospital.display_info())
print("\nPatients:")
for patient in hospital.list_patients():
    print(patient)

print("\nDoctors:")
for doctor in hospital.list_doctors():
    print(doctor)

print("\nAppointments:")
for appointment in hospital.list_appointments():
    print(appointment)
