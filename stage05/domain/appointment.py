
from enum import Enum

from stage05.domain.patient import Patient
from stage05.domain.practitioner import Practitioner


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"
    COMPLETED = "Completed"


class Appointment:
    """Represents an appointment between a patient and practitioner."""

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