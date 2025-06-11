import csv
from fpdf import FPDF

# Read data from CSV
data = []
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    headers = next(reader)  # ["Name", "Roll No", "Marks"]
    for row in reader:
        data.append(row)

# Define PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Student Marks Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

# Create PDF
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Calculate effective page width and column width
line_height = pdf.font_size * 2
epw = pdf.w - 2 * pdf.l_margin  # Effective page width
col_width = epw / len(headers)  # Equal width for each column

# Add table headers
pdf.set_fill_color(200, 220, 255)
for header in headers:
    pdf.cell(col_width, line_height, header, border=1, align="C", fill=True)
pdf.ln(line_height)

# Add data rows
for row in data:
    for item in row:
        pdf.cell(col_width, line_height, str(item), border=1, align="C")
    pdf.ln(line_height)

# Save PDF
pdf.output("student_marks_report.pdf")
print("✅ student_marks_report.pdf generated successfully!")
