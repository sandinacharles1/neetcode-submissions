class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        permutations, current_permutation = [],[] #List for easy appending.
        #The parameters are opening and closing because those are information we need to maintain so we can accurately generate parenthesis that are VALID.
        def generate(opening, closing): 
            if len(current_permutation) == 2*n: 
                permutations.append("".join(current_permutation))
                return

            if opening < n: 
                current_permutation.append("(")
                generate(opening + 1, closing)
                current_permutation.pop()

            if closing < opening:
                current_permutation.append(")")
                generate(opening, closing + 1)
                current_permutation.pop()

            return
        generate(0,0)
        return permutations

        '''Criteria:
       N-pairs. So n-opening, n closing. so 2*n length

       We can only add a closing parenthesis when theres MORE openioing parenthesiss closing < opening
       We can always add an opening aprentehsis if the count is under n. 

       So we maintain count of closing and opening parentehses.Otherwise, we perform backtracking

       So we generate both options, then rescind. So we do opening, then the first instance will max the openings, then it'll all return back to the last oepning (all the opening conditions will fail while oepneing = n) then we do the next tconditional for closing, then we keep going in that time, then we reescind and keep goign back'''
