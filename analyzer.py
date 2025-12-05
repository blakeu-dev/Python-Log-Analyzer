import csv
from datetime import datetime


class LogEntry:
    #Constructor
    #Runs whenever there is new LogEntry
    def __init__(self, ticket_data):
        
        #assigning to instance variables
        self.ticket_id = ticket_data['TicketID'].strip()
        self.timestamp = self.parse_timestamp(ticket_data['Timestamp'].strip())
        self.error_code = ticket_data['ErrorCode'].strip()
        self.description = ticket_data['Description'].strip()
        self.department = ticket_data['Department'].strip()
        self.priority = ticket_data['Priority'].strip()

    def parse_timestamp(self, timestamp):
        #Converts timestamp str to datetime obj

        try:
            return datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            print(f"Couldn't parse timestamp '{timestamp}'")
            return None
        
    def get_incident(self):

        #Returns string summary of entry for reporting

        return f"[{self.department} Ticket {self.ticket_id}, P: {self.priority} Error {self.error_code} {self.description}]"
    
    def get_hour(self):
        if self.timestamp:
            return self.timestamp.hour
        return None


    def get_date(self):
        if self.timestamp:
            return self.timestamp.date()
        return None


class Analyzer:
    def __init__(self, entries):
        #Constructor 
        #Stores list of LogEntry objects
        self.entries = entries


    def count_error_frequency(self):
        #Counts the amount of times a unique error occurs"
        error_count = {}
        for entry in self.entries:
            
            code = entry.error_code #Access error code

            if code in error_count:
                error_count[code] += 1 #If already seen, increment

            else:
                error_count[code] = 1 #If new, start at 1
        return error_count


    def filter_by_department(self, department):
        #Filters tickets to only include specific departments
        filtered_tickets = []
        for entry in self.entries:
            if entry.department == department:
                filtered_tickets.append(entry)
        return filtered_tickets
    
    def analyze_department_load(self):
        #Counts total ticket count for each department
        #Uses filter by department method
        department_count = {}
        different_departments = set() #set is used to find unique items

        #Finds different department names
        for entry in self.entries:
            different_departments.add(entry.department)

        #Find total count 
        for department_name in different_departments:
            filtered_list = self.filter_by_department(department_name)
            department_count[department_name] = len(filtered_list)     

        return department_count       
    



#keep outside of Analyzer class
def load_data(filename):
#Reads CSV, creates LogEntry objects, gives list
    entries_lst = []

    #Handles errors if CSV is missing
    try:
        #makes sure it safely opens and closes
        with open(filename, mode = 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                new_ob = LogEntry(row)
                entries_lst.append(new_ob)
        return entries_lst
    
    #Final snippet of error handling
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found")
        return []
    

if __name__ == "__main__":
    FILE_NAME = 'support_data.csv'
    all_entries = load_data(FILE_NAME)

    if all_entries:

        #Test code for datetime
        """for entry in all_entries[:3]:  # Test first 3 entries
            print(f"\nTicket ID: {entry.ticket_id}")
            print(f"  Timestamp object: {entry.timestamp}")
            print(f"  Hour: {entry.get_hour()}")
            print(f"  Date: {entry.get_date()}")""" 

        analysis_tool = Analyzer(all_entries)
        print(f"Successfully loaded and initialized Analyzer with {len(all_entries)} tickets.")

        error_report = analysis_tool.count_error_frequency()
        print("\n--- TOP RECURRING ERRORS ---")

        for code, count in error_report.items():
            print(f"Error code{code}: {count} instances")


        #This was single department report
        #Changed to give report for all departments
        """admin_tickets = analysis_tool.filter_by_department('Admin')
        print (f"\n----- ADMIN DEPARTMENT LOAD -----")
        print(f"Total tickets for Admin: {len(admin_tickets)}")

        for ticket in admin_tickets:
                print (f"   {ticket.get_incident()}")"""
        
        
        department_report = analysis_tool.analyze_department_load()

        print("\n--- Comprehensive Department Load ---")

        for dept, count in department_report.items():
            print(f"Department {dept}: {count} tickets")