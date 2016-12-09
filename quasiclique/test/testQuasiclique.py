import unittest
from quasiclique import QuasiClique

class TestQuasiclique(unittest.TestCase):

    def setUp(self):
        self.quasiclique = QuasiClique.QuasiClique()

    def test_coieficOf(self):
        temp_adj_matrix = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0]]

        temp_nodes = [0, 1, 2, 3]
        expected_resp = False

        resp = self.quasiclique.coieficOf(temp_adj_matrix, temp_nodes)

        self.assertEqual(expected_resp, resp)
