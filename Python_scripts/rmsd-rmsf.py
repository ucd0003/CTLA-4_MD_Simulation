import numpy as np
import matplotlib.pyplot as plt

def read_xvg(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if not line.startswith(('#', '@')):  # Skip comments and headers
                data.append([float(x) for x in line.split()])
    return np.array(data)

def plot_rmsd(file_path='rmsd.xvg'):
    data = read_xvg(file_path)
    time = data[:, 0]
    rmsd = data[:, 1]
    
    plt.figure(figsize=(8, 5))
    plt.plot(time, rmsd, color='green', label='RMSD for Pocket 2')
    plt.xlabel('Time (ns)')
    plt.ylabel('RMSD (nm)')
    plt.title('RMSD over Time')
    plt.legend()
    plt.xlim(0, 100)
    plt.ylim(0, 0.8)
    plt.savefig('rmsd.png', dpi=300)
    plt.show()

def plot_rmsf(file_path='rmsf.xvg'):
    data = read_xvg(file_path)
    residue = data[:, 0]
    rmsf = data[:, 1]
    
    plt.figure(figsize=(8, 5))
    plt.bar(residue, rmsf, color='blue', label='RMSF')
    plt.xlabel('Residue Number')
    plt.ylabel('RMSF (nm)')
    plt.title('RMSF per Residue')
    plt.legend()
    plt.xlim(0, 244)
    plt.ylim(0, 0.8)
    plt.savefig('rmsf_plot.png', dpi=300)
    plt.show()

def main():
    print("Plotting RMSD from rmsd.xvg...")
    plot_rmsd()
    print("Plotting RMSF from rmsf.xvg...")
    plot_rmsf()

if __name__ == "__main__":
    main()


