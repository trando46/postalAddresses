# Postal Address Search
This is a simple program for Software Architecture and Design 5200 at Seattle Univeristy

# Project Requirements
1. A web-based user interface (a form) that can capture a country-specific address format entered by an end user
    - The form must dynamically adjust to capture the address based on the address format
    - Validation of the address formats and related data must occur in a reasonable time for the user
    - The end user should be able to select data from appropriate user interface elements and not just type everything in free-form
    - Where possible, default values and constrained lists should be presented to the user
2. A way for a user to search for a given address based on the country-specific format and user interface
3. A way for a user to search across countries to find structurally-"matching" addresses and display them in the application
4. An API callable via HTTP (curl or postman) because we might want to sell access to this application
    - Documentation for the API, preferably available alongside the API itself (think swagger / OpenAPI)

# Supported Countries
Brazil, Canada, Germany, India, Japan, South Korea, Mexico, Spain, UK, USA

## Architecture Design = MVC
## Design Pattern = Respository patter
