class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair each car's position with its speed and sort by position descending
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
    
        for pos, spd in cars:
            # Time to reach destination = (target - position) / speed
            time_to_target = (target - pos) / spd
            stack.append(time_to_target)  # Fixed: changed 'tack' to 'stack'
        
            # If the car behind catches up to (or arrives faster than) the car ahead,
            # it merges into the fleet ahead (pop its separate time).
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
# Example Usage

        