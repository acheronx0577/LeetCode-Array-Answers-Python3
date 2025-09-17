class solution:
    def hades(self, nums: list[int], target: int):
        seen = {} # Create a hash table first to store the list 
        for i in range(len(nums)): # This is the loop will start with i which is 0, in len(nums) means it will count how many numbers in a list then the range(list(nums)) will take that and know the order of the index in the list so lets say 4 numbers and start with 0, 1, 2, 3 so in total there are 4 numbers and so on.

            aella = target - nums[i] # Now after we got the hash table and the loop we need something to calculate and the method o(n*2) is not good because of the time it consume to calculate every posibiliies to equal the target number, so instead we take the target number and minus to one of the numbers in the list thats given and use that as the method to save so much time!

            if aella in seen: # Okay so after we got the number we want to check the other number in the list so we put it to in the hash table to check it and give us the answer if its in the hash table.

                # If the number is seen inside the hash table it will give us the sum which is aella and, i which is index number of that sum so lets saythe target is 13 and the list is [5, 8, 12, 17] we take the first number which is 5 and the index number is 0 the reason it's 0 is range(len(nums)), so reread if you don't understand, so when 13 - 5 = 8, 8 is the sum which is aella in this case now because in the first loop its going to be empty inside the dictionary so it will run the else which is false instead and save it as a key inside that hash table as nums[i] = 5 = 0(i is index) now it will go to the next number which is 8 so 13 - 8 = 5, now because 5 is already saved in the hash table as the first number so this will trigger as true and return as seen[5] = 0 and 8 is going to be seen[8] = 1 so the answer is going to be [0, 1] as 8 + 5 = 13
                return [seen[aella], i]
            else:
                seen[nums[i]] = i

sol = solution()
print(sol.hades([5, 8, 12, 17], 13))
print(sol.hades([4, 6, 9, 3], 12))
print(sol.hades([7, 7, 2, 1], 14))
