class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []  # Holds indices of days
    
        for i, temp in enumerate(temperatures):
        # Resolve all previous colder days
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            
        # Push current day's index onto stack
            stack.append(i)
        return result
        