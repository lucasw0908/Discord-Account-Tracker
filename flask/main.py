import os
from dotenv import load_dotenv
from flask_migrate import Migrate
from app import create_app, db

dotenv_path = os.path.join(os.path.dirname(__file__), ".flaskenv")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)

app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
