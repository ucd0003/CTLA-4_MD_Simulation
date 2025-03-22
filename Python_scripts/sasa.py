import matplotlib.pyplot as plt
import numpy as np

# Load data from the .xvg file
time, total_sasa, group_sasa = np.loadtxt("sasa_pocket1.xvg", comments=["#", "@"], unpack=True)

# Plot 1: Total SASA over time
plt.figure(figsize=(8, 5))
plt.plot(time, total_sasa, color="blue", label="Total SASA")
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("SASA (nm²)", fontsize=12)
plt.title("Total Solvent-Accessible Surface Area Over Time", fontsize=14)
plt.legend()
plt.xlim(0, 100)
plt.savefig("total_sasa_plot.png", dpi=300)  
plt.show()

# Plot 2: Pocket 2 SASA over time
plt.figure(figsize=(8, 5))
plt.plot(time, group_sasa, color="red", label="Pocket 2 SASA")
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("SASA (nm²)", fontsize=12)
plt.title("Pocket 2 Solvent-Accessible Surface Area Over Time", fontsize=14)
plt.legend()
plt.xlim(0, 100)
plt.savefig("pocket2_sasa_plot.png", dpi=300)  
plt.show()
