"""
Two distinct problems: detecting a cycle and then finding the start of the cycle assuming there is one
if just detecting a cycle, need to put the fast pointer 1 ahead of slow,
but if we know there is a cycle, we don't do that
"""

def floyds1(nums: list):
    if not detect_cycle(nums):
        return -1

    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


def detect_cycle(nums: list):
    slow, fast = 0, 1
    while fast < len(nums) and nums[fast] < len(nums):
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            return True

    return False


if __name__ == "__main__":
    array = [1, 2, 9, 3, 4, 6, 7, 5, 5, 8]
    print(floyds1(array))
