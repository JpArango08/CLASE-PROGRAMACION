def actividades_maximas(actividades):
    actividades.sort(key=lambda x: x[2]) #nlog(n)
    result = []
    final_actual = 0
    for act in actividades: #O(n)
        if act[1] >= final_actual:
            result.append(act)
            final_actual = act[2]
    return result
