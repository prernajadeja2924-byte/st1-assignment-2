
from stage05.domain.appointment import Appointment
from stage05.repositories.appointment_repository import AppointmentRepository


class InMemoryAppointmentRepository(AppointmentRepository):
    """Stores appointments in memory."""

    def __init__(self):
        self._appointments = {}

    def save(self, appointment: Appointment) -> None:
        self._appointments[appointment.appointment_id] = appointment

    def find_by_id(self, appointment_id: str) -> Appointment | None:
        return self._appointments.get(appointment_id)