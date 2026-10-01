
class Patient:
    """Represents a patient in the SmartCare system."""

    def __init__(self, patient_id: str, name: str):
        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty")

        if not name.strip():
            raise ValueError("Patient name cannot be empty")

        self.patient_id = patient_id
        self.name = name

    def create_record(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name
        }

    def view_information(self):
        return f"Patient ID: {self.patient_id}, Name: {self.name}"