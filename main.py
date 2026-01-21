import sys
import os
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QAbstractItemView
from PySide6.QtCore import Qt
from src.db import DatabaseManager
from ui.ui_main_window import Ui_MainWindow

class CarCostController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)        
        DB_PATH = os.path.join('data', 'database.db')
        os.makedirs("./data", exist_ok=True)
        self.db = DatabaseManager(DB_PATH)
        self.setup_table()
        self.connect_signals()
        self.load_costs()
        self.setup_validators()
    
    def setup_table(self):
        headers = ["ID", "Дата", "Название", "Пробег", "Стоимость"]
        self.ui.tableWidget.setColumnCount(len(headers))
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 200)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 120)
        self.ui.tableWidget.setSelectionBehavior(self.ui.tableWidget.SelectionBehavior.SelectRows)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.ui.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #2b2b2b;
                color: #ffffff;
                gridline-color: #555;
                font-size: 13px;
            }
            QTableWidget::item {
                background-color: #2b2b2b;
                color: #ffffff;
                padding: 5px;
                border-bottom: 1px solid #444;
            }
            QTableWidget::item:selected {
                background-color: #3a6ea5;
                color: white;
            }
            QHeaderView::section {
                background-color: #3b3b3b;
                color: #ffffff;
                font-weight: bold;
                font-size: 13px;
                padding: 8px;
                border: 1px solid #555;
                border-left: none;
                border-top: none;
            }
            QHeaderView::section:first {
                border-left: 1px solid #555;
            }
            QHeaderView::section:last {
                border-right: 1px solid #555;
            }
            QHeaderView::section:checked {
                background-color: #4a4a4a;
            }
            QTableCornerButton::section {
                background-color: #3b3b3b;
                border: 1px solid #555;
            }
        """)        
    
    def setup_validators(self):
        self.ui.Name.setPlaceholderText("Введите название")
        self.ui.Mileage.setPlaceholderText("0")
        self.ui.Price.setPlaceholderText("0")
        self.ui.deleted_index.setPlaceholderText("ID записи")
        self.ui.filter.setPlaceholderText("Название для поиска")
    
    def connect_signals(self):
        self.ui.Add_Button.clicked.connect(self.add_cost)
        self.ui.Delete_Button.clicked.connect(self.delete_cost)
        self.ui.filtered_btn.clicked.connect(self.apply_filter)
        self.ui.toolButton.clicked.connect(self.refresh_table)
        self.ui.filter.textChanged.connect(self.auto_search)
        self.ui.Name.returnPressed.connect(self.add_cost)
        self.ui.Price.returnPressed.connect(self.add_cost)
        self.ui.deleted_index.returnPressed.connect(self.delete_cost)
        self.ui.filter.returnPressed.connect(self.apply_filter)
    
    def format_date(self, date_str):
        try:
            if '.' in date_str:
                date_str = date_str.split('.')[0]
            date_obj = datetime.fromisoformat(date_str)
            return date_obj.strftime("%d.%m.%Y %H:%M")
        except:
            return date_str
    
    def load_costs(self, filter_text=None):
        self.ui.tableWidget.setRowCount(0)
        if filter_text and filter_text.strip():
            costs = self.db.GetFilteredCosts(filter_text.strip())
        else:
            costs = self.db.GetAllCosts()
        costs.sort(key=lambda x: x[1], reverse=True)
        for row, cost in enumerate(costs):
            self.ui.tableWidget.insertRow(row)
            id_item = QTableWidgetItem(str(cost[0]))
            id_item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row, 0, id_item)
            date_item = QTableWidgetItem(self.format_date(cost[1]))
            date_item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row, 1, date_item)
            title_item = QTableWidgetItem(cost[2])
            self.ui.tableWidget.setItem(row, 2, title_item)
            mileage_item = QTableWidgetItem(str(cost[3]))
            mileage_item.setTextAlignment(Qt.AlignCenter)
            self.ui.tableWidget.setItem(row, 3, mileage_item)
            price_item = QTableWidgetItem(f"{cost[4]:,}".replace(",", " "))
            price_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
            self.ui.tableWidget.setItem(row, 4, price_item)
        count = len(costs)
        self.statusBar().showMessage(f"Записей: {count}", 3000)
    
    def add_cost(self):
        title = self.ui.Name.text().strip()
        mileage_text = self.ui.Mileage.text().strip()
        price_text = self.ui.Price.text().strip()
        if not title:
            QMessageBox.warning(self, "!", "Введите название расхода!")
            self.ui.Name.setFocus()
            return
        if not price_text:
            QMessageBox.warning(self, "!", "Введите стоимость!")
            self.ui.Price.setFocus()
            return
        try:
            mileage = int(mileage_text) if mileage_text else 0
            price = int(price_text)
            if price <= 0:
                QMessageBox.warning(self, "!", "Стоимость должна быть больше 0!")
                self.ui.Price.setFocus()
                return
            if mileage < 0:
                QMessageBox.warning(self, "!", "Пробег не может быть отрицательным!")
                self.ui.Mileage.setFocus()
                return
        except ValueError:
            QMessageBox.warning(self, "!", "Пробег и стоимость должны быть числами!")
            return
        result = self.db.InsertCost(title, mileage, price)
        if result:
            self.ui.Name.clear()
            self.ui.Mileage.clear()
            self.ui.Price.clear()
            self.refresh_table()
            self.ui.Name.setFocus()
            QMessageBox.information(self, "!", f"Расход '{title}' успешно добавлен!")
        else:
            QMessageBox.critical(self, "!", "Не удалось добавить расход!")
    
    def delete_cost(self):
        id_text = self.ui.deleted_index.text().strip()
        if not id_text:
            QMessageBox.warning(self, "!", "Введите ID записи для удаления!")
            self.ui.deleted_index.setFocus()
            return
        try:
            cost_id = int(id_text)
            if cost_id <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "!", "ID должен быть положительным числом!")
            self.ui.deleted_index.clear()
            self.ui.deleted_index.setFocus()
            return
        reply = QMessageBox.question(
            self, 
            "Подтверждение", 
            f"Вы уверены, что хотите удалить запись с ID {cost_id}?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            result = self.db.DeleteCost(cost_id)
            if result:
                self.ui.deleted_index.clear()
                self.refresh_table()
                QMessageBox.information(self, "", f"Запись с ID {cost_id} удалена!")
            else:
                QMessageBox.warning(self, "!", f"Запись с ID {cost_id} не найдена!")
                self.ui.deleted_index.clear()
                self.ui.deleted_index.setFocus()
    
    def apply_filter(self):
        filter_text = self.ui.filter.text().strip()
        self.load_costs(filter_text)
        if filter_text:
            self.statusBar().showMessage(f"Фильтр: '{filter_text}'", 3000)
        else:
            self.statusBar().showMessage("Все записи", 2000)
    
    def auto_search(self):
        filter_text = self.ui.filter.text().strip()
        if len(filter_text) >= 1:
            self.load_costs(filter_text)
    
    def refresh_table(self):
        self.ui.filter.clear()
        self.load_costs()
        self.statusBar().showMessage("Таблица обновлена", 2000)
    
    def closeEvent(self, event):
        self.db.CloseSonnection()
        event.accept()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Car Cost Controller")

    app.setStyleSheet("""
        QMessageBox {
            font-size: 10px;
        }
        QMessageBox QLabel {
            font-size: 10px;
        }
        QMessageBox QPushButton {
            font-size: 11px;
            min-width: 70px;
            min-height: 25px;
        }
    """)
    
    window = CarCostController()
    window.setWindowTitle("Car Cost Controller")
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
