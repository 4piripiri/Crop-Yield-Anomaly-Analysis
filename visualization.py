import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Custom_Crops_yield_Historical_Dataset.csv")

sns.set_theme(style="whitegrid")

# ============================================================
# FIGURE 1: CROP YIELD TRENDS
# ============================================================

fig1, axes = plt.subplots(2, 1, figsize=(20, 14))

# Graph 1: Annual Average Yield Trend by Crop
yearly_crop_yield = df.groupby(
    ['Year', 'Crop']
)['Yield_kg_per_ha'].mean().reset_index()

sns.lineplot(
    data=yearly_crop_yield,
    x='Year',
    y='Yield_kg_per_ha',
    hue='Crop',
    marker='o',
    ax=axes[0]
)

axes[0].set_title(
    '1. Annual Average Yield Trend by Crop',
    fontsize=13,
    fontweight='bold'
)
axes[0].set_ylabel('Yield (kg/ha)')
axes[0].set_xlabel('Year')
axes[0].tick_params(axis='x', labelsize=8, rotation=0)


# Graph 2: Identification of Poor-Yield Years
yearly_national = df.groupby(
    'Year'
)['Yield_kg_per_ha'].mean().reset_index()

bottom_threshold = yearly_national[
    'Yield_kg_per_ha'
].quantile(0.10)

yearly_national['Status'] = yearly_national[
    'Yield_kg_per_ha'
].apply(
    lambda x: 'Poor Yield Year'
    if x <= bottom_threshold
    else 'Normal / High Yield Year'
)

sns.barplot(
    data=yearly_national,
    x='Year',
    y='Yield_kg_per_ha',
    hue='Status',
    palette={
        'Poor Yield Year': 'crimson',
        'Normal / High Yield Year': 'steelblue'
    },
    ax=axes[1]
)

axes[1].set_title(
    '2. Identification of Poor-Yield Years (Bottom 10%)',
    fontsize=13,
    fontweight='bold'
)
axes[1].set_ylabel('Mean Yield (kg/ha)')
axes[1].set_xlabel('Year')
axes[1].tick_params(axis='x', labelsize=8, rotation=0)
axes[1].legend(title='Yield Status', loc='upper right')

fig1.tight_layout(pad=4.0, h_pad=4.0)
plt.show()


# ============================================================
# FIGURE 2: YIELD VS ENVIRONMENTAL FACTORS
# ============================================================

fig2, axes = plt.subplots(2, 1, figsize=(20, 12))

national_env = df.groupby('Year')[
    ['Yield_kg_per_ha', 'Rainfall_mm', 'Temperature_C']
].mean().reset_index()


# Graph 3: Yield vs Rainfall
ax1 = axes[0]
ax1_twin = ax1.twinx()

line1 = ax1.plot(
    national_env['Year'],
    national_env['Yield_kg_per_ha'],
    color='green',
    marker='o',
    label='Yield'
)

line2 = ax1_twin.plot(
    national_env['Year'],
    national_env['Rainfall_mm'],
    color='blue',
    linestyle='--',
    marker='s',
    label='Rainfall'
)

ax1.set_title(
    '3. Yearly Crop Yield vs Rainfall',
    fontsize=13,
    fontweight='bold'
)
ax1.set_xlabel('Year')
ax1.set_ylabel('Yield (kg/ha)', color='green')
ax1_twin.set_ylabel('Rainfall (mm)', color='blue')
ax1.tick_params(axis='x', labelsize=8, rotation=0)

ax1.legend(
    line1 + line2,
    ['Yield', 'Rainfall'],
    loc='upper left'
)


# Graph 4: Yield vs Temperature
ax2 = axes[1]
ax2_twin = ax2.twinx()

line3 = ax2.plot(
    national_env['Year'],
    national_env['Yield_kg_per_ha'],
    color='green',
    marker='o',
    label='Yield'
)

line4 = ax2_twin.plot(
    national_env['Year'],
    national_env['Temperature_C'],
    color='red',
    linestyle='--',
    marker='^',
    label='Temperature'
)

ax2.set_title(
    '4. Yearly Crop Yield vs Temperature',
    fontsize=13,
    fontweight='bold'
)
ax2.set_xlabel('Year')
ax2.set_ylabel('Yield (kg/ha)', color='green')
ax2_twin.set_ylabel('Temperature (°C)', color='red')
ax2.tick_params(axis='x', labelsize=8, rotation=0)

ax2.legend(
    line3 + line4,
    ['Yield', 'Temperature'],
    loc='upper left'
)

fig2.tight_layout(pad=4.0, h_pad=4.0)
plt.show()


# ============================================================
# FIGURE 3: ENVIRONMENTAL ANALYSIS
# ============================================================

fig3, axes = plt.subplots(1, 2, figsize=(20, 8))


# Graph 5: Rainfall Comparison Across Crop Yield Categories
df['Yield_Status'] = df.groupby(
    'Crop'
)['Yield_kg_per_ha'].transform(
    lambda x: pd.qcut(
        x,
        q=[0, 0.15, 1.0],
        labels=[
            'Unusually Poor Yield',
            'Normal / High Yield'
        ],
        duplicates='drop'
    )
)

sns.boxplot(
    data=df,
    x='Crop',
    y='Rainfall_mm',
    hue='Yield_Status',
    hue_order=[
        'Unusually Poor Yield',
        'Normal / High Yield'
    ],
    palette={
        'Unusually Poor Yield': '#e74c3c',
        'Normal / High Yield': '#2ecc71'
    },
    ax=axes[0]
)

axes[0].set_title(
    '5. Rainfall by Crop Yield Category',
    fontsize=13,
    fontweight='bold'
)
axes[0].set_xlabel('Crop')
axes[0].set_ylabel('Rainfall (mm)')
axes[0].tick_params(axis='x', labelsize=9, rotation=0)
axes[0].legend(title='Yield Category', loc='best')


# Graph 6: Correlation Matrix
env_cols = [
    'Yield_kg_per_ha',
    'Rainfall_mm',
    'Temperature_C',
    'Humidity_%',
    'pH',
    'Wind_Speed_m_s'
]

sns.heatmap(
    df[env_cols].corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f',
    square=True,
    ax=axes[1]
)

axes[1].set_title(
    '6. Correlation Matrix of Yield and Environmental Variables',
    fontsize=13,
    fontweight='bold'
)
axes[1].tick_params(axis='x', labelsize=9, rotation=45)
axes[1].tick_params(axis='y', labelsize=9, rotation=0)

fig3.tight_layout(pad=4.0, w_pad=4.0)
plt.show()