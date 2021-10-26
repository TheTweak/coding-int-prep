'''
You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project depends on a first). All of a project dependencies must be built before the project is. Find a build order that will allow the project to be built. If there is no such order, return an error.

Example:

projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
output: f, e, a, b, d, c

Solution:

1) create a directed graph
2) iterate over each node:
    - if node doesn't have any outgoing edge, add it to output
    - if node has outgoing edges:
        - make DFS
        - when reaches node without outgoing edges, add it to ouput
        - add node itself
time: O(N)=P+D
space: O(N)=P
'''
from collections import deque

class Project:
    def __init__(self, name: str):
        self.name = name
        self.dependencies = []

class ProjectGraph:
    def __init__(self, projects: list[Project]):
        self.projects = projects


def create_build_order(pg: ProjectGraph) -> list[str]:
    built = set()
    result = []
    stack = deque()
    for p in pg.projects:
        stack.append(p)

        while len(stack):
            p = stack[-1]
            try:
                if stack.index(p, 0, -1):
                    raise RuntimeError('cycle detected in a graph')
            except ValueError:
                pass

            if p.name in built:
                stack.pop()
                continue

            all_deps_built = True
            for dp in p.dependencies:
                if not dp.name in built:
                    all_deps_built = False
                    stack.append(dp)

            if all_deps_built:
                stack.pop()
                result.append(p.name)
                built.add(p.name)

    return result


if __name__ == '__main__':
    projects_map = {}
    for n in ['a', 'b', 'c', 'd', 'e', 'f']:
        projects_map[n] = Project(n)
    projects_map['d'].dependencies.append(projects_map['a'])
    projects_map['b'].dependencies.append(projects_map['f'])
    projects_map['d'].dependencies.append(projects_map['b'])
    projects_map['a'].dependencies.append(projects_map['f'])
    projects_map['c'].dependencies.append(projects_map['d'])
    projects_map['d'].dependencies.append(projects_map['c'])
    pg = ProjectGraph([p for _, p in projects_map.items()])
    build_order = create_build_order(pg)
    print(*build_order)
    assert ['f', 'e', 'a', 'b', 'd', 'c'] == build_order
