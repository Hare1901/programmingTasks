" Тут будут решения задач с литкода(medium, hard) и кодварса(6-5-4 kuy)"

def alphabet_position(text):
    """
                          Codewars 6 kuy
                          Name : Replace With Alphabet Position
    :param text: string
    :return: string
    """

    alp = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(alp.find(c) + 1) for c in text.lower() if c in alp])


def first_non_repeating_letter(string):
    """
                           Codewars: 5 kuy
                           Name: First non-repeating character
    :param string: string
    :return: string
    """
    a = [i for i in string if string.lower().count(i.lower()) == 1]
    if len(a) > 0:
        return a[0]
    else:
        return ''


def make_readable(seconds):
    """
                           Codewars: 5 kuy
                           Name: Human Readable Time
    :param seconds: int
    :return:
    """
    return f'{str(seconds//3600).rjust(2, "0")}:{str(seconds//60%60).rjust(2, "0")}:{str(seconds%60).rjust(2, "0")}'


def sum_of_intervals(intervals):
    """
                          Codewars 4 kuy
                          Name: Sum of Intervals
    :param intervals: [[int]]
    :return:
    """
    if not intervals:
        return 0
    sum = 0
    intervals.sort(key = lambda e: e[0])
    cursor = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= cursor[1]:
            cursor = (cursor[0], max(cursor[1], intervals[i][1]))
        else:
            sum += cursor[1] - cursor[0]
            cursor = intervals[i]
    sum += cursor[1] - cursor[0]
    return sum


def move_zeros(lst):
    """
                            Codewars 5 kuy
                            Name: Moving Zeros To The End
    :param lst: [int]
    :return: [int]
    """
    a = [i for i in lst if i!=0]
    return a + [0] * (len(lst) - len(a))

class Solution(object):
    """
                            LeetCode
                            Name: 2444. Count Subarrays With Fixed Bounds
                            lvl: Hard
    """
    def countSubarrays(self, nums, minK, maxK):
        """
        :type nums: List[int]
        :type minK: int
        :type maxK: int
        :rtype: int
        """
        j1 = j2 = k = -1
        ans = 0
        for i, v in enumerate(nums):
            if v < minK or v > maxK:
                k = i
            if v == minK:
                j1 = i
            if v == maxK:
                j2 = i
            ans += max(0, min(j1, j2) - k)
        return ans