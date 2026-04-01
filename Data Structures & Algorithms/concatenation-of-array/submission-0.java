class Solution {
    public int[] getConcatenation(int[] nums) {
        int[]ans = new int[2*(nums.length)];
        for (int i=0;i<nums.length;i++){
            ans[i] = nums[i];
        }
        for (int j=0; j<ans.length-nums.length;j++){
            ans[nums.length+j] = nums[j];
        }
        return ans;

    }
}