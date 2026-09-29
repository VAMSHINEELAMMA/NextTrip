"""
Optimization algorithms for NexTrip.

Includes:
- 0/1 Knapsack optimizer for Solo Mode
- Asymmetrical Smart-Split for Group Mode
"""

import numpy as np
from scipy.optimize import linprog
from typing import List, Tuple, Dict, Optional

class SoloOptimizer:
    """
    0/1 Knapsack optimizer for solo travel itineraries.
    Maximizes quality/utility within budget constraints.
    """
    
    @staticmethod
    def optimize(
        flights: List[Dict],
        hotels: List[Dict],
        activities: List[Dict],
        total_budget: float,
        buffer_percentage: float = 0.12  # 10-15% buffer
    ) -> Dict:
        """
        Optimize itinerary using 0/1 knapsack.
        Returns best flight + hotel + activity combo under budget.
        """
        available_budget = total_budget * (1 - buffer_percentage)
        buffer = total_budget - available_budget
        
        # TODO: Implement dynamic programming knapsack
        # For now, return greedy solution
        
        best_flight = min(flights, key=lambda x: x['cost'])
        best_hotel = min(hotels, key=lambda x: x['cost'])
        selected_activities = []
        
        remaining = available_budget - best_flight['cost'] - best_hotel['cost']
        for activity in sorted(activities, key=lambda x: x['quality_score'], reverse=True):
            if activity['cost'] <= remaining:
                selected_activities.append(activity)
                remaining -= activity['cost']
        
        total_cost = total_budget - remaining
        
        return {
            'flight': best_flight,
            'hotel': best_hotel,
            'activities': selected_activities,
            'buffer': buffer,
            'total_cost': total_cost,
            'remaining': remaining
        }

class GroupOptimizer:
    """
    Asymmetrical Smart-Split optimizer for group travel.
    Fairly distributes costs while respecting individual budgets.
    """
    
    @staticmethod
    def smart_split(
        members: List[Dict],  # {user_name, max_budget, room_pref}
        hotel: Dict,  # {base_price, ...}
        room_tiers: List[Dict],  # {tier, price_multiplier}
        shared_costs: float,  # flight + activities
        nights: int
    ) -> Tuple[Dict, Optional[List[str]]]:
        """
        Run Asymmetrical Smart-Split algorithm.
        Returns allocation dict or errors if infeasible.
        """
        # Sort members by budget ascending
        sorted_members = sorted(members, key=lambda x: x['max_budget'])
        
        allocation = {}
        errors = []
        
        # Greedy assignment: cheapest tier first for each member
        for member in sorted_members:
            # TODO: Implement tier assignment logic
            # Pro-rate shared costs by tier weight
            pass
        
        return allocation, errors
