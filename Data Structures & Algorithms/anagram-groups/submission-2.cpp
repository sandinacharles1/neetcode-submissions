class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        //1. Initialize Hashmap for finding words in order, and the list (vector) of matches
        unordered_map<string, vector<string>> hashmap;
        vector<vector<string>> output;

        //2. Sort the word in place, and attack the sorted to the hashmap key, and push_back the words onto the list of hashmap values
        for(int i = 0; i < strs.size(); i++){
            string word = strs[i];
            sort(word.begin(), word.end());
            hashmap[word].push_back(strs[i]);
        };
        
        //3. Get all key value pairs, and append values onto the output. FOr this I learned the format of going thtrough a hashmap is for(const auto& [key,value] : hashmap)
        for(const auto& [key, value] : hashmap){
            output.push_back(value);
        }

        return output;
        
    }
    
};
