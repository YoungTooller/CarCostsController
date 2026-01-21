import sqlite3

class DatabaseManager():
    def CreateTablet(self):
        try:
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Costs (
            id INTEGER PRIMARY KEY,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            title TEXT NOT NULL,
            mileage INTEGER,
            price INTEGER
            )
            ''')
            
            self.connection.commit()
        except Exception:
            self.connection.rollback()
            return False
    
    def __init__(self, db_dir):
        try:
            self.connection = sqlite3.connect(db_dir)
            self.cursor = self.connection.cursor()
            self.CreateTablet()
        except Exception:
            return False
                
    def InsertCost(self, title, mileage, price):
        try:
            self.cursor.execute('''
            INSERT INTO Costs (title, mileage, price)
            VALUES (?, ?, ?)    
            ''', (title, mileage, price))
            
            self.connection.commit()
            return self.cursor.lastrowid
        except Exception:
            self.connection.rollback()
            return False
            
    def DeleteCost(self, id):
        try:
            self.cursor.execute('SELECT title FROM Costs WHERE id = ?', (id,))

            row = self.cursor.fetchone()
            if row is None:
                return False

            self.cursor.execute('DELETE FROM Costs WHERE id = ?', (id,))
            self.connection.commit()
            
            return True 
            
        except Exception:
            self.connection.rollback()
            return False
        
    def GetAllCosts(self):
        try:            
            self.cursor.execute('SELECT * FROM Costs')
            return self.cursor.fetchall()
        except Exception:
            self.connection.rollback()
            return []
            
    def GetFilteredCosts(self, title):
        try:            
            self.cursor.execute('SELECT * FROM Costs WHERE title = ?', (title,))
            return self.cursor.fetchall()
        except Exception:
            self.connection.rollback()
            return []
            
    def CloseSonnection(self):
        self.connection.close()
      
