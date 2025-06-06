import pandas as pd
import numpy as np

input_dict = {
    'ID': [101, 102, 103, 104, 105, 106],
    'Name': ['An', 'Bình', 'Cường', 'Dương', np.nan, 'Hạnh'],
    'Age': [25, np.nan, 30, 22, 28, 35],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', np.nan],
    'Salary': [700, 800, 750, np.nan, 710, 770]
}

df_nv = pd.DataFrame(input_dict)

df_pb = pd.DataFrame({
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'Manager': ['Trang', 'Khoa', 'Minh', 'Lan']
})

print("Số lượng ô bị thiếu theo cột:", df_nv.isnull().sum())

df_nv = df_nv[df_nv.isnull().sum(axis=1) <= 2]

df_nv['Name'] = df_nv['Name'].fillna("Chưa rõ")
df_nv['Age'] = df_nv['Age'].fillna(df_nv['Age'].mean())
df_nv['Salary'] = df_nv['Salary'].fillna(method='ffill')
df_nv['Department'] = df_nv['Department'].fillna("Unknown")

df_nv['Age'] = df_nv['Age'].astype(int)
df_nv['Salary'] = df_nv['Salary'].astype(int)

df_nv['Salary_after_tax'] = df_nv['Salary'] * 0.9

filtered_nv = df_nv[(df_nv['Department'] == 'IT') & (df_nv['Age'] > 25)]
print("\nNhân viên phòng IT có tuổi > 25:\n", filtered_nv)

df_nv_sorted = df_nv.sort_values(by='Salary_after_tax', ascending=False)
print("\nBảng Nhân viên sắp xếp theo lương sau thuế:\n", df_nv_sorted)

avg_salary_per_dept = df_nv.groupby('Department')['Salary'].mean().reset_index()
print("\nLương trung bình theo phòng ban:\n", avg_salary_per_dept)

df_nv_with_manager = pd.merge(df_nv, df_pb, on='Department', how='left')
print("\nBảng Nhân viên có thêm tên Quản lý:\n", df_nv_with_manager)

new_nv = pd.DataFrame({
    'ID': [107, 108],
    'Name': ['Lan', 'Hòa'],
    'Age': [26, 29],
    'Department': ['Marketing', 'Finance'],
    'Salary': [780, 760]
})
new_nv['Salary_after_tax'] = new_nv['Salary'] * 0.9

df_nv_final = pd.concat([df_nv_with_manager, new_nv], ignore_index=True)
print("\nBảng Nhân viên sau khi thêm nhân viên mới:\n", df_nv_final)

