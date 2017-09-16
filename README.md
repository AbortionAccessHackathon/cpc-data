# cpc-data
link to data dictionary
https://github.com/lecy/Open-Data-for-Nonprofit-Research/blob/master/Build_IRS990_E-Filer_Datasets/Data%20Dictionary.csv

Things To Look For:
* Some of the clinics own property -- how is that used?  If the property was bought with non-profit funding, that's a large purchase that did not go towards providing health services (the non-profit's stated purpose)
* Look for high non-cash benefit line amount, compared to other spending.  
* Look at board members
* Look at ten highest-paid employees, if present
* EIN - clinic website -- make the attachment -- companies that provide products might not like their products being used on those websites.
* Do they have board-licensed doctors?
* Identify state-funded orgs.
* Identify sonogram provision.
* Identify where state funded orgs provide more to advertising than to services (another type of large purchase that runs counter to stated purpose).
* Identify where entities operate without proper medical licensure.
* Identify where entities operate without proper 990 filing/nonprofit status.
* Groups that have not filed in a while, are no longer registered -- should not be accepting donations.
* Go to IRS website.  there's a list of groups that have not filed in 3 years
* 14 states with public funding to CPCs: Georgia (under TANF), Indiana, Kansas, Louisiana, Michigan, Minnesota, Missouri, New Mexico, North Carolina, North Dakota, Ohio, Pennsylvania, Texas, and Wisconsin.

Scripts:
*get_990_urls.py relies on data/incomplete_ein_list.csv -- bug wcrest for it
