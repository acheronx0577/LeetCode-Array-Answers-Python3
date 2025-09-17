class Solution:
    def hades(self, nums: list[int], target: int):
        seen = {}  # Create a hash table first to store the list
        for i in range(len(nums)):
            """
            This is the loop that will start with i, which is 0.
            len(nums) means it will count how many numbers are in the list.
            Then range(len(nums)) will take that count and determine the index order for the list.
            For example, with 4 numbers [5, 8, 12, 17], the range(len(nums)) will be range(4),
            which generates indices 0, 1, 2, 3.
            So in total, len(nums) will recognize there are 4 numbers, and so on.
            """

            aella = target - nums[i]
            """
            Now that we have the hash table and the loop, we need something to calculate.
            The O(n²) method is not good because of the time it consumes to calculate
            every possibility to equal the target number. Instead, we take the target number
            and subtract one of the numbers from the given list, and use that as the method
            to save so much time!
            """

            if aella in seen:
                """
                Okay, so after we get the number, we want to check if the other number is in the list.
                We put it in the hash table to check and see if it's already there,
                which would give us the answer we're looking for.
                """
                return [seen[aella], i]
                """
                If the number is found inside the hash table, it will give us the complement (which is aella)
                and i, which is the index number of the current number.

                Let's say the target is 13 and the list is [5, 8, 12, 17].
                We take the first number, which is 5, and the index number is 0
                (the reason it's 0 is because of range(len(nums)) - reread the comments on top if you don't understand).

                When we calculate 13 - 5 = 8, 8 is the complement (aella in this case).
                Since in the first loop the dictionary is empty, it will execute the else statement
                (which is false for the if condition) and save it as a key in the hash table as
                nums[i] = 5:0 (where i is the index).

                Now it moves to the next number, which is 8. We calculate 13 - 8 = 5.
                Since 5 is already saved in the hash table as the first number, this will trigger
                as true and return seen[5] = 0 and the current index i = 1.
                So the answer will be [0, 1] because 5 + 8 = 13.
                """
            else:
                seen[nums[i]] = i


sol = Solution()
print(sol.hades([5, 8, 12, 17], 13))
print(sol.hades([4, 6, 9, 3], 12))
print(sol.hades([7, 7, 2, 1], 14))
