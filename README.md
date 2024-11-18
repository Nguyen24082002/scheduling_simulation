Process Scheduling Simulator - README
Mô tả
Ứng dụng Process Scheduling Simulator mô phỏng các thuật toán lập lịch CPU như:

First Come, First Served (FCFS)
Round Robin
Priority Scheduling
Ứng dụng cung cấp giao diện đồ họa (GUI) để người dùng:

Thêm tiến trình với các thông số như PID, Arrival Time, Burst Time, Priority, và Time Quantum.
Lựa chọn thuật toán lập lịch và xem kết quả.
Xem bảng kết quả chi tiết và biểu đồ Gantt của các tiến trình.
Yêu cầu hệ thống
Python 3.8+
Các thư viện Python:
PyQt5
matplotlib
Cách cài đặt
1. Clone repository hoặc tải xuống mã nguồn
bash
Copy code
git clone <repository_url>
cd <project_folder>
2. Cài đặt các thư viện yêu cầu
Sử dụng pip để cài đặt các thư viện cần thiết:

bash
Copy code
pip install PyQt5 matplotlib
Cách chạy ứng dụng
1. Mở terminal và điều hướng đến thư mục chứa mã nguồn:
bash
Copy code
cd <project_folder>
2. Chạy file Python chính:
bash
Copy code
python <tên_file_chính>.py
Ví dụ:

bash
Copy code
python process_scheduling_app.py
Hướng dẫn sử dụng
1. Nhập thông tin tiến trình:
PID: Mã định danh của tiến trình.
Arrival Time: Thời điểm tiến trình đến (số nguyên dương).
Burst Time: Thời gian tiến trình cần để hoàn thành.
Priority (Tùy chọn): Mức ưu tiên của tiến trình (dành cho Priority Scheduling).
Time Quantum: Chỉ áp dụng cho thuật toán Round Robin.
2. Chọn thuật toán lập lịch từ danh sách:
FCFS
Round Robin
Priority Scheduling
3. Thêm tiến trình:
Nhấn Add Process để thêm tiến trình vào bảng.
4. Chạy thuật toán:
Nhấn Run để tính toán và hiển thị kết quả:
Bảng kết quả: Bao gồm Waiting Time, Turnaround Time, và Completion Time.
Biểu đồ Gantt: Hiển thị thời gian thực hiện của các tiến trình.
5. Xóa bảng:
Nhấn Clear Table để xóa danh sách tiến trình và kết quả hiện tại.
Cấu trúc dự án
process_scheduling_app.py: File chính chứa mã giao diện và logic.
algorithms.py: File chứa các thuật toán lập lịch (FCFS, Round Robin, Priority Scheduling).
requirements.txt (tuỳ chọn): Danh sách các thư viện cần thiết.
Ghi chú
Khi sử dụng thuật toán Round Robin, đảm bảo điền Time Quantum.
Đảm bảo nhập các giá trị hợp lệ (số nguyên dương).
Nếu xảy ra lỗi, ứng dụng sẽ hiển thị hộp thoại cảnh báo.