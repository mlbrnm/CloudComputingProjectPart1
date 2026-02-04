import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
df = pd.read_csv('All_Diets.csv')

# handle missing data (fill missing values with mean)
df.fillna(df.mean(), inplace=True)

# calculate the average macronurtrient content for each diet type
avg_macros = df.groupby('Diet_type')[['Protein(g)', 'Carbs(g)', 'Fat(g)']].mean()
print("\nAverage macronutrient content for each diet type:")
print(avg_macros)

# find the top 5 protein-rich recipes for each diet type
top_protein = df.sort_values('Protein(g)', ascending=False).groupby('Diet_type').head(5)
print("\nTop 5 protein-rich recipes per diet type:")
print(top_protein[['Diet_type', 'Recipe_name', 'Protein(g)']])

# add new metrics (protein-to-carbs ratio and carbs-to-fat ratio)
df['Protein_to_Carbs_ratio'] = df['Protein(g)'] / df['Carbs(g)']
df['Carbs_to_Fat_ratio'] = df['Carbs(g)'] / df['Fat(g)']

# find the diet type with the highest protein content
highest_protein_diet = df.groupby('Diet_type')['Protein(g)'].sum().idxmax()
print(f"\nDiet type with highest total protein content: {highest_protein_diet}")

# identify the most common cuisines for each diet type
most_common_cuisines = df.groupby('Diet_type')['Cuisine_type'].agg(lambda x: x.mode()[0] if not x.mode().empty else 'N/A')
print("\nMost common cuisine for each diet type:")
print(most_common_cuisines)


# Chart 1: Bar chart for average protein
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_macros.index, y=avg_macros['Protein(g)'])
plt.title('Average Protein by Diet Type')
plt.xlabel('Diet Type')
plt.ylabel('Average Protein (g)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 2: Bar chart for average carbs
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_macros.index, y=avg_macros['Carbs(g)'])
plt.title('Average Carbs by Diet Type')
plt.xlabel('Diet Type')
plt.ylabel('Average Carbs (g)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 3: Bar chart for average fat
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_macros.index, y=avg_macros['Fat(g)'])
plt.title('Average Fat by Diet Type')
plt.xlabel('Diet Type')
plt.ylabel('Average Fat (g)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
