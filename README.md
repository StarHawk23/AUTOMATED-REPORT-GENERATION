# AUTOMATED-REPORT-GENERATION

COMPANY NAME: CODTECH IT SOLUTIONS

NAME: S. HARI HARAN SRIRAM

INTERN ID: CT04DF2500

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTHOSH

IN THIS TASK, I SUCCESSFULLY CREATED A COMPLETE REPORT GENERATION SYSTEM USING PYTHON THAT READS STUDENT DATA FROM A CSV FILE AND OUTPUTS IT INTO A STRUCTURED AND PROFESSIONALLY FORMATTED PDF FILE. THE GOAL OF THIS TASK WAS TO AUTOMATE THE GENERATION OF STUDENT PERFORMANCE REPORTS, MAKING IT EASIER TO READ, STORE, AND SHARE STRUCTURED ACADEMIC DATA. THIS TASK PROVIDED A PRACTICAL USE CASE FOR INTEGRATING FILE HANDLING WITH DOCUMENT GENERATION USING THE CSV AND FPDF MODULES IN PYTHON. I RAN THE ENTIRE TASK USING VISUAL STUDIO CODE (VS CODE) AS MY DEVELOPMENT ENVIRONMENT.

THE PROCESS STARTED BY CREATING A DATASET OF STUDENT DETAILS, INCLUDING NAME, ROLL NUMBER, AND MARKS. THIS DATA WAS STORED IN A LIST OF LISTS FORMAT IN PYTHON AND THEN WRITTEN INTO A FILE NAMED STUDENTS.CSV USING PYTHON’S BUILT-IN CSV MODULE. THIS FILE SERVED AS THE DATA SOURCE FOR THE PDF GENERATION SCRIPT.

THE CREATE_CSV.PY SCRIPT WAS RESPONSIBLE FOR GENERATING THE CSV FILE. IT USED THE CSV.WRITER() FUNCTION TO WRITE THE DATA ROW BY ROW INTO STUDENTS.CSV. THIS INCLUDED A HEADER ROW FOLLOWED BY DATA FOR EACH STUDENT, SUCH AS "SRIRAM", 101, 95, AND SO ON. RUNNING THIS SCRIPT IN VS CODE ENSURED THAT THE CSV FILE WAS SAVED IN THE PROJECT DIRECTORY, READY TO BE READ BY THE NEXT PHASE OF THE PROJECT.

NEXT, THE MAIN SCRIPT REPORT_GENERATOR_FPDF.PY WAS CREATED. THIS SCRIPT UTILIZED THE FPDF MODULE TO READ THE STUDENTS.CSV FILE AND CONVERT ITS CONTENTS INTO A NEAT TABULAR FORMAT INSIDE A PDF FILE TITLED STUDENT_MARKS_REPORT.PDF. THE FPDF LIBRARY WAS CHOSEN BECAUSE IT IS LIGHTWEIGHT, SIMPLE TO USE, AND WELL-SUITED FOR GENERATING BASIC STRUCTURED PDFS WITH TABLES, HEADERS, AND FOOTERS.

ONE OF THE KEY CHALLENGES FACED DURING THIS STAGE WAS HANDLING THE EPW ATTRIBUTE, WHICH IS NOT A BUILT-IN PROPERTY OF FPDF. INITIALLY, THE PROGRAM RAISED AN ATTRIBUTEERROR BECAUSE PDF.EPW WAS UNDEFINED. TO RESOLVE THIS, THE EFFECTIVE PAGE WIDTH (EPW) WAS MANUALLY CALCULATED USING THE FORMULA EPW = PDF.W - 2 * PDF.L_MARGIN. THIS ALLOWED THE SCRIPT TO DYNAMICALLY ADJUST COLUMN WIDTHS BASED ON THE NUMBER OF HEADERS, ENSURING THAT THE TABLE FIT NEATLY WITHIN THE PAGE MARGINS.

THE PDF GENERATION SCRIPT ALSO INCLUDED A CUSTOM HEADER AND FOOTER USING FPDF CLASS METHODS HEADER() AND FOOTER(). THE HEADER ADDED THE TITLE “STUDENT MARKS REPORT” IN BOLD AT THE TOP CENTER OF THE PAGE, WHILE THE FOOTER AUTOMATICALLY ADDED A PAGE NUMBER AT THE BOTTOM OF EVERY PAGE. THE DATA ROWS WERE DRAWN USING PDF.CELL() INSIDE A LOOP, FORMATTED WITH BORDERS AND ALIGNMENT TO GIVE THE OUTPUT A CLEAN AND PROFESSIONAL LOOK.

THE COMPLETE SCRIPT WAS RUN IN VISUAL STUDIO CODE (VS CODE), WHICH PROVIDED A SMOOTH DEVELOPMENT EXPERIENCE WITH FEATURES LIKE CODE HIGHLIGHTING, INTEGRATED TERMINAL, AND INSTANT ERROR FEEDBACK. THE TERMINAL INSIDE VS CODE WAS USED TO RUN BOTH THE CSV WRITER SCRIPT AND THE PDF GENERATOR SCRIPT WITHOUT NEEDING TO SWITCH TO AN EXTERNAL COMMAND PROMPT. THIS HELPED STREAMLINE DEVELOPMENT AND TESTING.

IN THE END, RUNNING THE SCRIPT GENERATED A PDF FILE NAMED STUDENT_MARKS_REPORT.PDF, WHICH CONTAINED A WELL-FORMATTED TABLE OF STUDENT NAMES, ROLL NUMBERS, AND MARKS. THE FINAL OUTPUT SERVES AS A PRINTABLE AND SHAREABLE DOCUMENT THAT COULD BE USED FOR ACADEMIC PURPOSES LIKE STUDENT REPORT CARDS, EXAM SUMMARIES, OR INTERNAL ASSESSMENTS.

OVERALL, THIS TASK WAS A GREAT EXAMPLE OF USING PYTHON FOR DATA PROCESSING AND DOCUMENT AUTOMATION. IT DEMONSTRATED HOW SIMPLE MODULES LIKE CSV AND FPDF CAN BE COMBINED TO SOLVE REAL-WORLD PROBLEMS EFFICIENTLY. THROUGH THIS TASK, I LEARNED NOT JUST HOW TO MANIPULATE FILES AND GENERATE PDFS, BUT ALSO HOW TO STRUCTURE CODE FOR READABILITY AND MAINTAINABILITY USING VS CODE.

#OUTPUT:
![Image](https://github.com/user-attachments/assets/755fd1d7-35a8-4034-b002-0745b9bf6fa8)
