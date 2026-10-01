# SmartCare Stage 4 - Design Review

## Activity 1 - Encapsulation Review

### Patient

**Protected state / invariant**
- patient_id
- name
- Patient name must not be empty.

**Public operations**
- create_record()
- view_information()

### Practitioner

**Protected state / invariant**
- practitioner_id
- name
- specialty
- Practitioner name must not be empty.

**Public operations**
- view_information()

### Appointment

**Protected state / invariant**
- appointment_id
- patient
- practitioner
- appointment_time
- status
- Appointment must have a valid patient and practitioner.
- Appointment status changes must follow the allowed transition rules.

**Public operations**
- create_appointment()
- change_appointment()
- cancel()

## Activity 2 - Composition or Inheritance?

### Appointment and Patient

**Decision:** Composition/Association

**Reason:** An Appointment has a Patient, but an Appointment is not a type of Patient. Therefore, inheritance is not appropriate.

### Appointment and Practitioner

**Decision:** Composition/Association

**Reason:** An Appointment is associated with a Practitioner, but an Appointment is not a type of Practitioner.

### Doctor and Practitioner (Hypothetical)

**Decision:** Inheritance

**Reason:** A Doctor could be a specialised type of Practitioner. Therefore, inheritance may be appropriate if the system requires different practitioner types.

### Clinic and Appointment

**Decision:** Composition/Association

**Reason:** A Clinic may contain or manage Appointments, but a Clinic and an Appointment are different concepts. An Appointment is not a type of Clinic.

## Activity 3 - Responsibility Allocation

### Who decides whether SCHEDULED can become CANCELLED?

The Appointment class should decide whether its status can change from SCHEDULED to CANCELLED because the status and its transition rules belong to the Appointment.

### Who validates a patient name?

The Patient class should validate the patient name because the name is part of the Patient's state.

### Should Appointment execute SQL? Why?

No. Appointment should not execute SQL. The Appointment class should focus on domain data and business rules rather than database operations.

### Should the UI decide whether a status transition is legal?

No. The UI should not decide whether a status transition is legal. The Appointment class should protect and enforce its own status transition rules.

## Activity 4 - AI Code Critique

### Problem 1 - Public status mutation
**Problem:** Appointment status can be changed directly from outside the class.

**Correction:** Protect the status and allow changes only through controlled methods such as cancel().

### Problem 2 - SQL inside cancel()
**Problem:** The Appointment class directly executes database SQL.

**Correction:** Keep database logic outside the domain class. Appointment should only manage its own state and business rules.

### Problem 3 - NotificationManager dependency
**Problem:** NotificationManager was added even though it is not part of the approved design.

**Correction:** Remove NotificationManager and implement only the responsibilities supported by the approved model.

### Problem 4 - Appointment inherits from PatientRecord
**Problem:** Appointment is not a type of PatientRecord, so this inheritance relationship is incorrect.

**Correction:** Use an association between Appointment and Patient instead of inheritance.

### Problem 5 - Status transition is not protected
**Problem:** The generated design may allow invalid status changes.

**Correction:** Appointment should enforce valid status transitions, such as allowing SCHEDULED to become CANCELLED and preventing an illegal repeated cancellation.

### Problem 6 - Too many responsibilities
**Problem:** The generated Appointment class handles domain logic, database operations and notifications.

**Correction:** Keep Appointment focused on appointment state and business rules.

