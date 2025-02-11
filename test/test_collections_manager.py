import nose2
from qgis.testing import start_app, unittest

from qgis_resource_sharing.collection_manager import CollectionManager


class TestCollections(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        start_app()

    def test_get_collection_id(self):
        """Testing get_collection_id."""
        collections_manager = CollectionManager()
        collection_name = "Westeros Map"
        repository_url = "https://github.com/john.doe/my_map"
        collection_id = collections_manager.get_collection_id(
            collection_name, repository_url
        )
        expected_id = "01ece258a505a060830bcecce29f16333f706538"
        self.assertEqual(collection_id, expected_id)


if __name__ == "__main__":
    nose2.main()
