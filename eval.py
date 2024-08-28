def add_student(d):
    dic = {}
    name = input("Enter name:")
    sid = input("Enter id:")
    clas = input("Enter clas:")
    grade1 = input("Enter grade 1:")
    grade2 = input("Enter grade 2:")
    grade3 = input("Enter grade 3:")
    dic.update({
        ("name",name),
        ("class",clas),
        ("grade1",grade1),
        ("grade2",grade2),
        ("grade3",grade3)})
    d[sid] = dic

def update_grades(d, sid):
    d[sid]['grade1'] = input("Enter new grade 1:")
    d[sid]['grade2'] = input("Enter new grade 2:")
    d[sid]['grade3'] = input("Enter new grade 3:")
    print("Updated dictionary", d)

def calculate_average(d, sid):
    return int(d[sid]['grade1'] + d[sid]['grade2'] + d[sid]['grade3'])/3

def generate_top_students_report(d):
    topDict = {}
    for c in d.keys().get("class"):
        topDic[c] = 0.0
    
    for sid in d.keys():
        avg = calculate_average(d, sid)
        c = d[sid].get("class")
        if avg > topDict[c]:
            topDict[c] = avg;
    return topDict.keys(), topDict.values()

    
d = {}
add_student(d)
add_student(d)
print("Dictionary : ", d)
sid = input("Enter student id to update the grade:")
update_grades(d, sid)
avg = calculate_average(d, sid)
print("Average grade : ", avg)
print("Top students : ", generate_top_students_report(d))
