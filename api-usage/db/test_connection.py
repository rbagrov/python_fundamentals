# This file contains tests for the db connection


import unittest
from unittest.mock import patch


class ConnectionTestCase(unittest.TestCase):
    @patch('Connection.Connection.connect')
    def test_connect(self, mock_connect):
            mock_connect()
            assert mock_connect.called

    @patch('Connection.Connection.commit')
    def test_commit(self, mock_commit):
        mock_commit()
        assert mock_commit.called

    @patch('Connection.Connection.close')
    def test_close(self, mock_close):
        mock_close()
        assert mock_close.called


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ConnectionTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
