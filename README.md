# Watergun

This is a hobby project for creating an automated watergun.

## How to use

1. Install docker
2. Open the devcontainer in vscode
3. Run `pip install -r requirements.txt`
4. Run `python app.py`

## Results

|Measure|Value|Unit|
|--|--|--|
|Volumetric Flow Rate|2.564192571552358e-06|m^3/t|
|Mass Flow Rate|0.002564192571552358|kg/s|
|Velocity|4.030656027674828|m/s|
|Force|0.01033537824464653|Newton|

## Calculations for the force exerted by a watergun

![volume/time datapoints for reference water jet](/png/plot_flow_rate_vs_time.png)
![datapoints plotted as a histogram to show distribution](/png/plot_flow_rate_distribution.png)
![volume/time datapoints plotted with mean](/png/plot_flow_rate_mean.png)
