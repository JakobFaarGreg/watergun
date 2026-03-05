# This scripts calculates the Volumetric Flow Rate of a watergun
import pandas as pd # type: ignore
import print_utils as pu

df = pd.read_csv("raw_water_time.csv")

CUBIC_METER: str = "cubic_meter"
VOLUMETRIC_FLOW_RATE: str = "volumetric_flow_rate"
CENTILITER: str = "centiliter"
SECONDS: str = "seconds"

# Calculate VFR per row
df[CUBIC_METER] = df[CENTILITER] * 0.000001
df[VOLUMETRIC_FLOW_RATE] = df[CUBIC_METER] / df[SECONDS]

# Remove outliers and calculate aritmetic mean
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

