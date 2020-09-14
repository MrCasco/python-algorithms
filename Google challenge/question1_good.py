"""
Given a time (in 24-hour format) with missing digits marked as '?', we want to replace all of the question marks by the same digit (0-9) in such a way as to obtain the latest possible time. The earliest valid time is 00:00 and the latest valid time is 23:59.

Write a function: class Solution { public String solution(String T); }

that, given a string T, returns the latest valid time as a string in the format "HH:MM", where HH denotes an hour in a two-digit 24-hour format and MM denotes minutes in a two-digit format.

Examples:

1. Given T = "2?:?8", the function should return "23:38".

2. Given T = "1?:?2", the function should return "15:52".

3. Given T = "??:??", the function should return "22:22".

4. Given T = "06:34", the function should return "06:34".

5. Given T = "1?:33", the function should return "19:33".

Assume that:

    T consists of exactly five characters; the third one is ':'; the others are digits (0-9) or '?';
    there always exists a valid time obtained by substituting '?' with digits.


In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

import sys

def solution(T):
  if not '?' in T:
    return T
  # if '?' == T[0]:
  #   return T.replace('?', '2')

  digit = 9
  valid = lambda dig: True if int(T[:2].replace('?', str(dig))) < 24 and int(T[3:].replace('?', str(dig))) < 60 else False

  while not valid(digit):
    digit -= 1

  sys.stderr.write(
      "Tip: Use sys.stderr.write() to write debug messages on the output tab.\n"
  )
  return T.replace('?', str(digit))

print(solution('?5:3?'))
