def solution(inputArray):
    obs = sorted(inputArray)
     
    # set jump distance to 1
    jump_dist = 1
    # flag to check if current jump distance
    # hits an obstacle
    obstacle_hit = True
 
    while(obstacle_hit):
         
        obstacle_hit = False
        jump_dist += 1
         
        # checking if jumping with current length
        # hits an obstacle
        for i in range(0, len(obs)):
            if obs[i] % jump_dist == 0:
                 
                # if obstacle is hit repeat process
                # after increasing jump distance
                obstacle_hit = True
                break
 
    return jump_dist
        
