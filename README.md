<a id="readme-top"></a>

<h3 align="center">Bank-Account-Balance</h3>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#TO-DO">TO-DO</a></li>
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

<!-- GETTING STARTED -->
## Getting Started
<p align="left">(<a href="#readme-top">back to top</a>)</p>

### Prerequisites
Ensure you have Python installed. You will also need the following Python libraries:

- pandas
- matplotlib
- openpyxl

You can install these using pip:
* pandas
  ```sh
  pip install pandas

* matplotlib
  ```sh
pip install matplotlib

*os
  ```sh
pip install os

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Following reports are created
- [1] XLSL of expenses with item, price
- [2] XLSL report of incomes/outcomes
- [3] PNG report of incomes/outcomes

Modified clean data can be further allocated to categories.
Example:
Column C 'Type of Expense' 
- [0] Incomes/Expenses for items WANTED
- [1] Expenses for items NEEDED
- [X] Different/to be checked

<p align="left">(<a href="#go-to-roadmap">for details see roadmap</a>)</p>

<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
<a id="go-to-roadmap"></a>

1. **Prepare the Input CSV File:**
   - Ensure your input CSV file is named `bank.csv`.
   - Place `bank.csv` in the same directory as the script.

2. **Run the Script:**
   - Execute the script using the following command in your command line or terminal:
     ```bash
     python script_name.py
     ```

3. **Output:**
   - The script creates a new CSV file named `bank_report_MM_YY.csv`.
   - An Excel file named `expenses_report.xlsx` is also generated.
   - Both files are saved in the same directory as the script.



<p align="left">(<a href="#readme-top">back to top</a>)</p>

<!-- TO-DO -->
## TO-DO
<p align="left">(<a href="#readme-top">back to top</a>)</p>

- create delete_multiple_columns.py and run it before main.py


<!-- CONTACT -->
## Contact

Timon Nemeth -  timon.nemeth@gmail.com

Project Link: [https://github.com/AnkiMonkey/Bank-Account-Balance](https://github.com/AnkiMonkey/Bank-Account-Balance)

<p align="left">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/AnkiMonkey/Bank-Account-Balance.svg?style=for-the-badge
[contributors-url]: https://github.com/AnkiMonkey/Bank-Account-Balance/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AnkiMonkey/Bank-Account-Balance.svg?style=for-the-badge
