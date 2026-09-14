import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import warnings

warnings.filterwarnings('ignore')

# Memuat data
df = pd.read_csv('jra_race_results_2024.csv')
data = df['win_odds'].dropna()

# Kalkulasi parameter Log-Normal
shape, loc, scale = stats.lognorm.fit(data, floc=0)
mu = np.log(scale)
sigma = shape
x = np.linspace(0.1, 300, 1000)

# Membuat Plot CDF
plt.figure(figsize=(8, 6))
x_data = np.sort(data)
y_data = np.arange(1, len(x_data)+1) / len(x_data)
plt.step(x_data, y_data, where='post', color='steelblue', lw=2.5, label='Empirical CDF (Data Aktual)')

cdf_theoretical = stats.lognorm.cdf(x, s=sigma, scale=np.exp(mu))
plt.plot(x, cdf_theoretical, 'r--', lw=2.5, label='Theoretical CDF (Log-Normal)')

plt.xlim(0, 300)
plt.title('Cumulative Distribution Function (CDF)\nDistribusi Win Odds', fontsize=14, pad=15)
plt.xlabel('Win Odds', fontsize=12)
plt.ylabel('Probabilitas Kumulatif F(x)', fontsize=12)
plt.legend(fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()

# Menyimpan gambar
plt.savefig('jra_cdf_model.png')
print(f"File jra_cdf_model.png berhasil disimpan! (mu={mu:.4f}, sigma={sigma:.4f})")