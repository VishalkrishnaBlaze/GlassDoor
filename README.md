# GlassDoor

## Installation
pip install virtualenv

virtualenv <env_name>

<env_name>/scripts/activate

pip install -r requirements.txt

NOTE: face_recognition may require to clone the source git repositoary and [install](https://face-recognition.readthedocs.io/en/latest/installation.html) from there

## Usage
when using it for the first time make sure the 'Residents' folder is empty.

python glassdoor.py --start True (Run the main loop, default: False)

python glassdoor.py --adduser NAME (add a known face, default: None)

python glassdoor.py --deleteuser NAME (remove a residents data by giving resident name as argument)

python glassdoor.py --listusers True (List out the saved residents names (default: False))

python glassdoor.py --reset True (Reset face data, default: False)
