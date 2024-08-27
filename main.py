from edgar import * 
from edgar import set_identity, Company 
from rich.console import Console
import os
from cash_flow_excel import cashflow_excel
from income_statement_excel import income_statement_excel


set_identity("tpostinhas@gmail.com") 
console = Console(record=True)
company_name = 'ZTS'
initial_year = 2023

def save_file(folder_path, document_type, year):

    html_content = console.export_html() 
    file_name = str(year) + "_" + document_type + '_' + company_name + '.html'
    html_path = os.path.join(folder_path, file_name)

    with open(html_path, 'w', encoding='utf-8') as html_file: 
        html_file.write(html_content) 


current_directory = os.getcwd()
company = Company(company_name) 

company_root_folder = os.path.join(current_directory, company_name)
balance_sheet_folder = os.path.join(company_root_folder, "balance_sheet")
cash_flow_folder = os.path.join(company_root_folder, "cash_flow")
income_statement_folder = os.path.join(company_root_folder, "income_statement")

if not os.path.exists(company_root_folder):
    os.makedirs(company_root_folder)

if not os.path.exists(balance_sheet_folder):
    os.makedirs(balance_sheet_folder)

if not os.path.exists(cash_flow_folder):
    os.makedirs(cash_flow_folder)

if not os.path.exists(income_statement_folder):
    os.makedirs(income_statement_folder)

tenks = company.get_filings(form="10-K").latest(10)

for tenk in tenks:
    financials = tenk.obj().financials

    #balance_sheet = financials.get_balance_sheet()
    #console.print(balance_sheet) 
    #save_file(balance_sheet_folder, 'balance_sheet', initial_year)
    #cashflow_excel(balance_sheet)

    #cash_flow = financials.get_cash_flow_statement()
    #console.print(cash_flow)
    #save_file(cash_flow_folder, 'cash_flow', initial_year)
    #cashflow_excel(cash_flow, initial_year)

    income_statement = financials.get_income_statement()
    console.print(income_statement) 
    save_file(income_statement_folder, 'income_statement', initial_year)
    income_statement_excel(income_statement, initial_year)

    initial_year = initial_year - 1 

print("Done!")




# # Iterate through each concept
# concepts = balance_sheet.concepts
# labels = balance_sheet.labels

# # Create a mapping between concepts and labels
# concept_label_map = {}
# for concept, label in zip(concepts, labels):
#     concept_label_map[concept] = label

# data_array = []

# for concept, label in concept_label_map.items():

#         if "Abstract" in concept:
#              #print(f"Absctract Concept")
#              data_array.append((label, concept, "Abstract"))
            
#         else:
#             #try:
#                 # Retrieve the concept object
#                 #print(concept)
#                 value = balance_sheet.get_concept(concept).value.get('2023', '000000000000')
#                 data_array.append((label, concept, value))

#             #except Exception as e:
#                 # Handle any exceptions that might occur and print an error message
#             #    print(f"Error retrieving concept {concept} and {label}")
#             #    print(e)


# print(data_array)