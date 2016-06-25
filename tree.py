class Range(object):
    """
    Represents an open one dimensional range between low and high.
    """

    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __contains__(self, point):
        return self.low <= point < self.high

    def __repr__(self):
        return 'Range({}, {})'.format(self.low, self.high)

    def split(self):
        incr = (self.high - self.low) / 2
        for i in range(2):
            yield Range(self.low + incr * i, self.low + incr * (i + 1))


class Tree(object):
    """
    A realy simple space partitioning tree. That covers the volume
    [low, high)
    """

    def __init__(self, region, depth=0, max_depth=2):
        """
        Builds an instance of tree at a particular depth, it also adds
        children.
        """
        self.region = region
        self.depth = depth
        self.max_depth = max_depth
        self.children = []
        self.data = []
        self._ad_children()

    def _ad_children(self):
        if self.depth < self.max_depth:
            for sub_region in self.region.split():
                self.children.append(
                    Tree(
                        sub_region,
                        depth=self.depth + 1,
                        max_depth=self.max_depth
                    )
                )

    def contains(self, point):
        """
        Computes if a point is inside or outside the tree's region.
        """
        return point in self.region

    def add(self, point):
        """
        Add new data to the tree.
        """
        if self.contains(point):
            self.data.append(point)
            for child in self.children:
                child.add(point)

    def print_to_screen(self):
        """
        Prints the tree to the screen in text form.
        """
        spacing = '   ' * self.depth
        print(spacing,
              '-> me at depth {}'.format(self.depth))
        print(spacing,
              '   lie in te region {}'.format(self.region))
        print(spacing,
              '   contain {} data points'.format(len(self.data)))
        for child in self.children:
            child.print_to_screen()


if __name__ == "__main__":
    tree = Tree(Range(0, 8), max_depth=2)
    tree.add(1)
    tree.print_to_screen()
    assert tree.contains(3)
    assert not tree.contains(10)
    print('Everything working nicely')
