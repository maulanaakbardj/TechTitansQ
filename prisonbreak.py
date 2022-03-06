def prison(n, m, h, v):
    # Write your code here
    largest_h_gap = 1
    largest_v_gap = 1
    
    v_cell = [1] * m
    h_cell = [1] * n
    
    if len(h) == 0 and len(v) == 0:
        return largest_h_gap * largest_v_gap
    
    for vi in v:
        v_cell[vi-1] = 0
    for hi in h:
        h_cell[hi-1] = 0
        
    temp_gap = 1
    for i in range(len(v_cell)):
        if v_cell[i] == 1:
            temp_gap = 1
        if v_cell[i] == 0:
            temp_gap = temp_gap + 1
        if temp_gap > largest_v_gap:
            largest_v_gap = temp_gap
    
    temp_gap = 1
    for i in range(len(h_cell)):
        if h_cell[i] == 1:
            temp_gap = 1
        if h_cell[i] == 0:
            temp_gap = temp_gap + 1
        if temp_gap > largest_h_gap:
            largest_h_gap = temp_gap
            
    return largest_h_gap * largest_v_gap
