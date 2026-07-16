from plugins.basic_plugin import BasicPlugin

points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
convex_hull = BasicPlugin.convex_hull(points)
print(convex_hull)
