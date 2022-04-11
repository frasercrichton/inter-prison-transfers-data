# Inter-prison Transfers in Aotearoa New Zealand

<img width="805" alt="Screen Shot 2022-04-11 at 10 37 15 PM" src="https://user-images.githubusercontent.com/52700324/162723383-74d88090-bc0b-4404-8395-53edd91a5430.png">


Data and scripts to format and interrogate data provided by Corrections NZ on Inter-prison transfers between 2 July 2018 and 22 July 2021.

## Freedom of Information Request (FOI) - Inter-prison Transfers Across Time and Place

https://fyi.org.nz/request/16105-inter-prison-transfers-across-time-and-place#outgoing-27826

## Inter-prison Transfer Data Format 

The original spreadsheet provided by Corrections includes the following fields.

### From

Prison Name as abbreviation.

### To

Prison Name as abbreviation.

### Reasons

* **Population Pressure** - Adviser Prison Population only 
  1. For muster management purpose. 
  2. To separate different categories of prisoners
* **Judicial** - RO staff, PCO of the unit or Board Liaison Officers 
  1. For Judicial purposes. The transfer is pursuant to section 143 of the Sentencing Act 2002
* **Medical** - Health staff 
  1. to provide Health care
* **Placement Management** - Prison Director, Residential Manager or  PCO 
  1. to ensure the safety of that prisoner or any other reason 
  2. to reduce the risk of suicide or self-harm transfer has been directed by the Chief Executive or an Inspector 
  3. to restore or maintain security and order of the prison
* **Personal Request** - PCO 
  1. prisoner request transfer 
* **Accepted for Programme** - PCO or delegate from the destination unit 
  1. for reintegration / rehabilitation purposes 
  2. to address offender plan activities
* **Release** - PCO or RO staff to be close to home region
* **Placement Review** - PCO 
  1. to assist in likelihood of reducing re-offending due to change in security classification to allow for repairs or alterations at the prison

[https://www.corrections.govt.nz/resources/policy_and_legislation/Prison-Operations-Manual/Movement/M.04-External-movement-transportation-of-prisoners/M.04.03-Inter-prison-transfers](https://www.corrections.govt.nz/resources/policy_and_legislation/Prison-Operations-Manual/Movement/M.04-External-movement-transportation-of-prisoners/M.04.03-Inter-prison-transfers)

### Transfer Date

The date the person was transferred. 

### Status At Transfer

* Sentenced (Maximum)
* Sentenced (High)
* Sentenced (Minimum)
* Sentenced (Low Medium)
* Sentenced (Low)

* Remand - Convicted
* Remand - Accused

## Errata

The following records were did not include dates.

SHCF,Waikeria,Judicial,,
MECF,NRCF,In Transit/Multi-Site Move,,
MECF,SHCF,Judicial,,
MECF,SHCF,Personal Request,,
Rimutaka,SHCF,In Transit/Multi-Site Move,,

## Prison Locations Data Format

|Field | Description |
| ----------- | ----------- |
| Prison | Prison Name|
| Abbreviated   | Abbreviated Name |
| Official Name | Corrections NZ Name |
| Capacity | Prison popluation capacity |
| Opened | Date opened|
| Closed | Date closed|
| Gender |  Men/Women |
| Classification | Minimum/Low/Low-Medium/High/Maximum |
| Latitude | Latitude |
| Longitude | Longitude |
| Name | Common Name |

## Scripts

### Cleanse

* Remove anything not used in the visualisation
* Add latitude and longitude
* segregate out population manaegment stats from over all stats.

### Visualise

Generate a map with PyDeck.
