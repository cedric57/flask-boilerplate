"""
Unit tests for the domain entities.

These tests ensure that the domain entities behave as expected and that their
business logic is correctly implemented.
"""

import unittest
import uuid
from src.flask_boilerplate.domain.entities.example_entity import ExampleEntity


class TestExampleEntity(unittest.TestCase):
    """
    Test suite for the ExampleEntity class.
    """

    def setUp(self) -> None:
        """
        Set up test fixtures, if any.
        """
        self.entity_id = uuid.uuid4()
        self.entity = ExampleEntity(id=self.entity_id, name="Test Entity", value=42)

    def test_entity_initialization(self) -> None:
        """
        Test that an ExampleEntity is correctly initialized.
        """
        self.assertEqual(self.entity.id, self.entity_id)
        self.assertEqual(self.entity.name, "Test Entity")
        self.assertEqual(self.entity.value, 42)

    def test_entity_equality(self) -> None:
        """
        Test that two entities with the same ID and attributes are considered equal.
        """
        another_entity = ExampleEntity(id=self.entity_id, name="Test Entity", value=42)
        self.assertEqual(self.entity, another_entity)

    def test_entity_inequality(self) -> None:
        """
        Test that two entities with different IDs or attributes are not considered equal.
        """
        different_entity = ExampleEntity(id=uuid.uuid4(), name="Different Entity", value=99)
        self.assertNotEqual(self.entity, different_entity)

    def test_entity_hash(self) -> None:
        """
        Test that the hash of an entity is based on its ID and attributes.
        """
        self.assertEqual(hash(self.entity), hash((self.entity.id, self.entity.name, self.entity.value)))


if __name__ == '__main__':
    unittest.main()
