import pandas as pd

file = "TIP_partners.xlsx"
data = pd.read_excel(file)

print(data.columns)

# Setup necessary data spots
# Specific columns

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
