# 🌌Space-Weather-API


## 🔧 Installation & Usage
<details> 
<summary>To use this Space Weather API, follow these steps:</summary>

### 1️⃣ Clone the repository:
`git clone https://github.com/BambiCPT/Space-Weather-API.git` \
`cd Space-Weather-API`

### 2️⃣ Install dependencies:
`pip install -r requirements.txt`
Make sure to have `autopep8` and `pylint` extension if you have vscode

autopep8: https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8

pylint: https://marketplace.visualstudio.com/items?itemName=ms-python.pylint

### 4 Run db migration:
`python db/migration.py`
run this once when you make the project for the first time. Can also be runned when the db is broken. WARNING: if runned and already exist a db under the env db name. It will drop and recreate the db.

### 3️⃣ Run the script:
`python main.py` \
(Modify as needed based on how your project runs.)
</details>
