# Python Geolocation API Client

This Python script retrieves geographic information for a given location using a web API.

## Features
- Sends requests to a geolocation API
- Parses JSON responses
- Extracts:
  - Longitude
  - Latitude
  - Country
  - State

## Technologies Used
- Python
- urllib
- JSON
- Web APIs

## How it Works
1. The user enters a location.
2. The program builds an API request URL.
3. The API returns location data in JSON format.
4. The script extracts useful geographic information.

## Example

Input:
Type the location here: Gebäude 78 – Besucherempfang

Output:
this is lon 13.4050
this is lat 52.5200
location Germany, Berlin
