import gurobipy as gp

# max weight cases
max_weight = [10,15,30]

for max_weight in max_weight:
    m = gp.Model()
    m._X = m.addVars([1, 2, 3, 4, 5, 6, 7], name="x")

    # variables
    tent = m._X[1]
    chocolate = m._X[2]
    flashlight = m._X[3]
    fishing_kit = m._X[4]
    water = m._X[5]
    flare_gun = m._X[6]
    video_game = m._X[7]

    # objective function
    m.setObjective(10 * tent + 1.5 * chocolate + 4 * flashlight + 
                   5 * fishing_kit + 4 * water + 5 * flare_gun + 
                   1 * video_game, gp.GRB.MAXIMIZE)

    # quantity constraints
    m.addConstr(tent <= 1)  
    m.addConstr(chocolate <= 5)  
    m.addConstr(flashlight <= 2)  
    m.addConstr(fishing_kit <= 1)  
    m.addConstr(water <= 2)  
    m.addConstr(flare_gun <= 1)  
    m.addConstr(video_game <= 1) 

    # weight constraint
    m.addConstr(8 * tent + 3 * chocolate + 2 * flashlight + 4 * fishing_kit + 3 * water + 5 * flare_gun +  2 * video_game <= max_weight)
    m.optimize()

    # results
    total_weight = 8 * tent.x + 3 * chocolate.x + 2 * flashlight.x +  4 * fishing_kit.x + 3 * water.x + 5 * flare_gun.x + 2 * video_game.x
    total_survival_points = m.objVal
    print(f"maximized survival points for {max_weight}kg: {total_survival_points} used {total_weight}kg")
    print(f"tent: {tent.x}")
    print(f"chocolate: {chocolate.x}")
    print(f"flashlight: {flashlight.x}")
    print(f"fishing kit: {fishing_kit.x}")
    print(f"water: {water.x}")
    print(f"flare gun: {flare_gun.x}")
    print(f"video game: {video_game.x}")
    


