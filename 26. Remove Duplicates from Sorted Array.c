int removeDuplicates(int* nums, int numsSize)
{
    if(numsSize == 0)
        return 0;
    for(int i = 0; i < numsSize; i++)
    {
        for(int j = i; j < numsSize; j++)
        {
            if(nums[j] > nums[i])
            {
                nums[i + 1] = nums[j];
                break;
            }
                
        }
    }
    int i = 0;
    for(i = 0; i < numsSize - 1; i++)
    {
        if( nums[i+1] <= nums[i] )
        {
            return i + 1;
        }
    }
    return i + 1;
}