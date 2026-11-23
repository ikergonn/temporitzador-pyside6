import unittest

from gestor_incidencies.models import IncidentFilters, Priority, Status
from gestor_incidencies.repository import JsonIncidentRepository
from gestor_incidencies.services import IncidentService, IncidentValidationError
from .support import cleanup_test_path, make_test_repo_path


class IncidentServiceTest(unittest.TestCase):
    def test_create_filter_and_close_incident(self) -> None:
        path = make_test_repo_path()
        self.addCleanup(cleanup_test_path, path)
        service = IncidentService(JsonIncidentRepository(path))
        service.create_incident(
            title="No es desa el formulari",
            category="formulari",
            priority=Priority.CRITICAL,
            tags=["UI", "UI", "Dades"],
        )

        filtered = service.list_incidents(
            IncidentFilters(text="formulari", priority=Priority.CRITICAL)
        )

        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered[0].tags, ["ui", "dades"])

        closed = service.close_incident(filtered[0].id)
        self.assertEqual(closed.status, Status.CLOSED)

    def test_rejects_empty_title(self) -> None:
        path = make_test_repo_path()
        self.addCleanup(cleanup_test_path, path)
        service = IncidentService(JsonIncidentRepository(path))
        with self.assertRaises(IncidentValidationError):
            service.create_incident(title="   ")

    def test_normalizes_text_priority_and_creates_open_incident(self) -> None:
        path = make_test_repo_path()
        self.addCleanup(cleanup_test_path, path)
        service = IncidentService(JsonIncidentRepository(path))

        incident = service.create_incident(title="Prioritat des del formulari", priority="alta")

        self.assertEqual(incident.priority, Priority.HIGH)
        self.assertEqual(incident.status, Status.OPEN)
        self.assertEqual(JsonIncidentRepository(path).get(incident.id).priority, Priority.HIGH)


if __name__ == "__main__":
    unittest.main()
