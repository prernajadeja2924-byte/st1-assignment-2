# Stage 3 Reflection

During Stage 3, I developed a domain model for the SmartCare system based on the requirements identified in Stage 2. I identified Patient, Practitioner and Appointment as the main classes because they represent the important concepts required by the system.

Creating CRC cards helped me understand the responsibilities of each class and how the classes collaborate. I also considered other possible classes such as Status, Clinic and Cancellation, but decided that they were not necessary as separate classes at this stage.

AI was useful for reviewing the proposed classes and relationships. However, I did not accept every AI suggestion. For example, classes such as NotificationManager and ScheduleEngine were not added because there was not enough evidence for them in the confirmed requirements.

The UML model helped me understand that one Patient can have many Appointments and one Practitioner can also have many Appointments. I then created Python class skeletons and compared them with the UML model. This helped me confirm that the design and code structure were consistent before implementing the full system behaviour.

