# This scripts calculates the Volumetric Flow Rate of a watergun
import pandas as pd # type: ignore
import print_utils as pu
import math

df = pd.read_csv("raw_water_time.csv")

CUBIC_METER: str = "cubic_meter"
VOLUMETRIC_FLOW_RATE: str = "volumetric_flow_rate"
CENTILITER: str = "centiliter"
SECONDS: str = "seconds"

diameter_in_millimeter: float = 1
diameter_in_meter: float = diameter_in_millimeter / 1000
cross_sectional_area_in_meter: float = math.pi * math.pow(diameter_in_meter / 2, 2)
# TODO: follow the thread, i figure out how to get to velocity, and from there to force.


# Calculate VFR per row
df[CUBIC_METER] = df[CENTILITER] * 0.000001
df[VOLUMETRIC_FLOW_RATE] = df[CUBIC_METER] / df[SECONDS]

# Remove outliers and calculate aritmetic mean
# TODO: ensure this is proper outlier detection. If not, improve or remove this outlier handling.
df = df.drop(df[VOLUMETRIC_FLOW_RATE].idxmax())
df = df.drop(df[VOLUMETRIC_FLOW_RATE].idxmin())

# Print mean and persist table
volumetric_flow_rate = df[VOLUMETRIC_FLOW_RATE].mean()
pu.pretty_print(str.format("Volumetric Flow Rate: {}", volumetric_flow_rate))
df.to_csv("volumetric_flow_rate.csv", index=False)

# Calculate Mass Flow Rate
MASS_DENSITY_OF_WATER: int = 1000
mass_flow_rate = volumetric_flow_rate * MASS_DENSITY_OF_WATER
pu.pretty_print(str.format("Mass Flow Rate: {}", mass_flow_rate))

