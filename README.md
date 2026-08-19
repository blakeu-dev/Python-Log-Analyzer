# IT Support Ticket Analyzer (Python)

A Python application that processes and analyzes IT support ticket data from a CSV file. This project models each ticket as an object, performs frequency and pattern analysis and generates visualizations to highlight recurring issues across departments. 

## Features 🚀

- Object-oriented design using LogEntry and Analyzer classes
- CSV parsing with automatic timestamp conversion
- Error frequency analysis
- Department workload analysis
- Hour-by-hour ticket pattern detection
- Matplotlib bar chart visualization
- Clean and modular code

## Dataset 🗃️

-Ticket ID
-Timestamp
- Error Code
- Description
- Department
- Priority

Example Row:

T-101, 2025-10-01 12:00:00, 50, Printer Failure on PRADM02, Admin, Medium


## How It Operates 🧠

1. CSV Loader
Reads the CSV file and converts each row into LogEntry object.

2. LogEntry Class
Stores ticket information and provides helper methods for timestamps, summaries, etc

3. Analyzer Class
Performs error frequency counting, department load analysis, and hourly ticket pattern detection

4. Visualization
Generates a bar chart showing how often each error code appears using Matplotlib


## 📊 Example Output

- Error code frequency report  
- Department ticket counts  
- Hourly ticket distribution  
- Matplotlib bar chart  

## 🛠️ Technologies Used

- Python 3  
- `csv` 
- `datetime`  
- `matplotlib`  

## 📈 Future Improvements

- Add command‑line arguments for selecting CSV files or analysis modes  
- Add unit tests for `LogEntry` and `Analyzer`  
- Build a GUI 
- Add trend analysis (e.g., busiest days, average resolution time)  
- Create a web dashboard using Flask or FastAPI  
- Add error‑code severity mapping for smarter insights  

## 📄 License

MIT License

