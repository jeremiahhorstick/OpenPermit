# US state residential code books: adoption by state (DRAFT, verified 2026-10-03)

> Research reference only. Not legal advice. Confirm with the adopting agency. No code text is reproduced: only titles, editions, dates, section numbers and links.

Status: **DRAFT** research layer. Facts were checked against official pages fetched on 2026-10-03 and are not re-verified since; adoptions change, so confirm with the adopting agency. To finish: re-verify the category D states and the fields still marked UNVERIFIED (listed below), and refresh dates that have since passed.

## Summary

52 jurisdictions: 50 states, DC and Puerto Rico. Map categories:

- **A**: Statewide code; free state-published code book or amendment document: **24** (AL, CT, DC, GA, HI, ID, IN, KY, LA, ME, MD, MA, NJ, NM, OH, OK, OR, PA, RI, SC, UT, VA, WA, WI)
- **B**: Statewide code; state points to ICC Digital Codes / no-cost viewing (no free state download found): **4** (AR, CA, MN, NY)
- **C**: Local option / home rule (no mandatory statewide residential code): **16** (AK, AZ, CO, DE, IL, IA, KS, MS, MO, NE, NV, ND, SD, TX, VT, WV)
- **D**: Unverified (scope or book availability not confirmed): **8** (FL, MI, MT, NH, NC, PR, TN, WY)

