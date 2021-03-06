# Purpose of Depth first search is (mainly from my understanding) to find if a graph G is connected.
# Identify all nodes that are reachable from a given starting node.

# Programmed by Aladdin Persson <aladdin.persson at hotmail dot com>
#   2019-02-16 Initial programming

# Improvements:
#   * Check implementation with stack/queue

def load_graph(file='exgraph.txt'):
    data = open(file, 'r')
    G = {}

    for line in data:
        lst = [int(x) for x in line.split()]
        G[lst[0]] = lst[1:]

    num_nodes = len(G)

    return G, num_nodes


def DFS(curr_node):
    if visited[curr_node - 1]:
        return

    visited[curr_node-1] = True

    # G is a dictionary
    neighbours = G[curr_node]

    for next_node in neighbours:
        DFS(next_node)

if __name__ == '__main__':
    print('Loading graph and print:')

    try:
        G, num_nodes = load_graph()
        print(G)

    except TypeError:
        raise("Error loading graph.")

    visited = [False for i in range(1, num_nodes + 1)]
    start_node = 1

    DFS(start_node)

    if any(visited) == False:
        print("Result: This graph is connected!")