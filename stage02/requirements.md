# SmartCare v0.2 Requirements Specification

## 1. Problem and Scope

SmartCare Community Clinic currently uses spreadsheets and paper records to manage patient, practitioner and appointment information. Staff report duplicate bookings, difficulty finding patient information, inconsistent appointment status and limited appointment history.

The proposed SmartCare system will provide a small, maintainable solution for managing patients, practitioners and appointments.

### In Scope
- Patient management
- Practitioner management
- Appointment management
- Appointment status
- Appointment history
- Practitioner schedules and availability
- Prevention of duplicate bookings

### Out of Scope
- Online payments
- Facial-recognition login
- AI treatment recommendations

Features that are not clearly supported by the client brief will remain provisional until they are validated.

## 2. Stakeholders

| Stakeholder | Need | Evidence |
|---|---|---|
| Receptionist | Manage patient information and create, view, change or cancel appointments. | Stage 1 prototype focuses on receptionist appointment management. |
| Patients | Accurate patient records and appointment bookings. | The client brief identifies problems with patient information and appointments. |
| Practitioners | View their appointments and availability. | Limited visibility of practitioner availability was identified as a problem. |
| Clinic Management | A small, maintainable and reliable clinic system. | The Week 5 client brief states that management wants a small, maintainable patient, practitioner and appointment system. |

## 3. Functional Requirements

FR-01: The system shall allow staff to create a patient record.

FR-02: The system shall allow staff to search for a patient by ID.

FR-03: The system shall allow staff to view patient information.

FR-04: The system shall allow staff to create an appointment for a patient with a practitioner.

FR-05: The system shall allow staff to view recorded appointments.

FR-06: The system shall allow staff to change an existing appointment.

FR-07: The system shall allow staff to cancel an appointment.

FR-08: The system shall record the status of an appointment consistently.

FR-09: The system shall allow practitioner information to be recorded and viewed.

FR-10: The system shall allow practitioner schedules or availability to be viewed.

FR-11: The system shall prevent duplicate bookings for the same practitioner at the same appointment time.

FR-12: The system shall retain appointment history, including cancelled appointments, subject to client confirmation.

## 4. Non-Functional Requirements

NFR-01: The system should remain responsive for the course-scale dataset.

NFR-02: The system shall be maintainable so that core functions can be changed without rewriting the whole application.

NFR-03: Core business logic should be independently testable.

NFR-04: The system shall preserve data integrity by preventing invalid or conflicting appointment information.

NFR-05: The system should provide clear and understandable messages when input is invalid.

NFR-06: Access to patient information should be controlled according to roles or permissions once the client confirms the required access rules.

## 5. User Stories

US-01: As a receptionist, I want to create and find patient records, so that I can manage patient information efficiently.

US-02: As a receptionist, I want to create appointments, so that patients can be booked with practitioners.

US-03: As a receptionist, I want to change or cancel appointments, so that booking changes can be recorded accurately.

US-04: As a practitioner, I want to view my schedule, so that I can see my upcoming appointments.

US-05: As clinic management, I want appointment information to be consistent, so that the clinic has reliable records.

US-06: As a receptionist, I want the system to prevent duplicate practitioner/time bookings, so that appointment conflicts are avoided.

## 6. Acceptance Criteria

### AC-01 – Create Appointment

GIVEN a valid patient and practitioner exist  
WHEN the receptionist creates an appointment for an available time  
THEN the appointment is recorded and can be viewed.

### AC-02 – Prevent Duplicate Booking

GIVEN a practitioner already has an appointment at a particular time  
WHEN the receptionist tries to create another appointment for the same practitioner and time  
THEN the system rejects the conflicting booking.

### AC-03 – Cancel Appointment

GIVEN an existing appointment is recorded  
WHEN an authorised staff member cancels the appointment  
THEN the appointment status is updated to cancelled and remains available in the appointment history, subject to client confirmation.

## 7. Assumptions and Open Questions

- What exact patient information should the system store?
- What user roles and access permissions are required?
- What are the exact rules for changing and cancelling appointments?
- Should cancelled appointments remain in the appointment history?
- What response time is considered acceptable for patient searches?
- Are any additional appointment statuses required?

## 8. AI Requirements Review

| AI Suggestion | Evidence? | Decision | Reason | Verification |
|---|---|---|---|---|
| Prevent duplicate practitioner/time bookings | Yes | Accepted | Duplicate bookings are identified as a current problem. | Checked against the SmartCare client brief. |
| Retain cancelled appointments in history | Partial | Modified / Provisional | Limited appointment history is identified as a problem, but retention of cancelled appointments is not specifically confirmed. | Requires client confirmation. |
| Add SMS reminders | No | Unverified | SMS reminders are not mentioned in the client brief. | Requires client validation before becoming a requirement. |
| Add facial-recognition login | No | Rejected | There is no client evidence supporting facial recognition. | Rejected as unsupported and out of scope. |
| Add online payment | No | Rejected | Online payment is not part of the stated SmartCare scope. | Rejected as unsupported. |
| Add AI treatment recommendations | No | Rejected | Treatment recommendations are not part of the stated requirements. | Rejected as out of scope. |

### Review Outcome

The AI review was useful for identifying ambiguity and requirements that needed further clarification. However, AI suggestions were not treated as confirmed requirements unless they were supported by evidence from the SmartCare client brief. Unsupported suggestions were rejected or kept unverified until they could be confirmed with the client.

