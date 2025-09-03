import csv

# rows = []

# with open("employers.csv", newline="\n") as file:
#     read = csv.reader(file)
#     header = next(read)
#     for row in read:
#         rows.append(row)
#     print(header)
#     print(rows)

# del rows

# header = ["name", "Age"]
# data = [["Alex", 25],["Brad", 30], ["Joey", 18]]

# with open("people.csv", "w", newline="")as f:
#     write = csv.writer(f)
#     write.writerow(header)
#     write.writerows(data)

# del header
# del data

# with open("employers.csv", "r") as f:
#     read = csv.DictReader(f)
#     for row in read:
#         print(row)

# header = ["Name", "Age"]
# data = [["Alex", 25],["Brad", 30], ["Joey", 18]]

# with open("student.csv", "w", newline="") as f:
#     write = csv.DictWriter(f, fieldnames=header)
#     write.writeheader()
#     for row in data:
#         write.writerow(dict(zip(header,row)))

# import collections

# with open("employers.csv", )
#     employee = namedtuple("Employee", next(reader), rename=True)

# Read the following CSV about Australia states and territories
# Add a new header "Capital" and add the capital city for each state/territory
# write to the same CSV file
# Extra fun: calculate the total population of Australia



# census = []

# with open("census.csv", "r") as f:
#     read = csv.DictReader(f)
#     for row in read:
#         census.append(row)


# capitals = ["Melbourne", "Sydney", "Adelaide", "Perth", "Hobart", "Brisbane", "Canberra", "Darwin"]

# pop = 0

# for i, state in enumerate(census):
#     state["Capital"] = capitals[i]
#     pop += int(state['Population'])

# with open("census.csv", 'w', newline="") as f:
#     write = csv.DictWriter(f, fieldnames=census[0].keys())
#     write.writeheader()
#     for state in census:
#         write.writerow(state)

# print(pop)



# Load a CSV file (e.g., student grades (provided), or if you can find another csv file you can use that!)
# Clean and summarise the data
# e.g. avg grade
# highest/lowest grade 
# any more you'd like
# Output insights to a new file

grades = []

with open("grades.csv", "r", newline="\n") as f:
    read = csv.DictReader(f)
    for row in read:
        grades.append(row)

print(grades)

marks = [int(x["Grade"]) for x in grades]
print(marks)
avg_mark = sum(marks)/len(marks)
max_mark = max(marks)
min_mark = min(marks)
med_mark = (\
    (marks[len(marks)//2-1]+marks[len(marks)//2])/2, \
    marks[len(marks)//2]\
    )[len(marks)&1]

print("avg", avg_mark, "\nmedian", med_mark, "\nmax", max_mark, "\nmin", min_mark)

with open("agg.csv", "w") as f:
    f.write(f"avg: {avg_mark}\nmed: {med_mark}\nmax {max_mark}\nmin {min_mark}")


