# build_files.sh
python3 -m venv venv
pip install -r requirements.txt
python3.9 manage.py collectstatic