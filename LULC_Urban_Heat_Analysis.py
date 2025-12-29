"""
ADVANCED RESEARCH PROJECT: LULC & UHI MITIGATION STRATEGY
Study Area: Delhi NCR - Ganga Basin
Simulation: Business as Usual (BAU) vs Sustainable Mitigation (2045)
Author: Abhinav Chaudhary
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# ======================================================
# 1. DATA SIMULATION (BAU vs SUSTAINABLE)
# ======================================================
def generate_scenario_data(u_dens, f_dens):
    p_water, p_forest, p_urban = 0.05, f_dens, u_dens
    p_agri = max(0, 1.0 - p_urban - p_forest - p_water)
    probs = np.array([p_water, p_forest, p_agri, p_urban])
    probs /= probs.sum()
    return np.random.choice([0, 1, 2, 3], size=(50, 50), p=probs)

# Scenarios for 2045
data_2045_BAU = generate_scenario_data(0.80, 0.05)   # No planning
data_2045_SUS = generate_scenario_data(0.60, 0.25)   # Sustainable (More Greenery)

# ======================================================
# 2. MITIGATION THERMAL ENGINE
# ======================================================
def thermal_model(lulc, is_sustainable=False):
    base = 31.0
    lst = np.zeros(lulc.shape)
    
    # Heat assignments
    urban_heat = 8.0 if is_sustainable else 12.0 
    
    lst[lulc == 3] = base + urban_heat
    lst[lulc == 2] = base + 5
    lst[lulc == 1] = base + 1
    lst[lulc == 0] = base
    
    return lst + np.random.normal(0, 0.5, lulc.shape)

temp_BAU = thermal_model(data_2045_BAU, is_sustainable=False)
temp_SUS = thermal_model(data_2045_SUS, is_sustainable=True)

# ======================================================
# 3. RESEARCH COMPARISON DASHBOARD
# ======================================================
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
ncr_cmap = ListedColormap(['#1e3d59', '#228b22', '#f4d03f', '#d73027'])

# Map: Business as Usual
axes[0,0].imshow(data_2045_BAU, cmap=ncr_cmap)
axes[0,0].set_title("2045: Business as Usual (High Crisis)", fontweight='bold')
axes[0,0].axis('off')

# Map: Sustainable Mitigation
axes[0,1].imshow(data_2045_SUS, cmap=ncr_cmap)
axes[0,1].set_title("2045: Sustainable Planning (Mitigated)", fontweight='bold', color='green')
axes[0,1].axis('off')

# Thermal: BAU Heat
im3 = axes[1,0].imshow(temp_BAU, cmap='magma')
axes[1,0].set_title("LST: Business as Usual (°C)")
fig.colorbar(im3, ax=axes[1,0])

# Thermal: Sustainable Cooling
im4 = axes[1,1].imshow(temp_SUS, cmap='magma')
axes[1,1].set_title("LST: Sustainable Scenario (°C)")
fig.colorbar(im4, ax=axes[1,1])

plt.suptitle("MITIGATION ANALYSIS: COOLING POTENTIAL OF URBAN GREENING (2045)", fontsize=18)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# --- SAVE IMAGE BEFORE SHOWING ---
# Is line se aapki image phone mein save ho jayegi
plt.savefig("Sustainability_Mitigation_Report.png", dpi=300) 
print("\n[SUCCESS] Image saved as 'Sustainability_Mitigation_Report.png'")

plt.show()

# ======================================================
# 4. POLICY RECOMMENDATIONS & IMPACT
# ======================================================
avg_bau = np.mean(temp_BAU)
avg_sus = np.mean(temp_SUS)
cooling_benefit = avg_bau - avg_sus

print(f"\n{'#'*50}")
print("       RESEARCH-BASED POLICY RECOMMENDATIONS")
print(f"{'#'*50}")
print(f"1. Cooling Potential   : {cooling_benefit:.2f}°C average reduction")
print(f"2. Peak Mitigation     : Up to 4.00°C cooler in Urban Hotspots")
print(f"3. Recommendation      : Increase Forest/Green cover by 20% to stabilize UHI.")
print(f"4. Status              : Simulation Saved as 'Sustainability_Mitigation_Report.png'")
print(f"{'#'*50}")
