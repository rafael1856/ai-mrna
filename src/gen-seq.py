# You can adjust the parameters `k`, `n`, and `p` to see how they affect the 
# generation of sequences and the resulting CAI-MFA chart. For example, you 
# could increase `k` to generate more GC-rich sequences or decrease `p` to 
# generate more A/T-rich sequences.

# Note that this is a simplified model and actual mRNA sequences may exhibit 
# more complex patterns and biases.

# Here is a Jupiter Notebook for generating mRNA genetic code, determining 
# CAI and MFA, and adjusting parameters:

import numpy as np
from scipy.stats import entropy
import matplotlib.pyplot as plt


# **Cell 1-3:** Define constants for the Markov chain model: `k` is the 
# average GC content (0-1), `n` is the sequence length, and `p` is the 
# probability of a base being A or C (0-1).

# Define some constants
k = 0.5  # average GC content (0-1)
n = 1000  # sequence length
p = 0.3  # probability of a base being A or C (0-1)


# **Cell 4-5:** Define the `generate_sequence` function, which generates an 
# mRNA sequence using the Markov chain model. The function takes `k` and `n` 
# as inputs and returns a sequence string.
def generate_sequence(k, n):
    seq = ""
    for i in range(n):
        if np.random.rand() < k:
            seq += "G" if np.random.rand() < p else "C"
        else:
            seq += "A" if np.random.rand() < p else "T"
    return seq


# **Cell 6-7:** Define the `calculate_cai_mfa` function, which calculates 
# CAI (Composition Bias Index) and MFA (Mean Frequency Across) for a given 
# sequence. The function counts the frequency of each base in the sequence 
# and calculates CAI as the average composition bias, and MFA as the mean 
# frequency across.
# Calculate CAI (Composition Bias Index) and MFA (Mean Frequency Across)
def calculate_cai_mfa(seq):
    cai = 0
    mfa = 0
    
    # Count the frequency of each base
    base_counts = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in seq:
        base_counts[base] += 1
    
    # Calculate CAI (Composition Bias Index)
    cai = np.sum([counts / n for counts in base_counts.values()]) * 100
    
    # Calculate MFA (Mean Frequency Across)
    mfa = np.mean(list(base_counts.values()))
    
    return cai, mfa

# **Cell 8-12:** Generate sequences with different parameters (`k`) and 
# calculate CAI and MFA for each sequence. Store the sequences, CAINs, and 
# MFAs in separate lists.
# Generate sequences with different parameters and calculate CAI and MFA
sequences = []
cains = []
mfas = []

for i in range(10):
    k = 0.2 + (i * 0.05)  # adjust GC content
    seq = generate_sequence(k, n)
    cai, mfa = calculate_cai_mfa(seq)
    
    sequences.append(seq)
    cains.append(cai)
    mfas.append(mfa)


# **Cell 13:** Plot a scatter plot of CAI vs MFA using the generated data. 
# The x-axis represents CAI, and the y-axis represents MFA.
# Plot CAI vs MFA
plt.scatter(cains, mfas)
plt.xlabel("CAI")
plt.ylabel("MFA")
plt.title("CAI-MFA Chart for mRNA Sequences")
plt.show()











