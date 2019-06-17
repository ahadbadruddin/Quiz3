#!/usr/bin/env python3

class FizzBuzzer:

    def __init__(self, start =0):
        self.number = start

    def next(self):
        self.number+=1
        if self.number%3 ==0 and self.number%5==0:
            return("fizzbuzz")
        elif self.number%3==0:
            return("fizz")
        elif self.number%5==0:
            return("buzz")
        else:
            return(f"{self.number}")

if __name__=='__main__':
    buzzer= FizzBuzzer()
    print(buzzer.next())
    print(buzzer.next())
    print(buzzer.next())
   