from src.db import DatabaseManager

import os

if __name__ == "__main__":
    DB_PATH = os.path.join('data', 'database.db')
        
    os.makedirs("./data", exist_ok=True)
    
    db = DatabaseManager(DB_PATH)
    
    db.CloseSonnection()
