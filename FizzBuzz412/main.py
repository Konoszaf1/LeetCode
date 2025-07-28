from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lista = []
        for i in range(1, n + 1, 1):
            if i % 3 == 0 and i % 5 == 0:
                lista.append("FizzBuzz")
            elif i % 5 == 0:
                lista.append("Buzz")
            elif i % 3 == 0:
                lista.append("Fizz")
            else:
                lista.append(str(i))
        return lista

if __name__ == "__main__":
    print(Solution().fizzBuzz(1))