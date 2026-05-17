import math

nozzleDiameterInCentimeter = [0.1, 0.2, 0.3, 0.4, 0.5, 1, 2]
volumetricFlowRateLiterPerMinute = [0.1, 1, 10, 100]


# Der er noget helt galt med mine enheder her...
for elem in nozzleDiameterInCentimeter:
    for item in volumetricFlowRateLiterPerMinute:
        mass_flow_rate = item * 1e3
        cross_sectional_area_in_meter = math.pi * math.pow(elem / 2, 2)
        velocity = item / cross_sectional_area_in_meter
        print(f"Force: {mass_flow_rate * velocity}")
