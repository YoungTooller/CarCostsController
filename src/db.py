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
            print(f"ERROR: {Exception}")
            self.connection.rollback()
            return False
    
    def __init__(self, db_dir):
        try:
            self.connection = sqlite3.connect(db_dir)
            self.cursor = self.connection.cursor()
            self.CreateTablet()
        except Exception:
            print(f"ERROR: {Exception}")
            return False
                
    def InsertCost(self, title, mileage, price):
        try:
            self.cursor.execute('''
            INSERT INTO Costs (title, mileage, price)
            VALUES (?, ?, ?)    
            ''', (title, mileage, price))
            
            self.connection.commit()
            print(f'SUCCESSFULLY: Расход "{title}" добавлен!')
            return self.cursor.lastrowid
        except Exception:
            print(f"ERROR: {Exception}")
            self.connection.rollback()
            return False
            
    def DeleteCost(self, id):
        try:
            self.cursor.execute('SELECT title FROM Costs WHERE id = ?', (id,))

            row = self.cursor.fetchone()
            if row is None:
                print(f"ERROR: Расход с ID {id} не найден")
                return False

            this_title = row[0]

            self.cursor.execute('DELETE FROM Costs WHERE id = ?', (id,))
            self.connection.commit()
            
            print(f'SUCCESSFULLY: Расход "{this_title}" удалён!')
            return True 
            
        except Exception:
            print(f"ERROR: {Exception}")
            self.connection.rollback()
            return False
        
    def GetAllCosts(self):
        try:            
            self.cursor.execute('SELECT * FROM Costs')
            return self.cursor.fetchall()
        except Exception:
            print(f"ERROR: {Exception}")
            self.connection.rollback()
            return []
            
    def GetFilteredCosts(self, title):
        try:            
            self.cursor.execute('SELECT * FROM Costs WHERE title = ?', (title,))
            return self.cursor.fetchall()
        except Exception:
            print(f"ERROR: {Exception}")
            self.connection.rollback()
            return []
            
    def CloseSonnection(self):
        self.connection.close()
      
