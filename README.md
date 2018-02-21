# Uncover Your Usage
Contributors: Kaelan Mikowicz, Thomas Munduchira, Sergei Chestakov

The Residential Energy Consumption Survey is a national survey that collects energy-related data for housing units. Data was collected from 12,083 households selected at random, and contains hundreds of factors as well as associated measures of energy usage. More information about the dataset can be obtained [here](https://www.eia.gov/consumption/residential/data/2009/index.php?view=microdata).

We utilized Principle Component Analysis (PCA) to find uncorrelated components within the dataset and to reduce the dimensionality along combinations of the dataset. We also conducted linear regression on normalized data to find the features that correlated the most with energy usage.

We then trained a deep neural network to predict expected annual energy usage in kilowatt hours based on fourteen independant and correlated variables from our analysis. This DNN is utilized for the [web app](https://energy.thomasmunduchira.com/) where any user can get an output of his or her predicted energy usage after filling out a form.

## Installation

Step 1:
```bash
git clone https://github.com/sergeichestakov/UncoverYourUsage.git
cd UncoverYourUsage
```

Step 2:
```bash
pip3 install virtualenv
virtualenv venv
venv\Scripts\activate (Windows)
. venv/bin/activate (Others)

# Use "deactivate" to exit virtual environment
```

Step 3:
```bash
pip3 install -r requirements.txt
```

Step 4:
```bash
export FLASK_APP=app.py
flask run
```

## Formatting
```bash
autopep8 --in-place --aggressive --aggressive *.py
```

## Deployment

```bash
pm2 start start.sh
```
