class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available = [i for i in range(n)]
        occupied = [] # (end, room_number)
        freq = [0] * n

        for start, end in meetings:
            # Calls Ending
            while occupied and start >= occupied[0][0]:
                end_time, room = heapq.heappop(occupied) # Job completing first
                heapq.heappush(available, room) # Make room available

            # No Room Available
            if not available:
                end_time, room = heapq.heappop(occupied) # Job completing first
                end = end_time + (end - start)
                heapq.heappush(available, room) # Make room available

            # Make booking
            room = heapq.heappop(available)
            heapq.heappush(occupied, (end, room))
            freq[room] += 1
        
        return freq.index(max(freq))