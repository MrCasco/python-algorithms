"""
There are 10 floors in a hotel (numbered from 0 to 9). On each floor there are 26 rooms, each marked with a capital letter of the English alphabet (from "A" to "Z").

You are presented with the list of reservations, which consists of N three-character strings. The first character of each string is "+" or "−", which describes whether the room was booked or freed. The second and third characters correspond to the number of the floor and letter of the room, respectively. For example, "+4C" means that room C on the 4th floor has just been booked, and "−0G" means that room G on the 0th floor has been freed.

Your task is to compute how many different rooms were booked at least once according to the list. You may assume that the list describes a correct sequence of bookings in chronological order; that is, only free rooms can be booked and only booked rooms can be freed. All rooms are initially free.

Write a function: class Solution { public int solution(String[] A); }

that, given an array A consisting of N strings, representing the reservations list, returns an integer: the number of different rooms that were booked at least once.

Examples:

    Given A = ["+0A", "+9Z", "+4F", "−9Z", "+3G"], the function should return 4. Four different rooms were booked: "0A", "9Z", "4F" and "3G".
    Given A = ["+4B", "−4B", "+4B", "−4B"], the function should return 1. Only room "4B" was booked.
    Given A = ["+4A", "+5B", "+5A"], the function should return 3. Rooms "4A", "5B" and "5A" were booked.


Assume that:

    N is an integer within the range [1..600];
    each element of array A is a string consisting of three characters: "+" or "−", a digit ("0"-"9"), and an uppercase English letter ("A"-"Z");
    the sequence is correct, that is every booked room was previously free and every freed room was previously booked.

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


"""


def solution(A):
  rooms = list(set(A))
  checkBook = lambda room: True if room[0] != '-' else False
  booked = filter(checkBook, rooms)
  return len(list(booked))
