Big Data Analysis Project Using Python

Project Overview:
This project showcases how Python can be used to analyze a small dataset, focusing on key tasks such as data aggregation, filtering, and visualization. The dataset contains student performance data across different subjects, providing insights into:

Average Marks by Subject
Students Scoring Above a Specific Threshold
Grade Distribution
By utilizing Python and libraries such as Pandas and Matplotlib, this project demonstrates the power of data analysis, a crucial aspect of Big Data analytics.

Technologies Used:
This project leverages the following technologies:
Python: The primary programming language for data manipulation, analysis, and visualization.
Pandas: A powerful Python library used for data manipulation and analysis.
Matplotlib: A popular Python library for creating visualizations such as bar charts and pie charts.
Jupyter Notebook: An interactive environment for running Python code and visualizing data.

Dataset Description
The dataset used in this project contains the following columns:
StudentID: A unique identifier for each student.
Name: The name of the student.
Subject: The subject of study (Math, Science, English).
Marks: The marks obtained by the student in the subject.
Grade: The grade assigned to the student (A, B, C).

Sample Data
| StudentID | Name   | Subject | Marks | Grade |
|-----------|--------|---------|-------|-------|
| 1         | John   | Math    | 85    | A     |
| 2         | Susan  | Science | 78    | B     |
| 3         | Alex   | Math    | 92    | A     |
| 4         | Emily  | Science | 68    | C     |
| 5         | Tom    | English | 74    | B     |
| 6         | Anna   | Math    | 89    | A     |
| 7         | Robert | English | 65    | C     |
| 8         | Linda  | Science | 72    | B     |


Key Analysis Queries
The following key queries were performed on the dataset:

Average Marks by Subject
We calculated the average marks obtained by students in each subject.

Students Scoring Above 80
We filtered out and displayed students who scored more than 80 marks.

Grade Distribution
We counted and displayed the number of students in each grade category (A, B, C).

Visualizations
The following visualizations were created to better understand the dataset:

Bar Chart: Represents the average marks obtained by students in each subject.
Pie Chart: Represents the grade distribution among the students.

How to Get Started
To run the project on your local machine, follow these simple steps:

Clone the Repository

git clone https://github.com/your-jeevajothiga/naan_mudhalvan_bigdata.git

Install Dependencies
Install the necessary Python libraries:
pip install pandas matplotlib
Run the Jupyter Notebook
Launch Jupyter Notebook:
jupyter notebook
Open the notebook file in the Jupyter interface and run the code cells to see the data analysis and visualizations.
Future Scope
Scalability: Although this project uses a small dataset, in real-world applications, tools like Hadoop and Hive can be used to handle much larger datasets. These tools are designed to scale across distributed systems, making them essential for Big Data processing.
Advanced Analytics: This project can be extended to include more complex analysis using frameworks like PySpark for distributed data processing and machine learning.
Conclusion
This project demonstrates how Python can be used to perform fundamental data analysis tasks, from data manipulation and aggregation to visualization. Although the dataset used here is small, the same principles can be applied to larger datasets, especially in Big Data environments where tools like Hadoop and Hive come into play.
## License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
