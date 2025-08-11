# Techno Property Nepal – Land Rental System

This is a simple **Land Rental System** developed in Python as a coursework project. The system allows users to rent and return lands, update their statuses, and generate bills (with late return fine calculations). The project uses a text file (`land.txt`) to store a list of available assets (lands) and their details.

## Features

- **Display Available Lands:** View a list of lands along with details such as Land ID, Location, Direction, Anna, Price, and current Status.
- **Rent a Land:** 
  - Validate user input (name, phone number, and rental duration).
  - Calculate the total rental price.
  - Update the asset status to "Not_Available".
  - Generate a detailed bill saved as a text file with a unique timestamp.
- **Return a Land:**
  - Allow users to return a previously rented land.
  - Calculate a fine if the land is returned later than the agreed number of months.
  - Update the asset status back to "Available".
  - Generate a detailed return bill saved as a text file.

## File Structure
- Main.py # Main entry point of the application.
- operation.py # Contains functions for renting, returning, billing, and fine calculation.
- read.py # Contains functions to read and display the available lands from land.txt. 
- write.py # Contains functions to update the land status in land.txt. 
- land.txt # Text file storing asset (land) details.


## Requirements

- Python 3.x  
- No external libraries required (only uses standard libraries such as `datetime`).

## Getting Started

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/land-rental-system.git
   cd Assect-Rental-System

## How It Works
- **Renting a Land:**
When renting a land, the system will:

  - Display available lands.
  - Ask for the Land ID to rent.
  - Validate the renter’s details (name and phone number).
  - Request the number of months to rent.
  - Calculate and display the total rental price.
  - Update the land status to "Not_Available" in land.txt.
  - Generate a bill file (e.g., bill_20250215123045.txt) containing all details.

- **Returning a Land:**
When returning a land, the system will:

  - Display available lands.
  - Ask for the Land ID to return.
  - Calculate any late return fine based on the agreed rental period.
  - Update the land status back to "Available" in land.txt.
  - Generate a return bill with details and any applicable fine.
