import io
import sys
import unittest
from unittest.mock import MagicMock, patch
from datetime import datetime, timedelta
from cleanup_old_deployments import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.stdout = sys.stdout
        self.mock_stdout = sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = self.stdout

    def test_main_with_dry_run(self):
        mock_boto = MagicMock()
        mock_response = { # just a mock not beeing passed in
            'Contents': [
                {
                    'Key': 's3-vidhya-test/klljkjkl123/',
                    'LastModified': datetime(2023, 4, 24, 10, 0, 0),
                },
            ]
        }
        mock_boto.list_objects_v2.return_value = mock_response

        expected_output = 'Deleting klljkjkl123/\n'
        with patch('sys.argv', ['cleanup_old_deployment.py', '4', '--dry-run']), \
            patch('boto3.client', return_value=mock_boto):
            main(dry_run=True)
        self.assertEqual(self.mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
