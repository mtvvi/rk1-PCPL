import unittest
from main import Computer, OperatingSystem, ComputersOS, get_one_to_many, get_many_to_many, task_1, task_2, task_3


class TestComputers(unittest.TestCase):

    def setUp(self):
        self.oses = [
            OperatingSystem(1, 'Windows'),
            OperatingSystem(2, 'Linux'),
            OperatingSystem(3, 'macOS'),
            OperatingSystem(11, 'Windows Server'),
            OperatingSystem(22, 'Ubuntu'),
        ]

        self.computers = [
            Computer(1, 'PC1', 1000, 1),
            Computer(2, 'PC2', 1200, 1),
            Computer(3, 'PC3', 900, 11),
            Computer(4, 'PC4', 1500, 3),
            Computer(5, 'PC5', 1100, 2),
        ]

        self.computers_os = [
            ComputersOS(1, 1),
            ComputersOS(1, 2),
            ComputersOS(2, 3),
            ComputersOS(2, 5),
            ComputersOS(3, 4),
            ComputersOS(11, 1),
            ComputersOS(22, 3),
        ]

    def test_task_1(self):
        result = task_1(self.oses, self.computers)
        expected = {
            'Windows': ['PC1', 'PC2'],
            'Windows Server': ['PC3']
        }
        self.assertEqual(result, expected)

    def test_task_2(self):
        one_to_many = get_one_to_many(self.oses, self.computers)
        result = task_2(self.oses, one_to_many)
        expected = [('macOS', 1500), ('Windows', 1200), ('Linux', 1100), ('Windows Server', 900)]
        self.assertEqual(result, expected)

    def test_task_3(self):
        result = task_3(self.oses, self.computers, self.computers_os)
        expected = {
            'Linux': ['PC3', 'PC5'],
            'Ubuntu': ['PC3'],
            'Windows': ['PC1', 'PC2'],
            'Windows Server': ['PC1'],
            'macOS': ['PC4']
        }
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
