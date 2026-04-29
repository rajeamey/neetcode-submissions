class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = []
        # ignore_index = []
        # for index in range(0, len(strs)):
        #     if index not in ignore_index:
        #         group = [strs[index]]
        #         for index2 in range(index+1,len(strs)):
        #             if index2 not in ignore_index:
        #                 if len(strs[index]) == len(strs[index2]) and set(strs[index]) == set(strs[index2]):
        #                     if sorted(list(strs[index])) == sorted(list(strs[index2])):
        #                         group.append(strs[index2])
        #                         ignore_index.append(index2)
        #         groups.append(group)
        o1 = {}
        for s in strs:
            st= tuple(sorted(s))
            if st not in o1: o1[st] = []
            o1[st].append(s)
        return list(o1.values())