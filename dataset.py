import csv
import random

# Define study plans with labeled sections for easy HTML parsing
study_plans = {
    "Basic": """
Title: Basic Level Study Plan: Data Science and Machine Learning
Goal: Understand the basic concepts and types of machine learning.
Week 1-2:
    - Introduction to data science and machine learning
    - Difference between supervised, unsupervised, and reinforcement learning
    - Basic terms: dataset, features, labels, and models
Resources:
    - Coursera: Introduction to Data Science by IBM
    - YouTube: Data School - What is Machine Learning?

Week 3-4:
    - Get familiar with Python for data science.
    - Introduction to Python libraries: NumPy, Pandas, Matplotlib
    - Loading and manipulating datasets with Pandas
Resources:
    - Python for Data Analysis by Wes McKinney
    - Kaggle: Python Course
""",
    "Intermediate": """
Title: Intermediate Level Study Plan: Data Science and Machine Learning
Goal: Strengthen data manipulation and analysis skills.
Week 1-2:
    - Data wrangling with Pandas and NumPy
    - Handling missing values, data cleaning, and transformations
Resources:
    - Kaggle: Pandas Course
    - YouTube: Corey Schafer - Data Analysis with Pandas

Week 3-4:
    - Exploratory Data Analysis (EDA) and Visualization
    - Using Seaborn and Matplotlib for EDA
    - Statistical analysis and correlation studies
Resources:
    - Udacity: Data Visualization in Python
    - Towards Data Science: EDA Tutorial
""",
    "Advanced": """
Title: Advanced Level Study Plan: Data Science and Machine Learning
Goal: Master feature engineering techniques for model optimization.
Week 1-2:
    - Advanced feature engineering methods
    - Scaling, normalization, and encoding
Resources:
    - Coursera: Feature Engineering for Machine Learning by University of Washington
    - YouTube: StatQuest with Josh Starmer - Feature Engineering

Week 3-4:
    - Deep dive into complex machine learning models
    - Ensemble methods, boosting, and bagging
Resources:
    - Coursera: Advanced Machine Learning Specialization by HSE University
    - Book: Hands-On Machine Learning with Scikit-Learn and TensorFlow by Aurélien Géron
""",
    "Expert": """
Title: Expert Level Study Plan: Data Science and Machine Learning
Goal: Conduct research and optimize algorithms for production.
Week 1-2:
    - Advanced research methodologies
    - Hyperparameter tuning, optimization techniques
Resources:
    - Coursera: Machine Learning Specialization by Andrew Ng
    - Research Papers on arXiv

Week 3-4:
    - Model deployment techniques
    - Building APIs and using cloud platforms
Resources:
    - FastAPI Documentation
    - AWS Machine Learning Services
"""
}

# Define score to level mapping
score_to_level = {
    0: "Basic",
    10: "Basic",
    20: "Basic",
    30: "Basic",
    40: "Intermediate",
    50: "Intermediate",
    60: "Intermediate",
    70: "Advanced",
    80: "Advanced",
    90: "Expert",
    100: "Expert"
}

# Function to create dataset with labeled sections in completions
def create_dataset(file_name, num_records=100):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["prompt", "completion"])  # Header

        for _ in range(num_records):
            score = random.choice([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
            level = score_to_level[score]

            prompt = f"Student scored {score}% in the Data Science and Machine Learning quiz. " \
                     f"Provide a study plan for the {level} level, focusing on key concepts and resources."

            # Use labeled sections for completion to make it HTML-friendly
            completion = study_plans[level].strip()
            writer.writerow([prompt, completion])

# Create the dataset
create_dataset("study_plan_dataset.csv", num_records=200)
print("Dataset created successfully as 'study_plan_dataset.csv'")

