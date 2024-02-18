
def moveZeroes(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums[0]
        else:
            counter = 0
            nums = sorted(nums)
            for idx, item in enumerate(nums):
                if item == 0:
                    counter = counter + 1
                    nums.append(0)
                else:
                    break
        del nums[counter:]
moveZeroes([0,1,0,3,12])