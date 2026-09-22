print("Pabpal1418")

import pandas as pd
import matplotlib.pyplot as plt

students = [
    "Ana", "Ana", "Ben", "Ben", "Cara", "Cara", "Drew", "Drew", "Eli", "Eli",
    "Fay", "Fay", "Gabe", "Gabe", "Hana", "Hana", "Ian", "Ian", "Jade", "Jade"
]
subjects = [
    "Math", "Science", "Math", "Science", "Math", "Science", "Math", "Science",
    "Math", "Science", "Math", "Science", "Math", "Science", "Math", "Science",
    "Math", "Science", "Math", "Science"
]

grades = [
    88, 92, 91, 70, 79, 85, 95, 88, 84, 94,
    99, 81, 76, 77, 90, 96, 87, 83, 93, 89
]

# 3. Create an index for the student and subject using the multiindex function
index = pd.MultiIndex.from_arrays([students, subjects], names=("Student", "Subject"))

# 4. Careate a Dataframe of grades for each student for two subjetcs 
df = pd.DataFrame({"Grade": grades}, index=index)

# 5. Display the DataFrame
print(df)

# I just added this so it would look cleaner
print("----------------------")

# 6. Group by the mean of the subject
grouped = df.groupby(by=["Subject"]).mean()
print(grouped)

grouped["Grade"].plot(kind="bar")
plt.xlabel("Average Grade by Subject")
plt.xticks(rotation=0)
plt.title("Pabpal1418 Classroom Roster")
plt.show()
