class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * n
        
        for booking in bookings:
            first, last, seats = booking
            result[first - 1] += seats
            if last < n:
                result[last] -= seats
        
        for i in range(1, n):
            result[i] += result[i - 1]
        
        return result