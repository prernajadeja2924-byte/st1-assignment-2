class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def create_record(self):
        pass

    def view_information(self):
        pass


class Practitioner:
    def __init__(self, practitioner_id, name, availability=None):
        self.practitioner_id = practitioner_id
        self.name = name
        self.availability = availability

    def view_information(self):
        pass

    def view_schedule(self):
        pass


class Appointment:
    def __init__(self, appointment_id, patient, practitioner, appointment_time, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.appointment_time = appointment_time
        self.status = status

    def create_appointment(self):
        pass

    def change_appointment(self):
        pass

    def cancel_appointment(self):
        pass

    