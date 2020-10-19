class Solution {
    public int searchInsert(int[] nums, int target) {
        int i = 0;
        for(int num: nums){
            if(num >= target) {
                return i;
            }
            i++;
        }
        return i;
    }   
}