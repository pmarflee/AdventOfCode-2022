from days import day7

class TestDay7:
    lines = [ "$ cd /",
              "$ ls",
              "dir a",
              "14848514 b.txt",
              "8504156 c.dat",
              "dir d",
              "$ cd a",
              "$ ls",
              "dir e",
              "29116 f",
              "2557 g",
              "62596 h.lst",
              "$ cd e",
              "$ ls",
              "584 i",
              "$ cd ..",
              "$ cd ..",
              "$ cd d",
              "$ ls",
              "4060174 j",
              "8033020 d.log",
              "5626152 d.ext",
              "7214296 k" ]
    def test_day7_calculate_part1(self):
        assert day7.calculate(self.lines, 1) == 95437

    def test_day7_calculate_part2(self):
        assert day7.calculate(self.lines, 2) == 24933642