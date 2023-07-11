"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #0 - Hello World! (helloworld.py)


Author: Koneshka Bandyopadhyay

Difficulty Level: 0/10

Use this file to practice the submission format for the rest of the Code Clashes.
Create a script that takes "Hello World!" as an input and if that input is given, also returns "Hello World!".

Test Case:
Input: "Hello World!"   Output: "Hello World!"
"""

class Solution:
    def helloworld(self, string):
        # input type: String
        # return type: String
        # TODO: Write code below to return a string with the solution to the prompt
        name = string  
        return name

def main():
    tc1 = Solution()
    string1= input()
    ans = tc1.helloworld(string1)
    print(ans)

if __name__ == "__main__":
    main()