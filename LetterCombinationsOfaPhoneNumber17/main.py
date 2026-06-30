HASHMAP = {"2" : "abc",
           "3" : "def",
           "4" : "ghi",
           "5" : "jkl",
           "6" : "mno",
           "7" : "pqrs",
           "8" : "tuv",
           "9" : "wxyz"}


def get_combinations(list1=[""], list2=[""], list3=[""], list4=[""]):
    combinations = []
    lists = [list1,list2,list3,list4]
    for item1 in lists[0]:
        for item2 in lists[1]:
            for item3 in lists[2]:
                for item4 in lists[3]:
                    add = f"{item1}{item2}{item3}{item4}"
                    if add not in combinations:
                        combinations += [add]
    return combinations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        return get_combinations(*[HASHMAP[x] for x in digits])


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations("2"))
    print(Solution().letterCombinations("5678"))
