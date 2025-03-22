import matplotlib.pyplot as plt
import numpy as np

time, hbonds = np.loadtxt("hbonds_pocket2.xvg", comments=["#", "@"], unpack=True)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(time, hbonds, label="Hydrogen Bonds in Pocket 2", color="orange")
plt.xlabel("Time (ns)")
plt.ylabel("Number of Hydrogen Bonds")
plt.title("Hydrogen Bonds in Pocket 2 Over Time")
plt.legend()
plt.xlim(0,100)
plt.ylim(0,7)
plt.savefig("hbonds_pocket2.png", dpi=300)  
plt.show()

