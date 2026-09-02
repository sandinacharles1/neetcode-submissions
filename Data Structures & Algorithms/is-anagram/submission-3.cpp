class Solution {
public:
    bool isAnagram(string s, string t) {
        //1. If they're diff lengths they cant be the same
        if (s.length() != t.length()){return false;}
        
        unordered_map<char, int> Char_To_Freq_S;
        unordered_map<char, int> Char_To_Freq_T;

        for (int i = 0; i < s.length(); i++){
            Char_To_Freq_S[s[i]] += 1;
            Char_To_Freq_T[t[i]] += 1;
        }  

        return Char_To_Freq_S == Char_To_Freq_T;
        }
};
