class Solution {
    public int[] plusOne(int[] digits) {
        int temp = 0;
        for(int num: digits){
            temp = temp * 10 + num;
        }
        temp += 1;
        int tempLength = (int)(Math.log10(temp)+1);
        int[] nums = new int[tempLength];
        for(int i = tempLength-1;i>=0;i--){
            nums[i] = temp % 10;
            temp /= 10;
        }
        return nums;
    }
}