
from stage05.domain.patient import Patient
from stage05.domain.practitioner import Practitioner
from stage05.services.appointment_service import AppointmentService
from stage05.persistence.in_memory_appointment_repository import (
    InMemoryAppointmentRepository
)



# Create repository and service
repository = InMemoryAppointmentRepository()
service = AppointmentService(repository)


# Create domain objects
patient = Patient("P001", "Alice Smith")

practitioner = Practitioner(
    "PR001",
    "Dr. John Doe",
    "General Practice"
)


# Create appointment through the service
appointment = service.create_appointment(
    "A001",
    patient,
    practitioner,
    "2026-10-10 10:00 AM"
)

print(patient.view_information())
print(practitioner.view_information())
print(appointment.view_information())


# Cancel appointment through the service
service.cancel_appointment("A001")

print(appointment.view_information())


# Test invalid transition
try:
    service.cancel_appointment("A001")
except ValueError as error:
    print("Invalid transition caught:", error)