import sys
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QFormLayout, QTableWidget, QTableWidgetItem, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from algorithms import Process, fcfs_scheduling, round_robin_scheduling, priority_scheduling
import random

class ProcessSchedulingApp(QWidget):
    def __init__(self):
        super().__init__()

        # Khởi tạo giao diện người dùng
        self.setWindowTitle("Process Scheduling Simulator")
        self.setGeometry(100, 100, 1000, 700)  # Adjusted the window size for the chart

        # Layout chính
        self.layout = QVBoxLayout()

        # Tạo các widget nhập liệu
        self.pid_entry = QLineEdit(self)
        self.arrival_time_entry = QLineEdit(self)
        self.burst_time_entry = QLineEdit(self)
        self.priority_entry = QLineEdit(self)
        self.time_quantum_entry = QLineEdit(self)

        # Chọn thuật toán
        self.algorithm_choice = QComboBox(self)
        self.algorithm_choice.addItems(["FCFS", "Round Robin", "Priority Scheduling"])

        # Thêm các widget vào layout
        form_layout = QFormLayout()
        form_layout.addRow("PID:", self.pid_entry)
        form_layout.addRow("Arrival Time:", self.arrival_time_entry)
        form_layout.addRow("Burst Time:", self.burst_time_entry)
        form_layout.addRow("Priority (Optional):", self.priority_entry)
        form_layout.addRow("Time Quantum (for Round Robin):", self.time_quantum_entry)

        self.layout.addLayout(form_layout)

        # Bảng Tiến Trình
        self.process_table = QTableWidget(self)
        self.process_table.setColumnCount(4)
        self.process_table.setHorizontalHeaderLabels(["PID", "Arrival Time", "Burst Time", "Priority"])
        self.layout.addWidget(self.process_table)

        # Nút thêm tiến trình và chạy thuật toán
        self.add_button = QPushButton("Add Process", self)
        self.add_button.clicked.connect(self.add_process)
        self.layout.addWidget(self.add_button)

        self.run_button = QPushButton("Run", self)
        self.run_button.clicked.connect(self.run_algorithm)
        self.layout.addWidget(self.run_button)

        # Nút clear bảng
        self.clear_button = QPushButton("Clear Table", self)
        self.clear_button.clicked.connect(self.clear_table)
        self.layout.addWidget(self.clear_button)

        # Bảng Kết Quả
        self.result_table = QTableWidget(self)
        self.result_table.setColumnCount(6)
        self.result_table.setHorizontalHeaderLabels(["PID", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time", "Completion Time"])
        self.layout.addWidget(self.result_table)

        # Kết quả hiển thị
        self.result_label = QLabel("Results will be shown here", self)
        self.layout.addWidget(self.result_label)

        # Thêm không gian cho biểu đồ
        self.chart_label = QLabel("Gantt Chart", self)
        self.layout.addWidget(self.chart_label)

        self.canvas = FigureCanvas(plt.figure(figsize=(10, 4)))
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

        # Danh sách tiến trình
        self.processes = []

    def add_process(self):
        try:
            # Lấy các thông tin đầu vào từ giao diện
            pid = int(self.pid_entry.text())
            arrival_time = int(self.arrival_time_entry.text())
            burst_time = int(self.burst_time_entry.text())
            priority = int(self.priority_entry.text()) if self.priority_entry.text() else None

            # Tạo tiến trình và thêm vào danh sách
            new_process = Process(pid, arrival_time, burst_time, priority)
            self.processes.append(new_process)

            # Thêm vào bảng tiến trình
            row_position = self.process_table.rowCount()
            self.process_table.insertRow(row_position)
            self.process_table.setItem(row_position, 0, QTableWidgetItem(str(pid)))
            self.process_table.setItem(row_position, 1, QTableWidgetItem(str(arrival_time)))
            self.process_table.setItem(row_position, 2, QTableWidgetItem(str(burst_time)))
            self.process_table.setItem(row_position, 3, QTableWidgetItem(str(priority if priority else 'N/A')))

            # Xóa các trường nhập liệu sau khi thêm
            self.pid_entry.clear()
            self.arrival_time_entry.clear()
            self.burst_time_entry.clear()
            self.priority_entry.clear()

        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter valid numbers.")

    def run_algorithm(self):
        try:
            # Kiểm tra lựa chọn thuật toán và chạy
            if self.algorithm_choice.currentText() == "FCFS":
                fcfs_scheduling(self.processes)
            elif self.algorithm_choice.currentText() == "Round Robin":
                time_quantum = int(self.time_quantum_entry.text())
                round_robin_scheduling(self.processes, time_quantum)
            elif self.algorithm_choice.currentText() == "Priority Scheduling":
                priority_scheduling(self.processes)

            # Cập nhật bảng kết quả
            self.update_result_table()

            # Vẽ Gantt Chart
            self.plot_gantt_chart()

        except ValueError:
            QMessageBox.critical(self, "Input Error", "Please enter valid numbers.")

    def update_result_table(self):
        # Cập nhật bảng kết quả sau khi chạy thuật toán
        self.result_table.setRowCount(0)  # Xóa các hàng cũ trong bảng kết quả
        for process in self.processes:
            row_position = self.result_table.rowCount()
            self.result_table.insertRow(row_position)
            self.result_table.setItem(row_position, 0, QTableWidgetItem(str(process.pid)))
            self.result_table.setItem(row_position, 1, QTableWidgetItem(str(process.arrival_time)))
            self.result_table.setItem(row_position, 2, QTableWidgetItem(str(process.burst_time)))
            self.result_table.setItem(row_position, 3, QTableWidgetItem(str(process.waiting_time)))
            self.result_table.setItem(row_position, 4, QTableWidgetItem(str(process.turnaround_time)))
            self.result_table.setItem(row_position, 5, QTableWidgetItem(str(process.completion_time)))

    def clear_table(self):
        # Xóa tất cả các tiến trình và kết quả
        self.processes.clear()
        self.process_table.setRowCount(0)
        self.result_table.setRowCount(0)
        self.result_label.setText("Results will be shown here")
        self.canvas.figure.clear()  # Clear the Gantt chart
        self.canvas.draw()

    def plot_gantt_chart(self):
        # Vẽ biểu đồ Gantt
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.set_title("Process Gantt Chart")
        ax.set_xlabel("Time")
        ax.set_ylabel("Process ID")

        start_times = []
        end_times = []
        process_ids = []
        colors = []

        # Tính toán thời gian bắt đầu và kết thúc cho mỗi tiến trình
        current_time = 0
        for process in self.processes:
            start_times.append(current_time)
            end_time = current_time + process.burst_time
            end_times.append(end_time)
            process_ids.append(process.pid)
            colors.append(self.get_random_color())  # Chọn màu ngẫu nhiên cho tiến trình
            current_time = end_time  # Cập nhật thời gian kết thúc

        # Vẽ các thanh trong biểu đồ Gantt với màu sắc
        ax.barh(process_ids, [end - start for start, end in zip(start_times, end_times)], left=start_times, color=colors)
        ax.set_xlim(0, current_time)

        self.canvas.figure = fig
        self.canvas.draw()

    def get_random_color(self):
        # Hàm tạo màu ngẫu nhiên dưới dạng hex
        return f"#{random.randint(0, 0xFFFFFF):06x}"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProcessSchedulingApp()
    window.show()
    sys.exit(app.exec_())
