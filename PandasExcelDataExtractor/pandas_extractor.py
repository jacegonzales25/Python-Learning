import pandas as pd

file = "TIP_partners.xlsx"
data = pd.read_excel(file)

# print(data.columns)

# Setup necessary data spots
# Specific columns for read

timestamp_column = data["Timestamp"]
email_address = data["Email Address"]
company_name = data["Company Name"]
company_address = data["Company Address"]
contact_person = data["Contact Person"]
designation = data["Designation"]
office_contact_number = data["Office Contact Number"]
resume_email_address = data["Resume Email Address"]
categories = data["Categories/Specializations of Company"]
programs = data["Programs/Course Requested"]
no_of_interns = data["No. of Intern/OJT Student Needed"]
allowance = data["Do you provide Allowance or Stipend?"]

# Timestamp into query()
converted_timestamp = pd.to_datetime(timestamp_column)
# print(converted_timestamp)

filtered_timestamp_column = data[converted_timestamp.dt.year == 2023]
# For convention
year_2023_data = data[data["Timestamp"].dt.year == 2023]
# print(filtered_timestamp_column)

# Filter companies having Computer Science or Information Technology
filtered_programs = data[programs.str.contains("Computer Science|Information Technology")]
# print(filtered_programs)

cs_it_data = year_2023_data[year_2023_data['Programs/Course Requested'].str.contains('Computer Science|Information Technology')]


# Adding the dataframe with filter
cs_it_data["Email"] = data["Email Address"]
cs_it_data["Company Name"] = data["Company Name"]
cs_it_data["Company Address"] = data["Company Address"]
cs_it_data["Contact Person"] = data["Contact Person"]
cs_it_data["Designation"] = data["Designation"]
cs_it_data["Office Contact Number"] = data["Office Contact Number"]
cs_it_data["Resume Email Address"] = data["Resume Email Address"]
cs_it_data["Categories/Specializations of Company"] = data["Categories/Specializations of Company"]
cs_it_data["No. of Intern/OJT Student Needed"] = data["No. of Intern/OJT Student Needed"]
cs_it_data["Do you provide Allowance or Stipend?"] = data["Do you provide Allowance or Stipend?"]

cs_it_data.to_excel('output.xlsx', index=False)

