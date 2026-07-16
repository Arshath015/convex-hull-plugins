from typing import List, Tuple
import math

class OptimizedPlugin:
    @staticmethod
    def orientation(p: Tuple[float, float], q: Tuple[float, float],
                    r: Tuple[float, float]) -> int:
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    @staticmethod
    def convex_hull(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        n = len(points)
        if n < 3:
            raise ValueError("Convex hull not possible")

        hull = []
        l = 0
        for i in range(1, n):
            if points[i][0] < points[l][0]:
                l = i

        p = l
        q = 0
        while True:
            hull.append(points[p])
            q = (p + 1) % n

            for i in range(n):
                if OptimizedPlugin.orientation(points[p], points[i], points[q]) == 2:
                    q = i

            p = q

            if p == l:
                break

        return hull
