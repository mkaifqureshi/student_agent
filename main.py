class StudentAgent:
    def __init__(self):
        self.students = []  # List to store student dictionaries
        self.unique_names = set()  # Set for duplicate prevention

    def calculate_average(self, marks):
        return sum(marks) / len(marks) if marks else 0

    def get_grade(self, avg):
        if avg >= 80: return "A"
        if avg >= 60: return "B"
        if avg >= 40: return "C"
        return "Fail"

    def add_student(self):
        print("\n--- 📝 Add New Student ---")
        name = input("Enter Student Name: ").strip()
        
        if name.lower() in {n.lower() for n in self.unique_names}:
            print(f"⚠️ Error: Student '{name}' already exists!")
            return

        try:
            age = int(input("Enter Age: "))
            # Using split() and list comprehension
            marks_raw = input("Enter marks for 3 subjects (comma-separated): ")
            marks = [float(m.strip()) for m in marks_raw.split(',')]
            
            if len(marks) != 3:
                print("⚠️ Please enter exactly 3 marks.")
                return
        except ValueError:
            print("❌ Invalid input! Age and Marks must be numeric.")
            return

        # Data Processing & Agent Logic
        avg = self.calculate_average(marks)
        grade = self.get_grade(avg)
        
        student_data = {
            "name": name,
            "age": age,
            "marks": marks,
            "average": round(avg, 2),
            "grade": grade
        }

        self.students.append(student_data)
        self.unique_names.add(name)
        print(f"✅ {name} added successfully!")
        
        # Agent Behavior
        if avg > 85: print("🌟 Agent Note: Top Student Detected!")
        elif avg < 40: print("📉 Agent Note: Needs Improvement.")

    def view_students(self):
        if not self.students:
            print("\n📂 Database is empty.")
            return

        print("\n" + "="*50)
        print(f"{'Name':<15} | {'Age':<5} | {'Average':<8} | {'Grade':<5}")
        print("-" * 50)
        for s in self.students:
            # Using join() and replace() for formatting
            marks_str = ", ".join(map(str, s['marks'])).replace(".0", "")
            print(f"{s['name']:<15} | {s['age']:<5} | {s['average']:<8} | {s['grade']:<5}")

    def search_student(self):
        query = input("\nEnter name to search: ").lower()
        found = False
        for s in self.students:
            # Using .find() and .lower() as requested
            if s['name'].lower().find(query) != -1:
                print(f"\n🔍 Match Found: {s}")
                found = True
        if not found:
            print("❓ No student found matching that name.")

    def run(self):
        while True:
            print("\n🤖 SMART STUDENT AGENT MENU")
            print("1. Add Student\n2. View All\n3. Search\n4. Exit")
            
            choice = input("Select an option (1-4): ")

            match choice:
                case "1":
                    self.add_student()
                case "2":
                    self.view_students()
                case "3":
                    self.search_student()
                case "4":
                    print("👋 System shutting down. Goodbye!")
                    break
                case _:
                    print("❗ Invalid choice, try again.")
                    continue

# --- Entry Point ---
if __name__ == "__main__":
    agent = StudentAgent()
    agent.run()
