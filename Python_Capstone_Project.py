#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns




# In[2]:


#Loading the dataset
df = pd.read_csv(r"C:\Users\ramsi\Downloads\myexcel - myexcel.csv.csv")


# In[3]:


# Preprocessing
#Replacing Height column with random numbers between 150 and 180
df["Height"] = np.random.randint(150, 181, size=df.shape[0])


# In[ ]:





# In[5]:


# missing salary fill using median value
df["Salary"].fillna(df["Salary"].median(), inplace=True)


# In[17]:


df.isnull().sum()


# In[6]:


# Analysis Tasks

#1. Distribution of employees across teams
team_distribution = df["Team"].value_counts()
team_percentage = (team_distribution / len(df)) * 100
print(f"Team distribution is : {team_distribution}")
print(f"\nTeam percentage is :{team_percentage}")


# In[7]:


# 2. Segregation by positions
position_distribution = df["Position"].value_counts()
position_distribution


# In[8]:


# 3. Predominant age group
age_bins = [20, 30, 40, 50, 60]
age_labels = ["20-30", "30-40", "40-50", "50-60"]
df["AgeGroup"] = pd.cut(df["Age"], bins=age_bins, labels=age_labels)
age_group_distribution = df["AgeGroup"].value_counts()

max_age_group = age_group_distribution.idxmax()


# In[9]:


# 4. Team and position with highest salary expenditure
group_salary = df.groupby(["Team", "Position"])['Salary'].sum().reset_index()
highest_salary_team = group_salary.loc[group_salary["Salary"].idxmax()]

print(f"Highest salary team is : {highest_salary_team['Team']}")


# In[10]:


# 5. Correlation between age and salary
correlation = df["Age"].corr(df["Salary"])
print(f"{correlation:.2f}")


# From the percentage distribution of employees across teams data analysis,
# it is observed, "New Orleans Pelicans" team has the highest percentage distribution of employees and
# "Minnesotta Timberwolves" team has the least percentage distribution of employees.
# 
# Apart from very few teams, most of the teams have an equal percentage distribution of employees.
# 
# 
# 
# 

# In[11]:


#VISUALIZATION

#Team distribution - Bar Chart
plt.figure(figsize=(10, 6))
sns.barplot(x=team_percentage.index, y=team_percentage.values, palette="pastel")
plt.title("Percentage Distribution of Employees Across Teams")
plt.xlabel("Team")
plt.ylabel("Percentage of Employees")

plt.xticks(rotation=90)
plt.show()


# In[12]:


#Position distribution - Horizontal Bar Chart
plt.figure(figsize=(8, 6))
sns.barplot(x=position_distribution.values, y=position_distribution.index, palette="rainbow")
plt.title("Distribution of Employees by Position")
plt.xlabel("Number of Employees")
plt.ylabel("Position")
plt.show()


# In[13]:


#Predominant age group - Histogram
plt.figure(figsize=(8, 6))
sns.histplot(df["Age"], bins=age_bins, kde=False, color="lightblue")
plt.title("Age Distribution of Employees")
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")
plt.xticks(age_bins)
plt.show()


# In[14]:


#Team and position with highest salary expenditure
plt.figure(figsize=(10, 8))
sns.barplot(
    x="Salary",
    y="Team",
    hue="Position",
    data=group_salary,
    palette="muted"
)
plt.title("Salary Expenditure by Team and Position")
plt.xlabel("Total Salary Expenditure")
plt.ylabel("Team")
plt.show()


# In[15]:


#Correlation between age and salary - Scatter Plot
plt.figure(figsize=(8, 6))
sns.scatterplot(x="Age", y="Salary", data=df, color="purple", alpha=0.6)
plt.title(f"Correlation Between Age and Salary (r={correlation:.2f})")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()


# # Data Story and Insights
# 

# In[16]:


Data Story:
Provide insights gained from the analysis, highlighting key trends, patterns, and correlations within the dataset. (3 marks)

Timely Submission:
Ensure timely submission of your project to earn an additional mark. (1 mark)


# ## Data Story and Insights
# 
# 
# 
# 1. From the percentage distribution of employees across teams data analysis,
# it is observed, "New Orleans Pelicans" team has the highest percentage distribution of employees and
# "Minnesotta Timberwolves" team has the least percentage distribution of employees.
# Apart from very few teams, most of the teams have an equal percentage distribution of employees.
# 
# 
# 
# 

# 2. From the "distribution of employees by position" chart, it is observed, that most number of employees are working as "SG" role in the organization and least number of employees are working in the role "C". The most common position represents the majority workforce, showcasing the focus on specific roles.

# 3. From the age distribution of employees graph, it is observed the most frequent age group (e.g., "20-30") represents the majority workforce, indicating the general experience level of employees are young to middle-age level.

# 4. "The Salary expenditure by Team and Position" graph highlights salary expenditures across different teams and positions within the company. It is observed, teams like the Los Angeles Lakers and Golden State Warriors allocate significantly higher budgets across various positions, indicating a focus on retaining highly paid employees in critical roles. 
# Positions such as PF and SF often have the highest salaries, reflecting their importance in the company’s operational strategy. 
# In contrast, teams like Houston Rockets and Oklahoma City Thunder demonstrate more modest spending, possibly due to budget constraints or restructuring efforts. Balanced salary distributions, seen in teams like Miami Heat and Denver Nuggets, suggest a focus on maintaining well-rounded team structures. 
# Overall, the graph underscores how salary allocation reflects the company’s strategic priorities and workforce management approach.

# 5. The corelation between Age (x-axis) and Salary (y-axis) graph depicts, the relation between Age and Salary with a correlation coefficient '𝑟' = 0.21. 
# It is observed that a corelation factor r=0.21 indicates a weak positive correlation between age and salary. As age increases, there is a slight tendency for salaries to increase, but the relationship is not strong.

# In[ ]:




