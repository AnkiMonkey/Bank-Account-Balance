<a id="readme-top"></a>

<h3 align="center">Bank-Account-Balance</h3>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#getting-started">Getting Started</a></li>
    <ul>
      <li><a href="#prerequisites">Prerequisites</a></li>
    </ul>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#to-do">TO-DO</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

BankApp is a Python script that processes a CSV file of bank transactions to generate detailed reports. It performs the following tasks:
- Processes the CSV file, modifies its header, removes specific unwanted columns.
- Calculates sum totals for profits and expenses.
- Generates a report with a table and a bar graph.
- Saves the modified data to a new Excel file which is used to allocate expenses to categories.
<p align="left">(<a href="#readme-top">back to top</a>)</p>

<p align="center">
  <img src="./mindmup.png" alt="Mindmup Diagram" width="500"/>
</p>


<!-- GETTING STARTED -->
## Getting Started
<p align="left">(<a href="#readme-top">back to top</a>)</p>

### Prerequisites
Ensure you have Python installed. You will also need the following Python libraries:

- pandas
- matplotlib
- openpyxl


<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Following reports are created:
- [1] XLSX of expenses with item, price
- [2] XLSX report of incomes/outcomes
- [3] PNG report of incomes/outcomes

Modified clean data can be further allocated to categories.
Example:
Column C 'Type of Expense':
- [0] Incomes/Expenses for items WANTED
- [1] Expenses for items NEEDED
- [X] Different

<p align="left">(<a href="#roadmap">for details see roadmap</a>)</p>

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
<a id="roadmap"></a>

1. **Prepare the Input CSV File:**
   - Ensure your input CSV file is in the same directory as the script.
   - Make sure the script has only data in Column A, otherwise it will not work. 

2. **Run the Script:**


3. **Output:**
   - The script creates a new CSV file named `bank_report_MM_YY.csv`.
   - An Excel file named `expenses_report.xlsx` is also generated.
   - Both files are saved in the same directory as the script.

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- TO-DO -->
## TO-DO
<p align="left">(<a href="#readme-top">back to top</a>)</p>

- Create `delete_multiple_columns.py` and run it before `main.py`.
- Delete all columns but A
- Did not work yet

<!-- CONTACT -->
## Contact

Timon Nemeth - timon.nemeth@gmail.com

Project Link: [https://github.com/AnkiMonkey/Bank-Account-Balance](https://github.com/AnkiMonkey/Bank-Account-Balance)

<p align="left">(<a href="#readme-top">back to top</a>)</p>
