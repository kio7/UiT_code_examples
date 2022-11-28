from Dijkstra import dijkstra

class TestDijkstra:
    def setup_method(self):
        dic = {
            'A': {'C': 2, 'E': 4},
            'B': {'A': 6, 'D': 5},
            'C': {'B': 4, 'E': 14},
            'D': {'A': 3, 'C': 7},
            'E': {'B': 6, 'D': 11}
        }

        return dic
    
    def test_dijkstra(self):
        graph = self.setup_method()
        first_var, second_var = dijkstra(graph, 'C')
        assert first_var == {'A': 10, 'B': 4, 'C': 0, 'D': 9, 'E': 14}
        assert second_var == {'B': 'C', 'E': 'C', 'A': 'B', 'D': 'B'}


test = TestDijkstra()
test.test_dijkstra()
