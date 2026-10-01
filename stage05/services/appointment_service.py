
from stage05.domain.appointment import Appointment
from stage05.domain.patient import Patient
from stage05.domain.practitioner import Practitioner
from stage05.repositories.appointment_repository import AppointmentRepository


class AppointmentService:
    """Coordinates appointment use cases."""

    def __init__(self, repository: AppointmentRepository):
        self.repository = repository

    def create_appointment(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        appointment_time: str
    ) -> Appointment:
        appointment = Appointment(
            appointment_id,
            patient,
            practitioner,
            appointment_time
        )

        self.repository.save(appointment)
        return appointment

    def find_appointment(self, appointment_id: str) -> Appointment | None:
        return self.repository.find_by_id(appointment_id)

    def cancel_appointment(self, appointment_id: str) -> Appointment:
        appointment = self.repository.find_by_id(appointment_id)

        if appointment is None:
            raise ValueError("Appointment not found")

        appointment.cancel()
        self.repository.save(appointment)

        return appointment