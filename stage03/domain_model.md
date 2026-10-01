# SmartCare v0.3 – Domain Model

## A. Requirements Review

### Important Nouns
- Patient
- Practitioner
- Appointment
- Appointment status
- Appointment history
- Practitioner schedule
- Practitioner availability

### Important Verbs
- Create patient record
- Search for patient
- View patient information
- Create appointment
- View appointment
- Change appointment
- Cancel appointment
- Record appointment status
- Record and view practitioner information
- View practitioner schedule and availability
- Prevent duplicate bookings
- Retain appointment history

### Business Rules
- A patient must exist before an appointment can be created.
- A practitioner must exist before an appointment can be created.
- A practitioner must not have two appointments at the same time.
- Appointment status must be recorded consistently.
- Cancelled appointments remaining in appointment history is provisional and requires client confirmation.
- Access rules for patient information require client confirmation.

## B. Candidate Classes

| Candidate | Class? | Reason |
|---|---|---|
| Patient | Yes | A patient is a main domain entity with information and relationships to appointments. |
| Practitioner | Yes | A practitioner is a main domain entity who has appointments and availability. |
| Appointment | Yes | An appointment is a main domain entity connecting a patient, practitioner and appointment time. |
| Name | No | Name is better represented as an attribute of Patient or Practitioner rather than a separate class. |
| Clinic | Not currently | The confirmed requirements focus on managing patients, practitioners and appointments. A separate Clinic class is not currently necessary. |
| Database | No | A database is a technical implementation detail, not a SmartCare domain concept. |
| Cancellation | No | Cancellation can be represented as an appointment status or behaviour rather than a separate class at this stage. |
| Status | No | Status can be represented as an attribute of Appointment rather than a separate class. |

## C. CRC Cards

### Patient

**Responsibilities**
- Store patient information.
- Provide patient information when searched or viewed.
- Be associated with the patient's appointments.

**Collaborators**
- Appointment

### Practitioner

**Responsibilities**
- Store practitioner information.
- Provide practitioner information when viewed.
- Maintain schedule or availability information.
- Be associated with practitioner appointments.

**Collaborators**
- Appointment

### Appointment

**Responsibilities**
- Store appointment date and time.
- Connect a patient with a practitioner.
- Store appointment status.
- Support appointment changes and cancellation.
- Prevent conflicting practitioner/time bookings.

**Collaborators**
- Patient
- Practitioner

## D. Relationship Reasoning

### Patient to Appointment

A Patient can have zero or many Appointments, while each Appointment is associated with one Patient.

**Multiplicity:**  
Patient `1` ---- `0..*` Appointment

### Practitioner to Appointment

A Practitioner can have zero or many Appointments, while each Appointment is associated with one Practitioner.

**Multiplicity:**  
Practitioner `1` ---- `0..*` Appointment

### Should Appointment inherit from Patient?

No. Appointment should not inherit from Patient because an appointment is not a type of patient. They are separate domain concepts. Appointment should instead be associated with Patient.

### Does Clinic need to own every object?

No. A Clinic class is not currently necessary because the confirmed requirements focus on Patient, Practitioner and Appointment. Adding Clinic as an owner of every object would introduce unnecessary complexity without clear requirement evidence.

## E. UML Class Diagram

### Patient

**Attributes**
- patient_id
- name

**Operations**
- create_record()
- view_information()

### Practitioner

**Attributes**
- practitioner_id
- name
- availability

**Operations**
- view_information()
- view_schedule()

### Appointment

**Attributes**
- appointment_id
- appointment_time
- status

**Operations**
- create_appointment()
- change_appointment()
- cancel_appointment()

### Relationships

Patient `1` -------- `0..*` Appointment

Practitioner `1` -------- `0..*` Appointment

Each Appointment is associated with exactly one Patient and exactly one Practitioner.

A Patient may have zero or many Appointments.

A Practitioner may have zero or many Appointments.

┌─────────────────────┐
│       Patient       │
├─────────────────────┤
│ patient_id          │
│ name                │
├─────────────────────┤
│ create_record()     │
│ view_information()  │
└─────────────────────┘
          1
          │
          │
        0..*
┌────────────────────────┐
│      Appointment       │
├────────────────────────┤
│ appointment_id         │
│ appointment_time       │
│ status                 │
├────────────────────────┤
│ create_appointment()   │
│ change_appointment()   │
│ cancel_appointment()   │
└────────────────────────┘
        0..*
          │
          │
          1
┌─────────────────────┐
│    Practitioner     │
├─────────────────────┤
│ practitioner_id     │
│ name                │
│ availability        │
├─────────────────────┤
│ view_information()  │
│ view_schedule()     │
└─────────────────────┘

## F. AI Design Review

| AI Suggestion | Evidence | Decision | Reason | Model Change |
|---|---|---|---|---|
| Use Patient as a class | FR-01, FR-02, FR-03 | Accepted | Patient information must be created, searched and viewed. | Patient remains a main class. |
| Use Practitioner as a class | FR-09, FR-10 | Accepted | Practitioner information and schedules must be represented. | Practitioner remains a main class. |
| Use Appointment as a class | FR-04 to FR-08, FR-11 | Accepted | Appointments have their own time, status and behaviours. | Appointment remains a main class. |
| Create a separate Status class | FR-08 | Modified | Status is required, but it is simple enough to be an Appointment attribute at this stage. | Status remains an attribute. |
| Add NotificationManager | No confirmed requirement | Rejected | Notifications are not supported by the confirmed SmartCare requirements. | No class added. |
| Add ScheduleEngine | FR-10 partially relates to schedules | Rejected | Viewing availability does not provide enough evidence for a separate scheduling engine. | No class added. |

## G. Model-Code Consistency Check

The Python class skeletons were compared with the UML domain model.

- Patient exists in both the UML model and Python code.
- Practitioner exists in both the UML model and Python code.
- Appointment exists in both the UML model and Python code.
- The main attributes identified in the UML are represented in the Python classes.
- Appointment references both Patient and Practitioner, which is consistent with the UML associations.
- The operations in the UML are represented as method skeletons in the Python classes.
- The Python file was executed successfully with no syntax errors.

Therefore, the Python class skeletons are consistent with the current SmartCare domain model.

