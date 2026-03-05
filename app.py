# This scripts calculates the Volumetric Flow Rate of a watergun
import pandas as pd # type: ignore
import print_utils as pu

df = pd.read_csv("raw_water_time.csv")

# Calculate VFR per row
df["cubicmeter"] = df["cl"] * 0.000001
df["volumetric_flow_rate"] = df["cubicmeter"] / df["time"]

# Remove outliers and calculate aritmetic mean
df = df.drop(df["volumetric_flow_rate"].idxmax())
df = df.drop(df["volumetric_flow_rate"].idxmin())

# Print mean and persist table
pu.pretty_print(str.format("Volumetric Flow Rate: {}", df["volumetric_flow_rate"].mean()))
df.to_csv("volumetric_flow_rate.csv", index=False)