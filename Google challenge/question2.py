"""
There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.
Write a function that, given an array A of N integers, of which represents loads caused by successive processes, the function should return the minimum absolute difference of server loads.
For example, given array A such that:
  A[0] = 1
  A[1] = 2
  A[2] = 3
  A[3] = 4
  A[4] = 5
your function should return 1. We can distribute the processes with loads 1, 2, 4 to the first server and 3, 5 to the second one, so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.
Assume that:
    N is an integer within the range [1..1,000]
    the sum of the elements of array A does not exceed 100,000
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""

# CODE
# Tests:
# 1,2,3,4,5 = 1
# 5,6,7,8,12,25 = 1
# 14,24,42,50 = 2

import sys

def solution(A):
  s1 = 0
  s2 = 0
  suma = sum(A)
  if suma%2 == 0:
    g1 = suma/2
  else:
    g1 = int(suma/2) + suma%2
    g2 = g1-1

  s1 = max(A)
  A.remove(max(A))
  s2 = max(A)
  A.remove(max(A))

  for i in range(len(A)):
    if (s1 == g1 or s2 == g1) and g1-g2 == 0:
      return 0
    if s1 + max(A) > g1:
      s2 += max(A)
      A.remove(max(A))
    else:
      s1 += max(A)
      A.remove(max(A))
  return abs(s1-s2)


def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
