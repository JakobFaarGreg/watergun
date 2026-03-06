# This scripts calculates the Volumetric Flow Rate of a watergun
import pandas as pd # type: ignore
import print_utils as pu
import math
import matplotlib.pyplot as plt # type: ignore

df = pd.read_csv("raw_water_time.csv")

# region constants

CUBIC_METER: str = "cubic_meter"
VOLUMETRIC_FLOW_RATE: str = "volumetric_flow_rate"
MILLILITER: str = "milliliter"
SECONDS: str = "seconds"

# endregion

diameter_in_millimeter: float = 1
diameter_in_meter: float = diameter_in_millimeter / 1e3
cross_sectional_area_in_meter: float = math.pi * math.pow(diameter_in_meter / 2, 2)

# Volumetric Flow Rate (m^3/t)
### V̇ = V / t
df[CUBIC_METER] = df[MILLILITER] * 1e-6
df[VOLUMETRIC_FLOW_RATE] = df[CUBIC_METER] / df[SECONDS]

# Remove outliers and calculate aritmetic mean
# TODO: ensure this is proper outlier detection. If not, improve or remove this outlier handling.
df = df.drop(df[VOLUMETRIC_FLOW_RATE].idxmax())
df = df.drop(df[VOLUMETRIC_FLOW_RATE].idxmin())

volumetric_flow_rate = df[VOLUMETRIC_FLOW_RATE].mean()
pu.pretty_print(str.format("Volumetric Flow Rate: {}", volumetric_flow_rate))

df.to_csv("volumetric_flow_rate.csv", index=False)

# Mass Flow Rate (kg/s)
### ṁ = ρ * V̇
MASS_DENSITY_OF_WATER: int = 1e3
mass_flow_rate = volumetric_flow_rate * MASS_DENSITY_OF_WATER
pu.pretty_print(str.format("Mass Flow Rate: {}", mass_flow_rate))

# Water Velocity: (m/s)
### v = ṁ / A
velocity = mass_flow_rate / cross_sectional_area_in_meter
pu.pretty_print(str.format("Velocity: {}", velocity))

# region Plots

# -----------------------------------------------------------
# Plot 1: Volumetric Flow Rate vs Time
# -----------------------------------------------------------

# This scatter plot shows how calculated flow rate varies
# with the measured discharge time.
plt.figure()

plt.scatter(df[SECONDS], df[VOLUMETRIC_FLOW_RATE])

plt.xlabel("Seconds")
plt.ylabel("Volumetric Flow Rate (m³/s)")
plt.title("Volumetric Flow Rate vs Time")

plt.grid(True)

# Save plot to file (works in dev containers without GUI)
plt.savefig("plot_flow_rate_vs_time.png")

plt.close()


# -----------------------------------------------------------
# Plot 2: Distribution of Flow Rates
# -----------------------------------------------------------

# Histogram showing how the measurements are distributed.
# Useful for spotting skew or experimental noise.
plt.figure()

plt.hist(df[VOLUMETRIC_FLOW_RATE], bins=10)

plt.xlabel("Volumetric Flow Rate (m³/s)")
plt.ylabel("Frequency")
plt.title("Distribution of Volumetric Flow Rates")

plt.savefig("plot_flow_rate_distribution.png")

plt.close()


# -----------------------------------------------------------
# Plot 3: Flow Rate with Mean Line
# -----------------------------------------------------------

# Scatter plot with the mean flow rate overlaid.
# This highlights how individual measurements compare
# to the average experimental result.

mean_flow = df[VOLUMETRIC_FLOW_RATE].mean()

plt.figure()

plt.scatter(df[SECONDS], df[VOLUMETRIC_FLOW_RATE], label="Measurements")

# Horizontal line representing the mean flow rate
plt.axhline(mean_flow, linestyle="--", label="Mean Flow Rate")

plt.xlabel("Seconds")
plt.ylabel("Volumetric Flow Rate (m³/s)")
plt.title("Water Gun Volumetric Flow Rate")

plt.legend()
plt.grid(True)

plt.savefig("plot_flow_rate_mean.png")

plt.close()

# endregion
