import pytest
from unittest.mock import Mock

from pyalgo.graphalgo import Graph


def test_graph__init__():
    # Empty graph
    g = Graph()
    assert len(g._edges) == 0

    # Both `edges` and `matrix` are passed
    with pytest.raises(ValueError, match="`edges` and `matrix` can't be "
                                         "provided together"):
        Graph(edges=Mock(), matrix=Mock())

    # List of edges
    g = Graph(edges=[(1, 1), (2, 1), (1, 3), (3, 2)])
    assert g._edges == {1: [1, 3], 2: [1], 3: [2]}

    # Adjacency matrix

    # Invalid matrix
    with pytest.raises(ValueError, match="`matrix` should be a square matrix"):
        Graph(matrix=[[1, 0]])

    g = Graph(matrix=[[1, 0, 1], [1, 1, 1], [1, 1, 0]])
    assert g._edges == {0: [0, 2], 1: [0, 1, 2], 2: [0, 1]}
