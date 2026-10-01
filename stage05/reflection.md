
# Stage 05 Reflection

In this stage, I refactored SmartCare into a layered architecture. I separated the system into domain, service, repository, persistence and presentation responsibilities. The existing Patient, Practitioner and Appointment behaviour was kept while the workflow coordination was moved into AppointmentService.

## AI Architecture Review

### Accepted Suggestion

I accepted the suggestion to use a small repository abstraction between the service and persistence layers. This reduces direct dependency on storage details and keeps AppointmentService focused on coordinating the appointment use case.

### Modified Suggestion

The AI suggested making the package structure clearer. I used separate domain, services, repositories, persistence and presentation folders, but kept the implementation simple rather than adding extra architectural patterns that were not required.

### Rejected / Deferred Suggestion

I rejected or deferred adding microservices, an event bus, multiple unnecessary interfaces and a dependency-injection framework. These would add unnecessary complexity to the current SmartCare requirements.

## Verification

After refactoring, I tested the application again. The patient and practitioner information displayed correctly, an appointment was created with Scheduled status, cancellation changed the status to Cancelled, and attempting to cancel it again correctly produced an error. This confirmed that the required behaviour remained unchanged after the architecture refactoring.