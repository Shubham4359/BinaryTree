class DSU:
    def __init__(self, n) -> None:
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        return self.parent[x] = self.find(self.parent[x])

    def merge(self, x, y):
        xset = self.find(x)
        yset = self.find(y)

        if xset == yset:
            return

        if self.rank[xset] < self.rank[yset]:
            self.parent[xset] = yset
            self.rank[yset]+=self.rank[xset]
        elif self.rank[xset] >= self.rank[yset]:
            self.parent[yset] = xset
            self.rank[xset]+=self.rank[yset]


def main():
    number_of_cities, number_of_roads = map(int, input().split())

    edges = []

    for _ in range(number_of_roads):
        edges.append(list(map(int, input().split())))

    edges.sort(key=lambda x: x[2])

    dsu = DSU(number_of_cities)

    total_weight = 0

    for u, v, c in edges:
        if dsu.find(u - 1) != dsu.find(v - 1):
            dsu.merge(u - 1, v - 1)
            total_weight += c

    parent = dsu.find(0)

    for i in range(1, number_of_cities):
        if dsu.find(i) != parent:
            print("IMPOSSIBLE")
            return

    print(total_weight)


if __name__ == "__main__":
    main()
