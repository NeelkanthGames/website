# Website


## Getting Started

### Prerequisites
1) Create a master folder NKG.
1) Clone or download this repository in this folder. Open your command prompt and navigate to the NKG folder 
```
cd \path\to\NKG
git clone https://github.com/NeelkanthGames/website
```
(if you don't have git installed, then just download in the NKG folder)

### Installing

1) Install Python3.7 (refer https://realpython.com/installing-python/)
2) Install pip (refer https://pip.pypa.io/en/stable/installing/)
3) Install virtualenv
```
pip install virtualenv
```

Once the initial setup is completed, create a virtual environment and once done, activate it.
```
virtualenv venv
venv\Script\activate
```

At this point, you will have two folders
|--NKG
    |--website
    |--venv


4) Install dependencies.
```
cd website
pip install -r requirements.txt
```

## Deploying in localhost

Run the server and fire up http://127.0.0.1:8000/ in web-browser.
```
python manage.py runserver
```
