class Person:
    def __init__(self, name="", job=""):
        self._name = name
        self._job = job
    def name(self):
        return self._name
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be a string between 1 and 25 characters.")
    def job(self):
        return self._job
    def job(self, value):
        APPROVED_JOBS = [
            "Admin",
            "Customer Service",
            "Human Resources",
            "ITC",
            "Production",
            "Legal",
            "Finance",
            "Sales",
            "General Management",
            "Research & Development",
            "Marketing",
            "Purchasing"
        ]

        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in the list of approved jobs.")


