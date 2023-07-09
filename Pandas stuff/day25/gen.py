import pandas

data = pandas.read_csv("./weather_data.csv")
mon = data[data.day == "Monday"]
print(32 + mon.temp * 9/5)

student_data = {
    "student": ["john", "amy", "paul"],
    "score": [70, 80, 90],
    "grade": ['C', 'B', 'A']
}
print(student_data)


stud = pandas.DataFrame(student_data)
stud.to_csv("./studentDetails.csv")
right = Button(width=20, height=20, image=right_img)
right.grid(row=1, column=0)right = Button(width=20, height=20, image=right_img)
right.grid(row=1, column=0)