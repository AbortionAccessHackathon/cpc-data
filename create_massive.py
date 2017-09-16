import pandas as pd
import json
import os
import numpy as np

eins = [name for name in os.listdir("./990") if os.path.isdir("./990/" + name)]

df_eins = []
df_name = []
df_dba = []
df_preparer = []
df_address = []
df_zipcode = []
df_phonenumber = []
df_website = []
df_tax_year = []
df_employees = []
df_total_volunteers = []
df_gross_sales = []
df_sales_cost = []
df_fees_professional_fundraising = []
df_contributions_fundraising_events = []
df_contributions_related_organizations = []
df_contributions_government_grants = []
df_contributions_all_other = []
df_contributions_total = []
df_contractor_fees = []
df_expenses_pre = []
df_expenses_post = []
df_land_equipment_cost = []
df_inventories_for_sale_pre = []
df_inventories_for_sale_post = []
df_forms_available_on_request = []
df_person_w_org_records = []
df_total_assets_pre = []
df_total_assets_post = []
df_total_liabilities_pre = []
df_total_liabilities_post = []
df_lobbying_costs_filing = []
df_lobbying_non_taxable = []

for ein in eins:
    print(ein)
    years = [name[4:8] for name in os.listdir("990/" + ein)]
    for year in years:
        with open('990/' + ein + '/990_' + year + '.json') as data:
            current_json_file = json.load(data)
        try:
            df_eins.append(ein)
        except:
            df_eins.append(np.nan)
        try:
            df_name.append(current_json_file['Return']['ReturnHeader']['Filer']['Name']['BusinessNameLine1'])
        except:
            df_name.append(np.nan)
        try:
            df_preparer.append(current_json_file['Return']['ReturnHeader']['PreparerFirm']['PreparerFirmBusinessName']['BusinessNameLine1'])
        except:
            df_preparer.append(np.nan)
        try:
            df_address.append(current_json_file['Return']['ReturnHeader']['Filer']['USAddress']['AddressLine1'] + ", " + current_json_file['Return']
                              ['ReturnHeader']['Filer']['USAddress']['City'] + ", " + current_json_file['Return']['ReturnHeader']['Filer']['USAddress']['State'])
        except:
            df_address.append(np.nan)
        try:
            df_zipcode.append(current_json_file['Return']['ReturnHeader']['Filer']['USAddress']['ZIPCode'])
        except:
            df_zipcode.append(np.nan)

        try:
            df_phonenumber.append(current_json_file['Return']['ReturnHeader']['Filer']['Phone'])
        except:
            df_phonenumber.append(np.nan)
        try:
            df_website.append(current_json_file['Return']['ReturnData']['IRS990']['WebSite'])
        except:
            df_website.append(np.nan)
        try:
            df_tax_year.append(current_json_file['Return']['ReturnHeader']['TaxYear'])
        except:
            df_tax_year.append(np.nan)
        try:
            df_employees.append(current_json_file['Return']['ReturnData']['IRS990']['TotalNbrEmployees'])
        except:
            df_employees.append(np.nan)
        try:
            df_total_volunteers.append(current_json_file['Return']['ReturnData']['IRS990']['TotalNbrVolunteers'])
        except:
            df_total_volunteers.append(np.nan)
        try:
            df_fees_professional_fundraising.append(current_json_file['Return']['ReturnData']['IRS990']['ProfessionalFundraising'])
        except:
            df_fees_professional_fundraising.append(np.nan)
        try:
            df_contributions_fundraising_events.append(current_json_file['Return']['ReturnData']['IRS990']['CntrbtnsRprtdFundraisingEvents'])
        except:
            df_contributions_fundraising_events.append(np.nan)
        try:
            df_contributions_related_organizations.append(current_json_file['Return']['ReturnData']['IRS990']['RelatedOrganizations'])
        except:
            df_contributions_related_organizations.append(np.nan)
        try:
            df_contributions_government_grants.append(current_json_file['Return']['ReturnData']['IRS990']['GovernmentGrants'])
        except:
            df_contributions_government_grants.append(np.nan)
        try:
            df_contributions_all_other.append(current_json_file['Return']['ReturnData']['IRS990']['AllOtherContributions'])
        except:
            df_contributions_all_other.append(np.nan)
        try:
            df_contributions_total.append(current_json_file['Return']['ReturnData']['IRS990']['TotalContributions'])
        except:
            df_contributions_total.append(np.nan)
        try:
            df_contractor_fees.append(sum([int(a['Compensation']) for a in current_json_file['Return']['ReturnData']['IRS990']['ContractorCompensation']]))
        except:
            df_contractor_fees.append(np.nan)
        try:
            df_expenses_pre.append(current_json_file['Return']['ReturnData']['IRS990']['TotalExpensesPriorYear'])
        except:
            df_expenses_pre.append(np.nan)
        try:
            df_expenses_post.append(current_json_file['Return']['ReturnData']['IRS990']['TotalExpensesCurrentYear'])
        except:
            df_expenses_post.append(np.nan)
        try:
            df_land_equipment_cost.append(current_json_file['Return']['ReturnData']['IRS990']['LandBuildingsEquipmentBasis'])
        except:
            df_land_equipment_cost.append(np.nan)
        try:
            df_inventories_for_sale_pre.append(current_json_file['Return']['ReturnData']['IRS990']['InventoriesForSaleOrUse']['BOY'])
        except:
            df_inventories_for_sale_pre.append(np.nan)
        try:
            df_inventories_for_sale_post.append(current_json_file['Return']['ReturnData']['IRS990']['InventoriesForSaleOrUse']['EOY'])
        except:
            df_inventories_for_sale_post.append(np.nan)
        try:
            df_forms_available_on_request.append(current_json_file['Return']['ReturnData']['IRS990ScheduleH']['Form990ScheduleHPartVSectionB']['AvailableOnRequest'])
        except:
            df_forms_available_on_request.append(np.nan)
        try:
            df_person_w_org_records.append(current_json_file['Return']['ReturnData']['IRS990']['TheBooksAreInCareOf']['NameBusiness']['BusinessNameLine1'])
        except:
            df_person_w_org_records.append(np.nan)
        try:
            df_total_assets_pre.append(current_json_file['Return']['ReturnData']['IRS990']['TotalAssetsBOY'])
        except:
            df_total_assets_pre.append(np.nan)
        try:
            df_total_assets_post.append(current_json_file['Return']['ReturnData']['IRS990']['TotalAssetsEOY'])
        except:
            df_total_assets_post.append(np.nan)
        try:
            df_total_liabilities_pre.append(current_json_file['Return']['ReturnData']['IRS990']['TotalLiabilitiesBOY'])
        except:
            df_total_liabilities_pre.append(np.nan)
        try:
            df_total_liabilities_post.append(current_json_file['Return']['ReturnData']['IRS990']['TotalLiabilitiesEOY'])
        except:
            df_total_liabilities_post.append(np.nan)
        try:
            df_lobbying_costs_filing.append(current_json_file['Return']['ReturnData']['IRS990ScheduleC']['TotalLobbyingExpenditures2']['CurrentYear'])
        except:
            df_lobbying_costs_filing.append(np.nan)
        try:
            df_lobbying_non_taxable.append(current_json_file['Return']['ReturnData']['IRS990ScheduleC']['LobbyingNontaxableAmount2']['CurrentYear'])
        except:
            df_lobbying_non_taxable.append(np.nan)


