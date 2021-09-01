class Words:
    def __init__(self, string):
        self.string = string

    def __len__(self):
        return len(self.string)

    @property
    def grid(self):
        return sorted(set(self.string))

    @property
    def unique_len(self):
        return len(self.grid)

    def contains_char(self, char):
        return char in self.grid

    def is_subset(self, quest_grid):
        return all(char in quest_grid for char in self.grid)

    def is_solution(self, quest_grid, compulsory_char):
        quest_grid.add(compulsory_char)
        return self.contains_char(compulsory_char) and self.is_subset(
            quest_grid
        )

    @property
    def score(self):
        if self.unique_len == 7:
            return 7 + len(self)
        elif len(self) == 4:
            return 1
        return len(self)

    def __repr__(self):
        return self.string
