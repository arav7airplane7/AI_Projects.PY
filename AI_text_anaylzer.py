 
import pandas as pd
file_path = r"C:\Users\a_bha\OneDrive\Desktop\AI projects\student_marks_large.csv"
# Load CSV file of student marks
try:
    df = pd.read_csv(file_path, encoding="utf-8-sig", sep=None, engine="python")
    print("📄 CSV Loaded Successfully!\n")
except FileNotFoundError:
    print("❌ Error: 'student_marks.csv' not found in the folder.")
    exit()
 
# Fill any missing marks with 0
df['Marks'] = df['Marks'].fillna(0)
 
# Drop rows where 'Name' is missing
df = df.dropna(subset=['Name'])
 
# Display basic data
print("📋 Student Data:")
print(df)
 
# Calculate average marks
avg_marks = df['Marks'].mean()
max_marks = df['Marks'].max()
 
print(f"\n📊 Average Marks: {avg_marks}")
print(f"🏅 Highest Marks: {max_marks}")
 
# Filter students who scored 80 or above
top_scorers = df[df['Marks'] >= 80]
print("\n🌟 High Performers (80+ Marks):")
print(top_scorers)
 
# ----------------------------------------------
# ✨ ADDITIONAL ACTIVITY: Add Remark (Pass/Fail)
# ----------------------------------------------
df['Remark'] = df['Marks'].apply(lambda x: 'Pass' if x >= 33 else 'Fail')
 
# Save updated data to new CSV
df.to_csv("updated_student_marks.csv", index=False)
 
print("\n✅ Remarks added and saved to 'updated_student_marks.csv'")
 
 

