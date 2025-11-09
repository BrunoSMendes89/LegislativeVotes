# 🏛️ Legislative Voting System

Django web application to query information about legislator votes and bills.

## 📋 Prerequisites

- Python 3.12 or higher
- pip (Python package manager)

## 🚀 Installation and Setup

### 1. Clone or download the project

```bash
cd legislative_votes
```

### 2. Install dependencies

```bash
pip install django pandas
```

### 3. Place CSV files in project root

Make sure the following files are in the same folder as `manage.py`:

- `bills.csv`
- `legislators.csv`
- `votes.csv`
- `vote_results.csv`

### 4. Set up the database

Run migration commands to create the tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Load data from CSVs

```bash
python manage.py load_data
```

You will see confirmation messages for each file loaded.

### 6. Start the server

```bash
python manage.py runserver
```

### 7. Access the application

Open your browser and go to:

```
http://127.0.0.1:8000
```

## 📊 How to Use

### Search for a Legislator
- Enter the legislator's **name** or **ID**
- Click **Search**
- View how many bills they voted **for** and **against**

### Search for a Bill
- Enter the bill's **title** or **ID**
- Click **Search**
- View how many legislators **supported** and **opposed** it
- See who was the **primary sponsor**

## 🗂️ CSV File Structure

### bills.csv
```
id,title,sponsor_id
```

### legislators.csv
```
id,name
```

### votes.csv
```
id,bill_id
```

### vote_results.csv
```
id,legislator_id,vote_id,vote_type
```

**Note:** `vote_type` should be:
- `1` = Vote in favor
- `2` = Vote against

## 🛠️ Troubleshooting

### Error loading data
If there's an error with the `load_data` command, check:
- CSV files are in the project root folder
- File names are correct
- CSVs have the correct columns

### Migration error
If there are problems with migrations:
1. Delete the `db.sqlite3` file
2. Delete the `votes/migrations` folder
3. Create an empty `votes/migrations` folder
4. Create an empty file `votes/migrations/__init__.py`
5. Run the migration commands again

## 🔄 Reload Data

To reload data from CSVs (deletes old data and loads new):

```bash
python manage.py load_data
```

## 🛑 Stop the Server

Press `Ctrl + C` in the terminal where the server is running.

## 📝 Technologies Used

- **Django 5.x** - Web framework
- **Pandas** - CSV data processing
- **SQLite** - Database
- **HTML/CSS** - User interface

## 👨‍💻 Developer

Project developed by Bruno Mendes for the Quorum challenge.

---

**Questions?** Check the official Django documentation at https://docs.djangoproject.com/