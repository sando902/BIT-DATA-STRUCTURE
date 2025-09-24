# Integers: CVs collected from different booths

cv_counts = [42, 35, 50, 28, 63, 45]  # CVs from various booths

total_cvs = sum(cv_counts)
average_cvs = total_cvs / len(cv_counts)
min_cvs = min(cv_counts)
max_cvs = max(cv_counts)

# Strings: CV Collection Summary Report

report = (
    f"Job Fair CV Tally Summary:\n"
    f"Total CVs Collected: {total_cvs}\n"
    f"Average CVs per Booth: {average_cvs:.2f}\n"
    f"Min CVs at a Booth: {min_cvs}\n"
    f"Max CVs at a Booth: {max_cvs}"
)
print(report)

# Booleans: Threshold Check

threshold = 40
if average_cvs > threshold and max_cvs > 60:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# Lists: Managing Booth Names

booth_names = ["Booth A", "Booth B", "Booth C", "Booth D", "Booth E", "Booth F"]
print("\nOriginal Booth List:", booth_names)

# Add a new booth
booth_names.append("Booth G")

# Remove any booth with name ending in 'D'
booth_names_filtered = [booth for booth in booth_names if not booth.endswith("D")]

# Sort updated booth names
booth_names_filtered.sort()
print("Updated and Sorted Booth List:", booth_names_filtered)

# Arrays: Fixed Subset of CV Counts

import array

cv_array = array.array('i', cv_counts[:4])  # First 4 booth CV counts
array_sum = sum(cv_array)
list_sum = sum(cv_counts[:4])

print(f"\nSum of CVs using array: {array_sum}")
print(f"Sum of CVs using list: {list_sum}")

# Dictionaries: Booth Record Management

cv_records = [
    {'id': 1, 'name': 'Booth A', 'value': 42},
    {'id': 2, 'name': 'Booth B', 'value': 35},
    {'id': 3, 'name': 'Booth C', 'value': 50},
    {'id': 4, 'name': 'Booth D', 'value': 28}
]

# Update Booth C's CV count
for record in cv_records:
    if record['name'] == 'Booth C':
        record['value'] = 55

# Delete Booth D
cv_records = [record for record in cv_records if record['name'] != 'Booth D']

# Calculate total CVs from updated records
total_cv_records = sum(record['value'] for record in cv_records)

print("\nUpdated CV Records:")
for record in cv_records:
    print(record)

print(f"Total CVs from Updated Records: {total_cv_records}")