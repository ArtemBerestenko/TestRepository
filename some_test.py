# -*- coding: cp1251 -*-
import random
import unittest

from ForTest import TestedClass

def setUpModule():
    f = open("text.txt", 'a')
    f.write("start of module:\n")
    f.close()

def tearDownModule():
   f = open("text.txt", 'a')
   f.write("end of module\n")
   f.close()

testinst = TestedClass()
   
class TestSequenceFunctions(unittest.TestCase):
   
   def test_ForTest(self):
      self.assertTrue (testinst.plus(1,2) == 3)

   @classmethod
   def setUpClass(self):
      f = open("text.txt", 'a')
      f.write("start of testclass:\n")
      f.close()

   @classmethod
   def tearDownClass(self):
      f = open("text.txt", 'a')
      f.write("start of testclass\n")
      f.close()    

   def setUp(self):
      f = open("text.txt", 'a')
      f.write("start of testcase\n")
      f.close()
      self.seq = range(10)

   def tearDown(self):
      f = open("text.txt", 'a')
      f.write("end of testcase\n\n")
      f.close()

   def test_mytest(self):
      self.assertTrue(2 == 1)
   

        

   def test_shuffle(self):
       # проверяем, что перемешанная последовательность не потеряла
       # ни одного элемента
       random.shuffle(self.seq)
       self.seq.sort()
       self.assertEqual(self.seq, range(10))
       # возбуждает исключение для неизменяемых последовательностей
       self.assertRaises(TypeError, random.shuffle, (1,2,3))

   def test_choice(self):
       element = random.choice(self.seq)
       self.assertTrue(element in self.seq)

   def test_sample(self):
       with self.assertRaises(ValueError):
           random.sample(self.seq, 20)
       for element in random.sample(self.seq, 5):
           self.assertTrue(element in self.seq)



