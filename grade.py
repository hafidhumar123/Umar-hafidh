score = 47
grade = ""

"""
0 - 39 F9
40 - 44 E8
45 - 49 D7
50 - 54 C6
55 - 59 C5
60 - 64 C4
65 - 69 B3
70 - 74 B2
75 - 100 A1
"""
if score < 40:
    grade = "F9"
elif score > 39 and score < 45:
    grade = "E8"
elif score > 44 and score < 50:
    grade = "D7"
elif score > 49 and score < 55:
    grade = "C6"
elif score > 54 and score < 60:
    grade = "C5"
elif score > 59 and score < 65:
    grade = "C4"
elif score > 64 and score < 70:
    grade = "B3"
elif score > 69 and score < 75:
    grade = "B2"
elif scor > 74 and score < 101:
    grade = "A1"
    