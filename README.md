# Python_capstone_project
Employee Dataset Analysis
Project Overview
This project analyzes an employee dataset to uncover insights about workforce distribution, salary allocations, and demographic patterns. The analysis tasks include preprocessing the data, performing exploratory data analysis (EDA), visualizing key trends, and deriving actionable insights. The project highlights how data-driven decisions can optimize workforce management and resource allocation.

## Dataset
The dataset contains the following columns:
Team: The team to which an employee belongs.
Position: The role or designation of the employee.
Age: The age of the employee.
Salary: The salary earned by the employee.
Height: Height of the employee (randomized in preprocessing).

## Preprocessing Steps
Handling Missing Values:
Missing values in the Salary column were filled with the median salary.

Data Cleaning:
Randomized the Height column values between 150 and 180 for analysis consistency.

Feature Engineering:
Added a new column, AgeGroup, by binning ages into predefined intervals (e.g., 20-30, 30-40).

## Analysis Tasks and Insights

1.  Distribution of Employees Across Teams
Objective: Identify the distribution of employees across teams and calculate their percentage split.
Visualization: Bar chart and pie chart.
Insight: The "New Orleans Pelicans" team has the highest percentage of employees, while "Minnesota Timberwolves" has the least. Most teams have similar employee distribution, reflecting balanced workforce allocation.

2. Segregation by Positions
Objective: Group employees based on their positions within the company.
Visualization: Horizontal bar chart.
Insight: The "SG" role has the highest number of employees, while the "C" role has the least. This indicates a focus on specific operational roles.

3. Predominant Age Group
Objective: Identify the most common age group among employees.
Visualization: Histogram.
Insight: The "20-30" age group is the largest, suggesting a predominantly young workforce.

4. Team and Position with the Highest Salary Expenditure
Objective: Determine which team and position have the highest salary allocation.
Visualization: Bar chart with team and position breakdown.
Insight: The "Los Angeles Lakers" team, specifically the "SF" position, has the highest salary expenditure. This reflects strategic investment in critical roles.

 5. Correlation Between Age and Salary
Objective: Investigate the relationship between age and salary.
Visualization: Scatter plot with a trendline.
Insight: A weak positive correlation (r=0.21) was observed, indicating a slight tendency for salaries to increase with age.

## Conclusion

This project highlights several key trends:

1. Workforce distribution is balanced across most teams, with a few outliers.
2. Operational roles like "SG" dominate, while specialized roles like "C" are fewer.
3. The organization invests heavily in specific teams and positions, reflecting strategic priorities.
4. A predominantly young workforce suggests opportunities for long-term growth and retention strategies.
5. Weak correlation between age and salary indicates that experience alone may not significantly influence pay.
