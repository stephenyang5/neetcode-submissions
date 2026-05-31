class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        total_list = {}

        for string in strs:
            s_string = ''.join(sorted(string))
            if s_string not in total_list:
                total_list[s_string] = [string]
            else:
                total_list[s_string].append(string)
        
        return [total_list[key] for key in total_list]

