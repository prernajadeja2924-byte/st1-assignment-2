
from abc import ABC, abstractmethod

from stage05.domain.appointment import Appointment


class AppointmentRepository(ABC):
    """Defines the operations needed to store and retrieve appointments."""

    @abstractmethod
    def save(self, appointment: Appointment) -> None:
        pass

    @abstractmethod
    def find_by_id(self, appointment_id: str) -> Appointment | None:
        pass