import unittest
from MNode import MNode

class MNodeTests(unittest.TestCase):
    def setUp(self):
        self.node = MNode('TestNode')

    def tearDown(self):
        self.node = None

    def testAddOptionPositive(self):
        self.node = MNode('TestNode')
        self.node.addoption(MNode('AnotherTest'))
        self.assertEqual(self.node.totalcount, 1, 'Legal node was not added.')

    def testAddOptionNegative(self):
        self.node = MNode('TestNode') 
        self.node.addoption(None)
        self.assertEqual(self.node.totalcount, 0, 'Illegal node was added.')

    def testNextPositive(self):
        self.node = MNode('TestNode')
        self.assertEqual(str(self.node.next()), '',
                'Node with no options returned a node with a non-null state.')

        self.node.addoption(MNode('ChildNode'))
        self.assertEqual(str(self.node.next()), 'ChildNode',
                'Node with only one option did not return expected option.')

if __name__ == '__main__':
    unittest.main()
