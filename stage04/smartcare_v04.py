from enum import Enum


class Patient:
    """Represents a patient in the SmartCare system."""

    def __init__(self, patient_id: str, name: str):
        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty")

        if not name.strip():
            raise ValueError("Patient name cannot be empty")

        self.patient_id = patient_id
        self.name = name

    def create_record(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name
        }

    def view_information(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}"


class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be empty")

        if not specialty.strip():
            raise ValueError("Practitioner specialty cannot be empty")

        if not name.strip():
            raise ValueError("Practitioner name cannot be empty")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def create_record(self):
        return {
            "practitioner_id": self.practitioner_id,
            "name": self.name,
            "specialty": self.specialty
        }

    def view_information(self):
        return (
            f"Practitioner ID: {self.practitioner_id}, "
            f"Name: {self.name}, "
            f"Specialty: {self.specialty}"
        )


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class Appointment:
    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        appointment_time: str
    ):
        if not appointment_id.strip():
            raise ValueError("Appointment ID cannot be empty")

        if not appointment_time.strip():
            raise ValueError("Appointment time cannot be empty")

        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.appointment_time = appointment_time
        self._status = AppointmentStatus.SCHEDULED

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def change_appointment(self, new_time: str):
        if self._status != AppointmentStatus.SCHEDULED:
            raise ValueError("Only scheduled appointments can be changed")

        if not new_time.strip():
            raise ValueError("Appointment time cannot be empty")

        self.appointment_time = new_time

    def cancel(self):
        if self._status != AppointmentStatus.SCHEDULED:
            raise ValueError("Only scheduled appointments can be cancelled")

        self._status = AppointmentStatus.CANCELLED

    def complete(self):
        if self._status != AppointmentStatus.SCHEDULED:
            raise ValueError("Only scheduled appointments can be completed")

        self._status = AppointmentStatus.COMPLETED

    def view_information(self):
        return (
            f"Appointment ID: {self.appointment_id}, "
            f"Patient: {self.patient.name}, "
            f"Practitioner: {self.practitioner.name}, "
            f"Time: {self.appointment_time}, "
            f"Status: {self._status.value}"
        )


# Manual testing

patient = Patient("P001", "Alice Smith")
print(patient.view_information())

practitioner = Practitioner(
    "PR001",
    "Dr. John Doe",
    "General Practice"
)
print(practitioner.view_information())

appointment = Appointment(
    "A001",
    patient,
    practitioner,
    "2026-10-10 10:00 AM"
)

print(appointment.view_information())

appointment.cancel()
print(appointment.view_information())

try:
    appointment.cancel()
except ValueError as error:
    print("Invalid transition caught:", error)