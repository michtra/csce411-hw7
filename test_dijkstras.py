import unittest
from dijkstras import dijkstra, build_graph

class TestDijkstras(unittest.TestCase):
    def test(self):
        # simple path
        edges = [
            ('A', 'B', 1),
            ('B', 'C', 3)
        ]

        graph = build_graph(edges)
        distances, paths = dijkstra(graph, 'A')

        # verify distances
        self.assertEqual(distances['A'], 0)  # to itself is 0
        self.assertEqual(distances['B'], 1)  # to B is 1
        self.assertEqual(distances['C'], 4)  # to C is 1 + 3 = 4

        # verify paths: only one path possible from A
        self.assertEqual(paths['A'], ['A'])
        self.assertEqual(paths['B'], ['A', 'B'])
        self.assertEqual(paths['C'], ['A', 'B', 'C'])


if __name__ == "__main__":
    unittest.main()
