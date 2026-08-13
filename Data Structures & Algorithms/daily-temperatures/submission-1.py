class Solution:

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Stores indices of unresolved days

        for i, temp in enumerate(temperatures):
            # Resolve warmer days for indices at the top of the stack
            while stack and temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index

            # Push current day's index onto the stack
            stack.append(i)

        return result