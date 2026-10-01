
class Practitioner:
    """Represents a practitioner in the SmartCare system."""

    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be empty")

        if not specialty.strip():
            raise ValueError("Practitioner specialty cannot be empty")

        if not name.strip():
            raise ValueError("Practitioner name cannot be empty")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def create_record(self):
        return {
            "practitioner_id": self.practitioner_id,
            "name": self.name,
            "specialty": self.specialty
        }

    def view_information(self):
        return (
            f"Practitioner ID: {self.practitioner_id}, "
            f"Name: {self.name}, "
            f"Specialty: {self.specialty}"
        )