How to read the categories:
- **Texas** is C. State law sets the IRC as the minimum municipal residential code (Tex. Loc. Gov't Code 214.212), but there is no state code agency or state book. Cities adopt and enforce.
- **Iowa, North Dakota, Nebraska, West Virginia and Mississippi** are C. Each has a state code, but it applies only where localities adopt it, or localities may opt out.
- **Tennessee** is statewide with local opt-out.
- **Category D** means a statewide adoption was confirmed but a free state book was not checked: Florida, Michigan, Montana, New Hampshire, North Carolina and Tennessee. Wyoming and Puerto Rico are D because their residential scope itself was not confirmed.

Notable findings (each is from a fetched official page; see `source_urls`):
- **Recent or upcoming changes:**
  - Montana: 2024 IRC effective Sept 26, 2026.
  - Oklahoma: 2024 IRC permanent rule effective Sept 14, 2026.
  - Oregon: 2026 ORSC effective Oct 1, 2026, with a six-month phase-in.
  - New Hampshire: 2024 IRC effective July 1, 2026, with concurrency through Dec 31, 2026.
  - Georgia: 2024 IRC amendments effective Jan 1, 2026.
  - Pennsylvania: 2021 IRC regulations effective Jan 1, 2026.
  - California: 2025 CRC effective Jan 1, 2026.
  - New York: 2025 RCNYS effective Dec 31, 2025.
  - Iowa: 2024 IRC effective Sept 10, 2025.
  - Washington (2024 codes) and South Carolina and Louisiana (next editions) take effect May 3, 2027, Jan 1, 2027 and Jan 1, 2027 respectively.
- **Michigan:** a July 7, 2025 court order kept the 2015-based residential rules in effect.
- **North Carolina:** the 2018 NC codes remain current while the 2024 code is delayed.
- **Kentucky:** the current code is the 2018 Kentucky Residential Code, still based on the 2015 IRC.
- **Full or near-full free state books:**
  - Ohio: Residential Code of Ohio rules, a 19.9 MB PDF.
  - Kentucky: 2018 KRC.
  - Wisconsin: Uniform Dwelling Code, a state-written code.
  - Hawaii, Connecticut, Massachusetts, West Virginia, Louisiana, New Mexico and Virginia: amendment documents.
- **States telling readers to use ICC's free viewer:** New York (DOS), Indiana (DHS) and Minnesota (DLI). California says the code is viewable at no cost through several channels, including depository libraries.
- **Copyright notices are mixed.**
  - Maryland's COMAR site says it is published under a "license with copyright held by the State of Maryland".
  - Rhode Island and Oklahoma state that the IRC text is ICC copyright.
  - The NJ code PDF carries a © notice from the NJ Office of Administrative Law.
  - No state source states that its code is public domain.

## Method

1. **Collection.** Official state agency, legislature and administrative-code pages were fetched with plain HTTP GET. Pages that returned 403 or rendered only through JavaScript (NY, NH, MI, FL, TN, MT, VT) were read with a web-fetch tool. Utah's server sends an incomplete TLS chain, so its statute PDF was fetched with certificate checks off. Fetched pages, hashes and the matched evidence are kept by the maintainer outside this repository; only the source URLs are published here.
2. **Evidence check.** Every fact carries a (URL, exact quote) pair. A build step looks for the quote in the fetched text and marks any field without a match `[UNVERIFIED]`. Fields with no evidence pair are also marked UNVERIFIED. The `evidence_checked` column counts the pairs that matched.
3. **ICC Digital Codes.** State page URLs (`https://codes.iccsafe.org/codes/united-states/<state>`) come from ICC's public US index page. **The state pages were not scraped**, as instructed. "Free read-only" is filled in only where the state's own page says the code can be viewed free. Everything else is "UNVERIFIED (ICC pages not scraped; link only)". ICC lists no territory pages, so PR has none.
4. **Licence classification.** This is based only on the notice quoted from the source: "state copyright (notice on state source)", "ICC copyright (model code text)" or "unclear (no copyright notice seen)". State works are **not** assumed to be public domain.
5. **No code books in this repository.** State code documents are linked by URL only. No state or model code text, PDF or extract is committed.

Files: [`research/data/us-state-codebooks-DRAFT.csv`](../research/data/us-state-codebooks-DRAFT.csv) and [`.json`](../research/data/us-state-codebooks-DRAFT.json) (one row per state, 24 columns), and [`research/maps/us-state-codebooks-DRAFT.html`](../research/maps/us-state-codebooks-DRAFT.html), a self-contained offline map (click a state; no external requests).

Licence: the data files and the map are dedicated CC0 1.0 (see `LICENSE-SPEC.md`); this document is CC BY-SA 4.0. The facts describe third-party adoptions and grant no right to any code text.

## Table

| ST | Cat | Scope | Residential code | Effective | State book (free?) | Admin citation | Licence |
|---|---|---|---|---|---|---|---|
| AL | A | statewide | 2015 IRC as modified by the Alabama Energy and Residential Codes Board | UNVERIFIED | yes [link](https://admincode.legislature.state.al.us/api/rule/305-2-4-.09) | Ala. Admin. Code r. 305-2-4-.09 [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| AK | C | local option | No state residential code (detached 1-3 family dwellings exempt) | n/a | yes [link](https://dps.alaska.gov/wp-content/uploads/2026/05/13-AAC-50-to-13-AAC-55-Fire-Prevention_effective-10-28-2022.pdf) | 13 AAC 50.020 [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| AZ | C | local option | None statewide | n/a | n/a | A.R.S. § 11-861 (county building codes) [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| AR | B | statewide | Arkansas Fire Prevention Code 2021, Volume III Residential | January 1, 2023 | ICC viewer (linked by DPS; free status not checked) [UNVERIFIED] | UNVERIFIED | state copyright (notice on state source) |
| CA | B | statewide | 2025 California Residential Code, Cal. Code Regs. Title 24, Part 2.5 | January 1, 2026 | no state download; viewable at no cost per CBSC [UNVERIFIED] | Cal. Code Regs., Title 24, Part 2.5 [UNVERIFIED] | state copyright (notice on state source) |
| CO | C | home rule | None statewide | n/a | n/a | UNVERIFIED | unclear (no copyright notice seen on the source) |
| CT | A | statewide | 2022 Connecticut State Building Code, incorporating the 2021 IRC with CT amendments [UNVERIFIED] | October 1, 2022 | yes [link](https://portal.ct.gov/das/-/media/das-beta/pdf/office-of-state-building-inspector/2022-csbc-final.pdf) | Conn. Gen. Stat. § 29-252 (adoption authority) | unclear (no copyright notice seen on the source) |
| DE | C | local option | None statewide (county codes) | n/a | n/a | 9 Del. C. ch. 25 (New Castle County Building Code) [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| DC | A | statewide | 2017 DC Residential Code: 2015 IRC as amended by 12-B DCMR | UNVERIFIED (DOB notes amendments after May 29, 2020 not shown in integrated codes) | yes [link](https://dob.dc.gov/page/dc-construction-codes) | 12-B DCMR (DC Residential Code Supplement) [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| FL | D | statewide | Florida Building Code, 8th Edition (2023) - Residential | December 31, 2023 | UNVERIFIED | Fla. Admin. Code R. 61G20-1.001 | unclear (no copyright notice seen on the source) |
| GA | A | statewide | 2024 IRC with Georgia amendments | January 1, 2026 | yes [link](https://dca.georgia.gov/document/document/irc-2026-amendment-packet-2024-edition/download) | UNVERIFIED | unclear (no copyright notice seen on the source) |
| HI | A | statewide | 2018 IRC as Hawaii State Residential Code | November 17, 2020 | yes [link](https://ags.hawaii.gov/wp-content/uploads/2021/09/2018StateResidentialCode_20201117rev1.pdf) | HRS §§ 107-24, 107-27, 107-28 (adoption) | unclear (no copyright notice seen on the source) |
| ID | A | statewide | 2018 IRC (Parts I, II, III, IX) with Idaho amendments | UNVERIFIED (rule sections dated 7-1-24) | yes [link](https://files.dfm.idaho.gov/dfm-admin-website/rules/current/24/243930.pdf) | IDAPA 24.39.30 [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| IL | C | local option | None statewide (local choice; state baseline from 1/1/2025) | n/a | n/a | 20 ILCS 3105/10.18 (UNVERIFIED: statute page not fetched) | unclear (no copyright notice seen on the source) |
| IN | A | statewide | 2020 Indiana Residential Code (675 IAC 14-4.4), based on the 2018 IRC [UNVERIFIED] | December 26, 2019 | yes (state amendments free per DHS) [link](https://www.in.gov/dhs/files/Adoption-and-Implementation-of-2020-Indiana-Residential-Code.pdf) | 675 IAC 14-4.4 | unclear (no copyright notice seen on the source) |
| IA | C | local option | 2024 IRC (661 IAC 301) | September 10, 2025 (ARC 9474C) | yes [link](https://www.legis.iowa.gov/docs/iac/chapter/10-15-2025.661.301.pdf) | 661 IAC ch. 301; Iowa Code § 103A.12 [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| KS | C | home rule | None statewide | n/a | n/a | K.S.A. 12-3301 et seq. | unclear (no copyright notice seen on the source) |
| KY | A | statewide | 2018 Kentucky Residential Code, Second Edition (based on 2015 IRC) | August 1, 2019 (mandatory) | yes [link](https://dhbc.ky.gov/Documents/2018KentuckyResidentialCode%20-%20FINAL_Clean.pdf) | 815 KAR 7:125 | unclear (no copyright notice seen on the source) |
| LA | A | statewide | 2021 IRC with Louisiana amendments | January 1, 2023 | yes [link](https://lsuccc.la/wp-content/uploads/2025/10/uniform_construction_codes_and_amendments_r1_effective_01-01-23.pdf) | LAC 17:I (formerly LAC 55:VI.Chapter 3) | state copyright (notice on state source) |
| ME | A | statewide | 2021 IRC (16-642 CMR ch. 5) | UNVERIFIED (90 days after approval per chapter text) | yes [link](https://www.maine.gov/dps/fmo/sites/maine.gov.dps.fmo/files/inline-files/642C005.pdf) | 16-642 CMR ch. 5 [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| MD | A | statewide | IRC (Maryland Building Performance Standards; edition 2021 UNVERIFIED on fetched text) [UNVERIFIED: evidence not matched] | UNVERIFIED | yes [link](https://regs.maryland.gov/us/md/exec/comar/09.12.51) | COMAR 09.12.51 | state copyright (notice on state source) |
| MA | A | statewide | 780 CMR 10th Edition, Residential (780 CMR 51.00, amendments to the 2021 IRC) [UNVERIFIED] | October 11, 2024 | yes [link](https://www.mass.gov/doc/10th-edition-residential-chapter-1-scope-and-application/download) | 780 CMR 51.00 [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| MI | D | statewide | Michigan Residential Code 2015 (2015 IRC basis) remains in effect | UNVERIFIED (2015 MRC original effective date) | UNVERIFIED | Construction Code - Part 5. Residential Code (Mich. Admin. Code; rule numbers UNVERIFIED) | unclear (no copyright notice seen on the source) |
| MN | B | statewide | 2020 Minnesota Residential Code (2018 IRC basis), Minn. R. ch. 1309 [UNVERIFIED] | March 31, 2020 | free online viewing per DLI [UNVERIFIED] | Minn. R. ch. 1309 | unclear (no copyright notice seen on the source) |
| MS | C | local option | UNVERIFIED | UNVERIFIED | UNVERIFIED | Senate Bill 2378 (2014) (codified citation UNVERIFIED) | state copyright (notice on state source) |
| MO | C | home rule | None statewide | n/a | n/a | n/a | unclear (no copyright notice seen on the source) |
| MT | D | statewide | 2024 IRC (as amended by ARM 24.301) | September 26, 2026 | UNVERIFIED | ARM Title 24, Chapter 301 | unclear (no copyright notice seen on the source) |
| NE | C | local option | IRC per Neb. Rev. Stat. 71-6403 (2018 edition UNVERIFIED in extracted text) | UNVERIFIED | yes [link](https://nebraskalegislature.gov/laws/statutes.php?statute=71-6403) | Neb. Rev. Stat. §§ 71-6403, 71-6406 | unclear (no copyright notice seen on the source) |
| NV | C | local option | None statewide | n/a | n/a | NRS 278.580 | unclear (no copyright notice seen on the source) |
| NH | D | statewide | 2024 IRC with New Hampshire amendments | July 1, 2026 | UNVERIFIED | RSA 155-A | unclear (no copyright notice seen on the source) |
| NJ | A | statewide | International Residential Code/2024 (one- and two-family dwelling subcode, N.J.A.C. 5:23-3.21) | UNVERIFIED (N.J.A.C. 5:23-3 shows amendments R.2026 d.086 effective August 17, 2026; not isolated to 3.21) | yes [link](https://www.nj.gov/dca/codes/codreg/pdf_regs/njac_5_23_3.pdf) | N.J.A.C. 5:23-3.21 | state copyright (notice on state source) |
| NM | A | statewide | 2021 New Mexico Residential Building Code (14.7.3 NMAC; 2021 IRC basis) [UNVERIFIED] | July 14, 2023 | yes [link](https://www.rld.nm.gov/wp-content/uploads/2024/09/14.7.3-NMRBC-Amendment-6.24.24-TKMR.pdf) | 14.7.3 NMAC | unclear (no copyright notice seen on the source) |
| NY | B | statewide | 2025 Residential Code of New York State (publication date July 2025) | December 31, 2025 | free on ICC per DOS [UNVERIFIED] | 19 NYCRR Parts 1219-1229 | unclear (no copyright notice seen on the source) |
| NC | D | statewide | 2018 North Carolina Residential Code | January 1, 2019 | UNVERIFIED | UNVERIFIED | unclear (no copyright notice seen on the source) |
| ND | C | local option | Updated ND State Building Code (I-code edition UNVERIFIED) | January 1, 2026 | yes [link](https://www.commerce.nd.gov/sites/www/files/documents/Community%20Services/Building%20Codes/2025%20BLDGcode%20amendment%20schedule.pdf) | N.D.C.C. ch. 54-21.3 | unclear (no copyright notice seen on the source) |
| OH | A | statewide | 2019 Residential Code of Ohio (updated to reflect the 2018 IRC) | July 1, 2019 | yes [link](https://dam.assets.ohio.gov/image/upload/com.ohio.gov/documents/bbst_ResidentialCodeofOhioEffectiveJuly1,2019.pdf) | OAC Chapter 4101:8 | unclear (no copyright notice seen on the source) |
| OK | A | statewide | 2024 IRC with Oklahoma amendments (permanent rule) | September 14, 2026 | yes [link](https://oklahoma.gov/content/dam/ok/en/oubcc/documents/rules/2026%2009%2014%20IRC%202024%20Permanent%20Rule.pdf) | OAC 748:20 (UNVERIFIED on fetched page) | ICC copyright (model code text; notice on state source) |
| OR | A | statewide | 2026 Oregon Residential Specialty Code (new); 2023 ORSC during phase-in | October 1, 2026 (six-month phase-in) | partial (errata/amendments free; integrated book via ICC) [link](https://www.oregon.gov/bcd/codes-stand/Documents/23orsc-errata.pdf) | OAR 918-480 (UNVERIFIED on fetched page) | unclear (no copyright notice seen on the source) |
| PA | A | statewide | International Residential Code of 2021 (34 Pa. Code § 403.21) | January 1, 2026 | yes [link](https://www.pacodeandbulletin.gov/Display/pacode?d=&file=%2Fsecure%2Fpacode%2Fdata%2F034%2Fchapter403%2Fs403.21.html) | 34 Pa. Code § 403.21 [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| PR | D | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | unclear (no copyright notice seen on the source) |
| RI | A | statewide | IRC 2021 as the Rhode Island One & Two-Family Dwelling Code (SBC-2) | UNVERIFIED | yes (amendments); IRC text on ICC [link](https://rules.sos.ri.gov/Regulations/Part/510-00-00-2) | 510-RICR-00-00-2 [UNVERIFIED] | ICC copyright (model code text; notice on state source) |
| SC | A | statewide | 2021 IRC with SC modifications (2021 South Carolina Residential Code) | January 1, 2023 | yes [link](https://llr.sc.gov/bcc/PDFfiles/2021-Code-Modifications.pdf) | UNVERIFIED | unclear (no copyright notice seen on the source) |
| SD | C | local option | None statewide | n/a | n/a | SDCL ch. 11-10 [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| TN | D | statewide | 2018 IRC with amendments | July 16, 2020 | UNVERIFIED | Tenn. Code Ann. § 68-120-101 (rule chapter UNVERIFIED) | unclear (no copyright notice seen on the source) |
| TX | C | local option | IRC statutory municipal minimum (edition as of May 1, 2012 - UNVERIFIED in extracted text); local adoption of later editions | UNVERIFIED (statute page not text-extractable) | n/a | Tex. Loc. Gov't Code § 214.212 | unclear (no copyright notice seen on the source) |
| UT | A | statewide | 2021 IRC (Utah Code § 15A-2-103) | UNVERIFIED (statute version shown is effective 7/1/2024) | yes [link](https://le.utah.gov/xcode/Title15A/Chapter2/C15A-2-S103_2024070120240501.pdf) | Utah Code § 15A-2-103; Title 15A ch. 3 | unclear (no copyright notice seen on the source) |
| VT | C | local option | No state residential building code listed (RBES energy standards only) | n/a (RBES revisions effective July 14, 2026) | n/a | UNVERIFIED | unclear (no copyright notice seen on the source) |
| VA | A | statewide | 2021 Virginia Residential Code (2021 IRC as amended by VCC 310.8) | January 18, 2024 | yes [link](https://www.dhcd.virginia.gov/sites/default/files/DocX/building-codes-regulations/archive-codes/2021/2021-virginia-construction-code.pdf) | 13VAC5-63 (USBC) | state copyright (notice on state source) |
| WA | A | statewide | 2021 IRC with Washington amendments (WAC 51-51) | March 15, 2024 | yes [link](https://apps.leg.wa.gov/wac/default.aspx?cite=51-51) | WAC 51-51 [UNVERIFIED] | state copyright (notice on state source) |
| WV | C | local option | 2018 IRC (87CSR4 4.1.h) | August 1, 2022 | yes [link](https://firemarshal.wv.gov/media/39311/download?inline=) | W. Va. Code R. § 87-4 [UNVERIFIED] | unclear (no copyright notice seen on the source) |
| WI | A | statewide | Uniform Dwelling Code, Wis. Admin. Code chs. SPS 320-325 (state-written) | UNVERIFIED (current register date) | yes [link](https://docs.legis.wisconsin.gov/document/administrativecode/ch.%20SPS%20320.pdf) | Wis. Admin. Code SPS 320-325 | unclear (no copyright notice seen on the source) |
| WY | D | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | UNVERIFIED | unclear (no copyright notice seen on the source) |

## Unverified items

- **States with category D:** FL (Florida), MI (Michigan), MT (Montana), NH (New Hampshire), NC (North Carolina), PR (Puerto Rico), TN (Tennessee), WY (Wyoming).
- **Fields still marked UNVERIFIED in other states:** see the CSV. The main ones are effective dates for AL, DC, ID, ME, MD, MI, NE, NJ, RI, TX, UT and WI, and admin citations for AR, CO, GA, NC and SC.
- **Free read-only status on ICC:** UNVERIFIED for every state except NY, IN, MN and CA, where the state's own page describes no-cost viewing.

## Attribution

The code information comes from these adopting agencies. Each is credited and linked:

- Alabama: Alabama Home Builders Licensure Board (residential code adoption authority since Act 2024-443); Alabama Division of Construction Management (state-jurisdiction buildings). https://dcm.alabama.gov/bldg_code.aspx
- Alaska: Alaska Department of Public Safety, Division of Fire and Life Safety. https://dps.alaska.gov/fire/plan-review/
- Arizona: No statewide residential code agency (county/municipal adoption). https://www.azleg.gov/ars/11/00861.htm
- Arkansas: Arkansas State Fire Marshal (Arkansas Department of Public Safety / ADEM). https://dps.arkansas.gov/emergency-management/adem/state-fire-marshals-office/helpful-links/
- California: California Building Standards Commission (DGS). https://www.dgs.ca.gov/bsc/codes
- Colorado: Colorado Energy Office / Dept. of Local Affairs (no statewide residential code). https://energyoffice.colorado.gov/climate-energy/energy-policy/building-energy-codes
- Connecticut: Department of Administrative Services, Office of the State Building Inspector. https://portal.ct.gov/das
- Delaware: County governments (no statewide residential building code agency found). https://delcode.delaware.gov/title9/c025/
- District of Columbia: DC Department of Buildings (DOB) / Construction Codes Coordinating Board. https://dob.dc.gov/node/1615636
- Florida: Florida Building Commission (DBPR). https://www.floridabuilding.org/c/default.aspx
- Georgia: Georgia Department of Community Affairs (DCA). https://dca.georgia.gov/
- Hawaii: State Building Code Council (Dept. of Accounting and General Services). https://ags.hawaii.gov/
- Idaho: Idaho Division of Occupational and Professional Licenses (DOPL), Building Code Board. https://dopl.idaho.gov/
- Illinois: Capital Development Board (CDB). https://cdb.illinois.gov/business/codes.html
- Indiana: Indiana Fire Prevention and Building Safety Commission (Dept. of Homeland Security). https://www.in.gov/dhs/
- Iowa: Iowa Department of Inspections, Appeals, and Licensing - State Building Code Bureau. https://www.legis.iowa.gov/docs/iac/chapter/10-15-2025.661.301.pdf
- Kansas: No statewide residential code agency (local adoption). https://kslegislature.gov/b2023_24/laws/012_000_0000_chapter/012_033_0000_article/012_033_0001_section/012_033_0001_k/
- Kentucky: Kentucky Department of Housing, Buildings and Construction (DHBC). https://dhbc.ky.gov/
- Louisiana: Louisiana State Uniform Construction Code Council (LSUCCC). https://lsuccc.la/
- Maine: Maine Technical Building Codes and Standards Board (Dept. of Public Safety, Fire Marshal - MUBEC). https://www.maine.gov/dps/fmo/
- Maryland: Maryland Department of Labor - Building Codes Administration. https://labor.maryland.gov/labor/build/buildcodes.shtml
- Massachusetts: Board of Building Regulations and Standards (BBRS). https://www.mass.gov/
- Michigan: LARA Bureau of Construction Codes. https://www.michigan.gov/lara/bureau-list/bcc
- Minnesota: Minnesota Department of Labor and Industry (DLI). https://www.dli.mn.gov/
- Mississippi: Mississippi Building Codes Council (Mississippi Insurance Dept., State Fire Marshal). https://www.mid.ms.gov/sfmo/mississippi-uniform-building-codes/
- Missouri: No statewide residential code (local adoption; DNR lists local codes). https://dnr.mo.gov/energy/efficiency/codes-jurisdiction
- Montana: Montana Department of Labor & Industry, Building Codes Program. https://bsd.dli.mt.gov/building-codes-permits/current-codes
- Nebraska: Nebraska Legislature (state building code by statute); local adoption. https://nebraskalegislature.gov/laws/statutes.php?statute=71-6403
- Nevada: No statewide residential code (local adoption). https://www.leg.state.nv.us/nrs/NRS-278.html
- New Hampshire: NH State Building Code Review Board / State Fire Marshal. https://www.firemarshal.dos.nh.gov/laws-rules-regulatory/state-building-code
- New Jersey: NJ Department of Community Affairs, Division of Codes and Standards (Uniform Construction Code). https://www.nj.gov/dca/codes/codreg/current.shtml
- New Mexico: Regulation and Licensing Department, Construction Industries Division. https://www.rld.nm.gov/construction-industries/
- New York: NY Department of State, Division of Building Standards and Codes. https://dos.ny.gov/notice-adoption
- North Carolina: NC Office of State Fire Marshal / Building Code Council / Residential Code Council. https://www.ncosfm.gov/codes/codes-current-and-past
- North Dakota: ND Department of Commerce, Division of Community Services. https://www.commerce.nd.gov/community-services/building-codes
- Ohio: Ohio Board of Building Standards (Dept. of Commerce). https://codes.ohio.gov/ohio-administrative-code/4101:8
- Oklahoma: Oklahoma Uniform Building Code Commission (OUBCC). https://oklahoma.gov/oubcc/codes-and-rules.html
- Oregon: Oregon Building Codes Division (BCD). https://www.oregon.gov/bcd/codes-stand/Pages/residential-structures.aspx
- Pennsylvania: PA Department of Labor & Industry, Uniform Construction Code. https://www.pa.gov/agencies/dli/programs-services/labor-management-relations/bureau-of-occupational-and-industrial-safety/uniform-construction-code.html
- Puerto Rico: UNVERIFIED (OGPe per third-party notice). (no official page confirmed)
- Rhode Island: RI Building Code Standards Committee (State Building Code Office). https://rules.sos.ri.gov/Regulations/Part/510-00-00-2
- South Carolina: SC Building Codes Council (LLR). https://www.llr.sc.gov/bcc/
- South Dakota: No statewide residential code (municipal ordinances; SDCL ch. 11-10). https://sdlegislature.gov/Statutes/11-10
- Tennessee: Tennessee State Fire Marshal's Office (Dept. of Commerce & Insurance). https://www.tn.gov/commerce/fire/codes-enforcement/history.html
- Texas: No state code agency for residential; municipalities enforce (state statute sets minimum). https://guides.sll.texas.gov/texas-law/building-codes
- Utah: Utah Legislature (State Construction Code by statute). https://le.utah.gov/xcode/Title15A/Chapter2/C15A-2-S103_2024070120240501.pdf
- Vermont: Vermont Division of Fire Safety (no state residential building code listed); Dept. of Public Service (RBES energy standards). https://firesafety.vermont.gov/buildingcode/codes
- Virginia: Virginia DHCD / Board of Housing and Community Development. https://www.dhcd.virginia.gov/codes
- Washington: Washington State Building Code Council (SBCC). https://sbcc.wa.gov/
- West Virginia: West Virginia State Fire Commission / State Fire Marshal. https://firemarshal.wv.gov/
- Wisconsin: Wisconsin Department of Safety and Professional Services (DSPS). https://dsps.wi.gov/a-z-programs-list/udc/
- Wyoming: Wyoming State Fire Marshal (state-adopted codes; residential scope UNVERIFIED). https://wsfm.wyo.gov/

- **International Code Council (ICC):** publisher of the International Residential Code®, International Building Code® and related I-Codes, and host of ICC Digital Codes (https://codes.iccsafe.org/). State pages are linked, not reproduced. IRC, IBC and I-Codes are ICC marks.
- **Map boundaries:** U.S. Census Bureau, Cartographic Boundary File cb_2024_us_state_500k (public domain).
- **Status lookups:** U.S. DOE Building Energy Codes Program state pages (energycodes.gov), used for "None Statewide" (AZ, KS, MO, CO).
