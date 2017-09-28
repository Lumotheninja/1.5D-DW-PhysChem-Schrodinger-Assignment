import scipy.constants as c

def energy_n(n):
    energy =-(c.m_e*(c.e*c.e/(4*c.pi*c.epsilon_0))**2)/((2*(c.hbar**2))*(n**2)*c.e)
    return round(energy,5)
    
print energy_n(4)