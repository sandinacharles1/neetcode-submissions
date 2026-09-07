class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;
        vector<vector<string>> output;
        
        for(int i = 0; i < strs.size(); i++){
            //1. If its sorted version in the hashmap, add it, else create it as a list
            string word = strs[i];
            sort(word.begin(), word.end());
            hashmap[word].push_back(strs[i]);
            /*if (hashmap.contains(sorted)){
                hashmap[sorted].pushback(strs[i]);
            } 
            
            else {
                hashmap[sorted] = [strs[i]];
            };*/
        };
        for(const auto& [key, value] : hashmap){
            output.push_back(value);
        }

        return output;
        
    }
    
};
