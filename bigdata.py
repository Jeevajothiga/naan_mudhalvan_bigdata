!pip install matplotlib
!pip install pandas
import pandas as pd
import matplotlib.pyplot as plt
data = {
    "StudentID": [1, 2, 3, 4, 5, 6, 7, 8],
    "Name": ["John", "Susan", "Alex", "Emily", "Tom", "Anna", "Robert", "Linda"],
    "Subject": ["Math", "Science", "Math", "Science", "English", "Math", "English", "Science"],
    "Marks": [85, 78, 92, 68, 74, 89, 65, 72],
    "Grade": ["A", "B", "A", "C", "B", "A", "C", "B"]
}
df = pd.DataFrame(data)
# Query 1: Average Marks by Subject
def query_average_marks():
    avg_marks = df.groupby("Subject")["Marks"].mean().reset_index()
    print("Average Marks by Subject:")
    print(avg_marks)
    
    # Plotting the bar chart for average marks by subject
    avg_marks.plot(kind='bar', x='Subject', y='Marks', legend=False, color='skyblue')
    plt.title('Average Marks by Subject')
    plt.ylabel('Average Marks')
    plt.xlabel('Subject')
    plt.tight_layout()
    plt.show()

# Query 2: Students Scoring Above 80
def query_students_above_80():
    above_80 = df[df["Marks"] > 80]
    print("Students Scoring Above 80 Marks:")
    print(above_80)

# Query 3: Grade Distribution
def query_grade_counts():
    grade_counts = df["Grade"].value_counts().reset_index()
    grade_counts.columns = ["Grade", "StudentCount"]
    print("Grade Distribution:")
    print(grade_counts)
    
    # Plotting the pie chart for grade distribution
    grade_counts.set_index("Grade").plot(kind='pie', y='StudentCount', autopct='%1.1f%%', legend=False)
    plt.title('Grade Distribution')
    plt.ylabel('')  # Hide y-axis label
    plt.tight_layout()
    plt.show()

# Menu to select queries
while True:
    print("Choose a query:\n1. Average Marks by Subject\n2. Students Scoring Above 80\n3. Grade Distribution\n4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        query_average_marks()
    elif choice == "2":
        query_students_above_80()
    elif choice == "3":
        query_grade_counts()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again!")
