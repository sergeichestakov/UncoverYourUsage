# Uncover Your Usage
Contributors: Kaelan Mikowicz, Thomas Munduchira, Sergei Chestakov

## Installation

Step 1:
```bash
git clone https://github.com/sergeichestakov/UncoverYourUsage.git
cd energy-analysis
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

## Deployment

```bash
pm2 start start.sh
```
