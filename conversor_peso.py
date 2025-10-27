def kg_para_lb(kg):
    return kg * 2.20462

def lb_para_kg(lb):
    return lb / 2.20462

def kg_para_g(kg):
    return kg * 1000

def g_para_kg(g):
    return g / 1000

def g_para_lb(g):
    kg = g_para_kg(g)
    return kg_para_lb(kg)

def lb_para_g(lb):
    kg = lb_para_kg(lb)
    return kg_para_g(kg)
