from edgar import * 
from edgar import set_identity, Company 
from rich.console import Console
import income_statement_dictionary as income_statement_dictionary
import winsound

# Frequency of the beep (Hz) and duration (ms)
frequency = 1000  # Frequency in Hertz
duration = 1000  # Duration in milliseconds


def find_label(df, array_search, year):
    year = str(year)  # Convert year to string once, outside the loop
    
    for label in array_search:
        try:
            df_filtered = df.loc[label.lower(), year]
        except KeyError:
            continue  # Skip to the next label if KeyError is encountered
        
        if isinstance(df_filtered, str):
            return df_filtered, True
        return df_filtered.values[0], True
    
    return None, None  # Return None, None if no match is found


def warn_is_null_beep(label, value):
    if value != 0 and value is None:
       winsound.Beep(frequency, duration)
    else:
        print(label +": "+ value)

def income_statement_excel(income_statement, year):
    
    
    print("************************************************************")
    print("*************************** NEW YEAR ***********************")
    print("************************************************************")
    print(year)
    df = income_statement.get_dataframe()
    df.index = df.index.str.lower()

    #print(df.index)
    
    print("######################### Revenues #########################")
    revenues, found = find_label(df, income_statement_dictionary.revenues, year)
    found and warn_is_null_beep("revenues", revenues)

    print("######################### Cost of Sales #########################")
    cost_of_sales, found = find_label(df, income_statement_dictionary.cost_of_sales, year)
    found and warn_is_null_beep("cost_of_sales", cost_of_sales)

    print("######################### Gross Profit #########################")
    gross_profit, found = find_label(df, income_statement_dictionary.gross_profit, year)
    found and warn_is_null_beep("gross_profit", gross_profit)

    print("######################### Technology and infrastructure #########################")
    technology_and_infrastructure, found = find_label(df, income_statement_dictionary.technology_and_infrastructure, year)
    found and warn_is_null_beep("technology_and_infrastructure", technology_and_infrastructure)


    print("######################### Sales and marketing #########################")
    sales_and_marketing, found = find_label(df, income_statement_dictionary.sales_and_marketing, year)
    found and warn_is_null_beep("sales_and_marketing", sales_and_marketing)

    print("######################### Research_and_development #########################")
    Research_and_development, found = find_label(df, income_statement_dictionary.Research_and_development, year)
    found and warn_is_null_beep("Research_and_development", Research_and_development)

    print("######################### Selling, general and administrative #########################")
    selling_general, found = find_label(df, income_statement_dictionary.selling_general, year)
    found and warn_is_null_beep("selling_general", selling_general)

    print("######################### Operating Expenses #########################")
    operating_expenses, found = find_label(df, income_statement_dictionary.operating_expenses, year)
    found and warn_is_null_beep("operating_expenses", operating_expenses)

    print("######################### Operating income #########################")
    operating_income, found = find_label(df, income_statement_dictionary.operating_income, year)
    found and warn_is_null_beep("operating_income", operating_income)
    
    print("######################### Nonoperating Expenses #########################")
    nonperating_income_expense, found = find_label(df, income_statement_dictionary.nonperating_income_expense, year)
    found and warn_is_null_beep("nonperating_income_expense", nonperating_income_expense)

    print("######################### Interest Expense #########################")
    interest_expense, found = find_label(df, income_statement_dictionary.interest_expense, year)
    found and warn_is_null_beep("interest_expense", interest_expense)

    print("######################### Earnings Per Share Basic #########################")
    earnings_per_share, found = find_label(df, income_statement_dictionary.earnings_per_share, year)
    found and warn_is_null_beep("earnings_per_share", earnings_per_share)

    print("######################### Earnings Per Share Diluted #########################")
    earnings_per_share_diluted, found = find_label(df, income_statement_dictionary.earnings_per_share_diluted, year)
    found and warn_is_null_beep("operating_expenses", earnings_per_share_diluted)

    print("#########################  Weighted Average Diluted Shares Outstanding #########################")
    weighted_average_diluted_shares_outstanding, found = find_label(df, income_statement_dictionary.weighted_average_diluted_shares_outstanding, year)
    found and warn_is_null_beep("weighted_average_diluted_shares_outstanding", weighted_average_diluted_shares_outstanding)