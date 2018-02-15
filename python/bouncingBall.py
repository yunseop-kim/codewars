def bouncingBall(h, bounce, window):
    # your code
    if not h > 0: return -1
    if not 0 < bounce < 1: return -1
    if not window < h: return -1
    
    count = 0
    
    while (h > window):
        h *= bounce
        count += 1
        if h > window: count += 1
    return count


# 사실 문제 이해를 잘 못했음. '떨어지거나 튀는 것을' 세야 하는데 떨어진 것만 셈.

def bouncingBall(h, bounce, window):
    if not 0 < bounce < 1: return -1
    count = 0
    while h > window:
        count += 1
        h *= bounce
        if h > window: count += 1
    return count or  -1