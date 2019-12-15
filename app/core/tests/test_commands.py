from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandsTestCase(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # @patch('time.sleep', return_value=True) <<--salah kat TRUE
    @patch('time.sleep', return_value=None)
    def test_wait_for_db(self, ts):
        """Testing waiting for db"""

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # gi.side_effects = [OperationalError] * 5 + [True] <<< side_effect
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)

# side_effect is under unittest.mock
# under patch
# for side_effect https://docs.python.org/3/library/unittest.mock.html
