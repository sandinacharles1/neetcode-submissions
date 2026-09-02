class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> valueIndex;
        //1. Go in order of smaller to larger index. Simeultaneously see if the complement is a preceeding value by checking pre-existing keys. Get the index (value) of the key and return it with the current index. A vector is not [] like python, its {} but returns []
        for (int i=0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (valueIndex.contains(complement)){
                int index = valueIndex[complement];

                return {index, i};
            }
            
            valueIndex[nums[i]] = i;
        }
        return {};
    }
};
