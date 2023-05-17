import unittest
import maze.obstacles as obstacles

class MyTestCase(unittest.TestCase):
    def test_find_obstacles(self):
        obstacles.random.randint=lambda a,b:1
        output = obstacles.find_obstacles()

        self.assertEqual([(1,1)],output)

    def test_position_closed(self):
        obstacles.random.randint=lambda a,b:0
        output = obstacles.find_obstacles()

        self.assertEqual([(1,1)],output)

    def test_path_closed(self):
        obstacles.random.randint=lambda a,b:1

        output = obstacles.path_closed(0,0,10,0)
        self.assertFalse(output)




if __name__ == "__main__":
    unittest.main()