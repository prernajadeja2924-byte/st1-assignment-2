

# Stage 04 Reflection

In this stage, I implemented the Patient and Practitioner classes using type hints and basic validation. I also used the class design from the previous stage to keep the code organised.

AI was used for the Appointment class as allowed in the activity. I reviewed the AI-generated code before using it. The Appointment class uses Patient and Practitioner objects and an AppointmentStatus enum. The status is protected so that it can only be changed through the appropriate methods.

I manually tested the program by creating a patient, practitioner and appointment. I tested a valid appointment, cancellation and an invalid transition. The invalid transition correctly produced an error when I tried to cancel an already cancelled appointment.

During refactoring, I improved the formatting, naming and readability of the code. I also fixed several indentation and syntax errors. This stage helped me understand how classes can work together and why validation and controlled state changes are important.

