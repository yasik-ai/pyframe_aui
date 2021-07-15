#  give permission to this file & folder before executing,
# chmod +x configurations/venv_dependencies.sh
# or Copy paste this command in your root folder and execute

virtualenv --no-site-packages --distribute venv_pyframe && source venv_pyframe/bin/activate  && sleep 30 && pip install -r configurations/requirements.txt

