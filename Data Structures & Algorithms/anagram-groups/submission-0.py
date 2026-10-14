class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if key in map:
                map[key].append(word)
            else:
                map[key] = [word]
        return list(map.values())

            