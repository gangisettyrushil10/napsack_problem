# napsack_problem
Mixed integer linear programming problem solved using gurobi. 

# Hiking Supplies Optimization

This project uses Gurobi's Mixed Integer Linear Programming (MILP) to optimize the selection of supplies for a hiking trip based on weight constraints and survival points.

## Problem Statement

You can carry a maximum weight of either 10 kg or 30 kg. The goal is to maximize survival points based on the items you can carry.

## Items Available

- Tent: 10 survival points, 8 kg (max 1)
- Chocolate Bar: 1.5 survival points, 3 kg (max 5)
- Flashlight: 4 survival points, 2 kg (max 2)
- Fishing Kit: 5 survival points, 4 kg (max 1)
- Water: 4 survival points, 3 kg (max 2)
- Flare Gun: 5 survival points, 5 kg (max 1)
- Video Game: 1 survival point, 2 kg (unlimited)

## How to Run

1. Ensure you have Gurobi installed and set up.
2. Run the script using Python:
   ```bash
   python HW_06_gangisetty.py
   ```

## Results

The script will output the maximized survival points and the items selected for each weight limit.
