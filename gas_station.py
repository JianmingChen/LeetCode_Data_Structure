class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Problem: Given an array gas where gas[i] is the amount of gas at the ith station, 
        and an array cost where cost[i] is the cost to travel from the ith station to the next one, 
        return the starting gas station's index if you can travel around the circuit once in the clockwise direction, 
        otherwise return -1. If there exists a solution, it is guaranteed to be unique.
        
        Args:
            gas (list[int]): Amount of gas at each station
            cost (list[int]): Cost to travel from each station
            
        Returns:
            int: Index of the starting station if a circuit is possible, -1 otherwise
        """
        total_gas = 0
        current_gas = 0
        start_station = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]

            if current_gas < 0:
                current_gas = 0
                start_station = i + 1

        return start_station if total_gas >= 0 else -1