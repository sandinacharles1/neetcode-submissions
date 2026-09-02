class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        //1. Learn Unordered Set. The format is you cast int onto the unordered set function, then you initalize the variable name and the function and define the RANGE
        unordered_set<int> varName(nums.begin(), nums.end());
        //2. Use .size() to see if they match
        if (varName.size() == nums.size()){return false;}
        return true;
    }
};