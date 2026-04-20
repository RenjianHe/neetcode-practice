class Solution {
    public int removeElement(int[] nums, int val) {
        List<Integer> tmp = new ArrayList<>();
        for (int i = 0; i<nums.length;i++){
            if (nums[i] != val){
                tmp.add(nums[i]);
            }
        }
        for (int j = 0; j<tmp.size();j++){
            nums[j] = tmp.get(j);
        }
        return tmp.size();
    }
}