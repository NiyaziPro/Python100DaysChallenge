import pandas

student_dict = {
    "student": ["Ani", "Fati", "Alex", "Lily"],
    "score": [58, 100, 76, 45]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

for (index, row) in student_data_frame.iterrows():
    print(row.student)
    print(row.score)