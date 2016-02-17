# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 22:20:33 2016

@author: Adam Zelenka
"""
import unittest

class NodeTest(unittest.TestCase):
    """Creates a test for the Node class.
    """
    def __init__(self):
        """Constructor does nothing and is therefore left blank.
        """
    def setUp3(self):
        """Creates a fresh Node object with three defined coordinates
        """
        myNode = Node(0, [1.,2.,3.]);
        
    def setUp2(self):
        """Creates a fresh Node object with two defined coordinates
        """
        myNode = Node(0, [1.,2.]);
    
    def setUp1(self):
        """Creates a fresh Node object with one defined coordinate
        """
        nyNode = Node(0, [1.]);
        
    def setUp0(self):
        """Creates a fresh Node object with no defined coordinates
        """
        myNode = Node(0, []);
        
    def testLengths(self):
        """Tests to see if created Nodes have correctly defined coordinates
        """
        setUp0();
        self.assertEqual([0.,0.,0.], myNode.x)