import math

def old_adjusted_wald(p, n, z=1.96):
    p_adj = (n * p + (z**2)/2)/(n+z**2)
    n_adj = n + z**2
    span = z * math.sqrt(p_adj*(1-p_adj)/n_adj)
    return max(0, p_adj - span), min(p_adj + span, 1.0)

def adjusted_wald(p, n, z=1.96):
    p_adj = (n * p + (z**2)/2)/(n+z**2)
    n_adj = n + z**2
    span = z * math.sqrt(p_adj*(1-p_adj)/n_adj)
    print(str(max(0, p_adj - span)) + ' ' + str(min(p_adj + span, 1.0)) )
    return max(0, p_adj - span), min(p_adj + span, 1.0)



a, b = old_adjusted_wald(0.777038269550748,1803)
print('95%CI:' + str(round(a,3)) + ' , ' + str(round(b,3)))
a, b = old_adjusted_wald(0.81926683716965,1173)
print('95%CI:' + str(round(a,3)) + ' , ' + str(round(b,3)))
a, b = old_adjusted_wald(0.698412698412698,630)
print('95%CI:' + str(round(a,3)) + ' , ' + str(round(b,3)))








a, b = old_adjusted_wald(0.811111111111111,180)
print('95%CI:' + str(round(a,3)) + ' , ' + str(round(b,3)))
a, b = old_adjusted_wald(0.897435897435897,117)
print('95%CI:' + str(round(a,3)) + ' , ' + str(round(b,3)))
a, b = old_adjusted_wald(0.65079365079365,63)

print('95%CI:' + str(round(a,3)) + ' , ' + str(round(b,3)))