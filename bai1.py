import pandas as pd
data = {
    'Name': ['Vinh', 'Thành', 'Tuyết', 'Dũng', 'Hậu', 'Phong', 'Gíap', 'Hà', 'Khánh', 'Phương'],
    'Age': [20, 21, 21, 20, 21, 22, 22, 20, 21, 20],
    'Gender': ['Nam', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nam', 'Nữ', 'Nữ', 'Nam', 'Nữ'],
    'Score': [8, 7, 9, 6, 8, 7, 9, 8, 6, 9]
}
df_students = pd.DataFrame(data)
df_students.index = range(1, 11)

print(" * Toàn bộ dữ liệu:")
print(df_students)

print(" * 3 dòng đầu tiên:")
print(df_students.loc[[1,2,3]])

print(" * Theo index=2 và cột Name:")
print(df_students.loc[2, 'Name' ])

print(" * Theo index=2 và cột Name:")
print(df_students.loc[10, 'Age' ])

print(" * Cột Name và cột Score:")
print(df_students[['Name', 'Score']])

df_students['Pass'] = df_students['Score'] >= 5
print(" * Thêm cột Pass:")
print(df_students)

df_sorted = df_students.sort_values(by='Score', ascending=False)
print(" * Sắp xếp theo Score giảm dần:")
print(df_sorted)




