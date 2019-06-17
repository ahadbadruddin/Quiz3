#!/usr/bin/env python3
from unittest import TestCase
from FizzBuzzQuiz import FizzBuzzer

class testFizzBuzz(TestCase):

    def testDefaultValue(self):
        x= FizzBuzzer()
        self.assertEqual(x.number,0,"checks to see if default number is set to 0")
    
    def testNext(self):
        x= FizzBuzzer()
        self.assertEqual(x.next(), "1", "returns the string \'1\' ")
        x= FizzBuzzer(2)
        self.assertEqual(x.next(),"fizz", "returns fizz because 3 is divisble by 3")
        self.assertEqual(x.next(),"4","returns 4 because 4 is not divisble by 3 or 5")