final = pd.DataFrame(data={'eins': df_eins, 'name': df_name, 'preparer': df_preparer, 'address': df_address, 'zipcode': df_zipcode, 'phonenumber': df_phonenumber, 'website': df_website, 'tax_year': df_tax_year, 'employees': df_employees, 'total_volunteers': df_total_volunteers, 'fees_professional_fundraising': df_fees_professional_fundraising, 'contributions_fundraising_events': df_contributions_fundraising_events, 'contributions_related_organizations': df_contributions_related_organizations, 'contributions_government_grants': df_contributions_government_grants, 'contributions_all_other': df_contributions_all_other, 'contributions_total': df_contributions_total,
                           'contractor_fees': df_contractor_fees, 'expenses_pre': df_expenses_pre, 'expenses_post': df_expenses_post, 'land_equipment_cost': df_land_equipment_cost, 'inventories_for_sale_pre': df_inventories_for_sale_pre, 'inventories_for_sale_post': df_inventories_for_sale_post, 'forms_available_on_request': df_forms_available_on_request, 'person_w_org_records': df_person_w_org_records, 'total_assets_pre': df_total_assets_pre, 'total_assets_post': df_total_assets_post, 'total_liabilities_pre': df_total_liabilities_pre, 'total_liabilities_post': df_total_liabilities_post, 'lobbying_costs_filing': df_lobbying_costs_filing, 'lobbying_non_taxable': df_lobbying_non_taxable})

final.set_index('EIN', inplace=True)
writer = pd.ExcelWriter('output.xlsx')
final.to_excel(writer,'cleaned')
writer.save()
