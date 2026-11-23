import unittest

from gestor_incidencies.models import Incident, Priority
from gestor_incidencies.repository import JsonIncidentRepository
from .support import cleanup_test_path, make_test_repo_path


class JsonIncidentRepositoryTest(unittest.TestCase):
    def test_add_list_update_and_delete_incidents(self) -> None:
        path = make_test_repo_path()
        self.addCleanup(cleanup_test_path, path)
        repository = JsonIncidentRepository(path)
        incident = Incident(
            id=repository.next_id(),
            title="Prova",
            priority=Priority.HIGH,
        )

        repository.add(incident)
        self.assertEqual(len(repository.list_all()), 1)
        self.assertEqual(repository.get("INC-0001").title, "Prova")

        incident.title = "Prova editada"
        repository.update(incident)
        self.assertEqual(repository.get("INC-0001").title, "Prova editada")

        repository.delete("INC-0001")
        self.assertEqual(repository.list_all(), [])


if __name__ == "__main__":
    unittest.main()
