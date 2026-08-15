class Solution:
    def isAnagram(self, s: str, target: str) -> bool:
        if len(s) != len(target):
            return False

        counts = {}

        for c in s:
            counts[c] = counts.get(c, 0) + 1

        for c in target:
            if c not in counts:
                return False

            counts[c] -= 1

            if counts[c] < 0:
                return False

        return True

    def groupByAnagrams(self, l: List[str]) -> List[List[str]]:
        groups = {}

        for s in l:
            key = ''.join(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupedBySizes = {}

        for s in strs:
            groupedBySizes.setdefault(len(s), []).append(s)

        anagrams = []

        for grouped in groupedBySizes.values():
            anagrams.extend(self.groupByAnagrams(grouped))

        return anagrams