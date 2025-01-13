#diary-app-m4l1-solution

## 📚 Project Setup and Database Configuration

To set up your project correctly and create the database, follow these steps:

```bash
# The command you need to type in the terminal to switch to the Python environment:
python

# Import required modules from main file
from main import app, db

# Activate the application context
app.app_context().push()

# Create the database file
db.create_all()