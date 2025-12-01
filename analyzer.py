import csv


class LogEntry:
    #constructor
    def __init__(self, ticket_data):
        
        #assigning to instance variables
        self.ticket_id = ticket_data['TicketID']
        self.timestamp = ticket_data['Timestamp']
        self.error_code = ticket_data['ErrorCode']
        self.description = ticket_data['Description']
        self.department = ticket_data['Department']
        self.priority = ticket_data['Priority']
        
    def get_incident(self):

        #Returns string summary of entry for reporting

        return f"[{self.department} Ticket {self.ticket_id}, P: {self.priority} Error {self.error_code} {self.description}]"

class Analyzer:
    def __init__(self, entries):
        
        self.entries = entries


    def count_error_frequency(self):
        
        error_count = {}
        for entry in self.entries:

            code = entry.error_code

            if code in error_count:
                error_count[code] += 1 

            else:
                error_count[code] = 1
        return error_count


    def filter_by_department(self, department):
        filtered_tickets = []
        for entry in self.entries:
            if entry.department == department:
                filtered_tickets.append(entry)
        return filtered_tickets
    
    def analyze_department_load(self):
        department_count = {}
        different_departments = set()

        for entry in self.entries:
            different_departments.add(entry.department)

        for department_name in different_departments:
            filtered_list = self.filter_by_department(department_name)
            department_count[department_name] = len(filtered_list)     

        return department_count       
    



#keep outside of Analyzer class
def load_data(filename):

    entries_lst = []
    try:
        with open(filename, mode = 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_ob = LogEntry(row)
                entries_lst.append(new_ob)
        return entries_lst
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found")
        return []
    

if __name__ == "__main__":
    FILE_NAME = 'support_data.csv'
    all_entries = load_data(FILE_NAME)

    if all_entries:
        analysis_tool = Analyzer(all_entries)
        print(f"Successfully loaded and initialized Analyzer with {len(all_entries)} tickets.")

        error_report = analysis_tool.count_error_frequency()
        print("\n--- TOP RECURRING ERRORS ---")

        for code, count in error_report.items():
            print(f"Error code{code}: {count} instances")

        """admin_tickets = analysis_tool.filter_by_department('Admin')
        print (f"\n----- ADMIN DEPARTMENT LOAD -----")
        print(f"Total tickets for Admin: {len(admin_tickets)}")

        for ticket in admin_tickets:
                print (f"   {ticket.get_incident()}")"""
        
        department_report = analysis_tool.analyze_department_load()

        print("\n--- Comprehensive Department Load ---")

        for dept, count in department_report.items():
            print(f"Department{dept}: {count} tickets")