# Cert Issuer
A python package to issue certificates via email. Uses a base image as template and appends details from excel sheet and sends certificate as pdf to mail id provided in details.

----
## Instructions to run
1. Clone the repo using any of the following commands
   - `git clone https://github.com/abhinand-c/Cert-Issuer.git`
   - `git clone git@github.com:abhinand-c/Cert-Issuer.git`
   - `gh repo clone abhinand-c/Cert-Issuer`
2. Paste the dummy .env file below to your cloned repo
3. Set values in .env file, with correct mail server credentials.
3. Setup & activate virtual python environment  (Refer: [Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) or [Python venv](https://docs.python.org/3/tutorial/venv.html))
4. Install requirements `pip install -r requirements.txt`
5. Modify parameters and values in `main.py`
6. Generate and send certificates via mail `python main.py`

----
#### Dummy .env file

Copy the code below and save it in your cloned repo as `.env` file, also add the values required.
```

HOST_MAIL = 
HOST = 
HOST_PASSWORD = 
PORT =

```
