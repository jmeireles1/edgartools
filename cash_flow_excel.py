from edgar import * 
from edgar import set_identity, Company 
from rich.console import Console
import cash_flow_dictionary as cash_flow_dictionary
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

def cashflow_excel(balance_sheet, year):
    
    
    print("************************************************************")
    print("*************************** NEW YEAR ***********************")
    print("************************************************************")
    print(year)
    df = balance_sheet.get_dataframe()
    df.index = df.index.str.lower()

    #print(df.index)
    
    print("######################### depreciation_and_amortization #########################")
    depreciation_and_amortization, found = find_label(df, cash_flow_dictionary.depreciation_and_amortization, year)
    found and warn_is_null_beep("depreciation_and_amortization", depreciation_and_amortization)

    print("######################### stock_based_compensation #########################")
    stock_based_compensation, found = find_label(df, cash_flow_dictionary.stock_based_compensation, year)
    found and warn_is_null_beep("stock_based_compensation", stock_based_compensation)    

    print("######################### cash_from_operations #########################")
    cash_from_operations, found = find_label(df, cash_flow_dictionary.cash_from_operations, year)
    found and warn_is_null_beep("cash_from_operations", cash_from_operations)

    print("######################### Capital Expenditure #########################")
    capital_expenditure, found = find_label(df, cash_flow_dictionary.capital_expenditure, year)
    found and warn_is_null_beep("capital_expenditure", capital_expenditure)

    print("######################### Cash Acquisitions #########################")
    cash_acquisitions, found = find_label(df, cash_flow_dictionary.cash_acquisitions, year)
    found and warn_is_null_beep("cash_acquisitions", cash_acquisitions)

    print("######################### Debt #########################")
    short_term_debt_new, found = find_label(df, cash_flow_dictionary.short_term_debt_new, year)
    found and warn_is_null_beep("short_term_debt_new", short_term_debt_new)
    
    short_term_debt_payments, found = find_label(df, cash_flow_dictionary.short_term_debt_payments, year)
    found and warn_is_null_beep("short_term_debt_payments", short_term_debt_payments)
    
    long_term_debt_new, found = find_label(df, cash_flow_dictionary.long_term_debt_new, year)
    found and warn_is_null_beep("long_term_debt_new", long_term_debt_new)

    long_term_debt_payments, found = find_label(df, cash_flow_dictionary.long_term_debt_payments, year)
    found and warn_is_null_beep("long_term_debt_payments", long_term_debt_payments)

    print("#########################  Interest Paid #########################")
    interest_paid, found = find_label(df, cash_flow_dictionary.interest_paid, year)
    found and warn_is_null_beep("wages", interest_paid)

    print("#########################  Issuance of Common Stock #########################")
    issuance_of_common_stock, found = find_label(df, cash_flow_dictionary.issuance_of_common_stock, year)
    found and warn_is_null_beep("issuance_of_common_stock", issuance_of_common_stock)

    print("#########################  Repurchase of Common Stock #########################")
    repurchase_of_common_stock, found = find_label(df, cash_flow_dictionary.repurchase_of_common_stock, year)
    found and warn_is_null_beep("issuance_of_common_stock", repurchase_of_common_stock)

    print("#########################  Common Dividends Paid #########################")
    common_dividends_paid, found = find_label(df, cash_flow_dictionary.common_dividends_paid, year)
    found and warn_is_null_beep("issuance_of_common_stock", common_dividends_paid)

    print("#########################  Inventory #########################")
    inventory, found = find_label(df, cash_flow_dictionary.inventory, year)
    found and warn_is_null_beep("Inventory", inventory)

    print("#########################  Accounts Receivable #########################")
    accounts_receivable, found = find_label(df, cash_flow_dictionary.accounts_receivable, year)
    found and warn_is_null_beep("accounts_receivable", accounts_receivable)

    print("#########################  Accounts Payable #########################")
    accounts_payable, found = find_label(df, cash_flow_dictionary.accounts_payable, year)
    found and warn_is_null_beep("accounts_payable", accounts_payable)

    print("#########################  Obligations #########################")
    obligations, found = find_label(df, cash_flow_dictionary.obligations, year)
    found and warn_is_null_beep("obligations", obligations)

    print("#########################  Wages #########################")
    wages, found = find_label(df, cash_flow_dictionary.wages, year)
    found and warn_is_null_beep("wages", wages)