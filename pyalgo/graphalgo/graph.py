"""Graph representation."""
from typing import List, Tuple, Optional
from collections import defaultdict


class Graph:
    # TODO: support edges orientation
    def __init__(self,
                 edges: Optional[List[Tuple[int, int]]] = None,
                 matrix: Optional[List[List[int]]] = None):
        if edges is not None and matrix is not None:
            raise ValueError("`edges` and `matrix` can't be provided together")
        self._edges = defaultdict(list)
        if edges is not None:
            for start, end in edges:
                self._edges[start].append(end)

        if matrix is not None:
            size = len(matrix)
            if size == 0:
                raise ValueError("`matrix` shouldn't be an empty matrix")
            row_sizes = {len(row) for row in matrix}
            if row_sizes != {size}:
                raise ValueError(f"`matrix` should be a square matrix "
                                 f"with {size} rows and {size} columns. "
                                 f"Found different row sizes: {row_sizes}")
            n_cols = row_sizes.pop()
            for i in range(size):
                for j in range(size):
                    if matrix[i][j] > 0:
                        self._edges[i].append(j)




