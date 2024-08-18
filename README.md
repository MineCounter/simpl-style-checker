# SIMPL Style Checker

This is a Python-based style checker for the SIMPL programming language. It checks C source code files for adherence to the specified coding style guidelines.
CS244 Stellenbosch University - 2024

## Features

- Checks brace placement
- Verifies function declaration formatting
- Ensures proper spacing around operators and keywords
- Checks indentation and line length
- Verifies preprocessor directive placement
- And many more style checks...

## Known Problems

Indentation and Line endings kinda work, but idk how accurate it is so I've commented the them out, feel free to uncomment it to check.

## Requirements

- Python 3.6+
- colorama

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/simpl-style-checker.git
   ```

2. Change to the project directory:
   ```
   cd simpl-style-checker
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the style checker on a C source file:

```
python style_checker.py <filename>
```

Replace `<filename>` with the path to your C source file.

## Output

The style checker will print any style violations it finds, including:
- The line number where the violation occurred
- The rule number that was violated
- A description of the style violation
- The problematic line of code

If no style errors are found, it will print a success message.

## Contributing

We welcome contributions to improve the SIMPL Style Checker! Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

Please make sure to update tests as appropriate and adhere to the project's coding standards.

### Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.

## Contributors

We appreciate all contributions. Here's a list of the current contributors to the project:

| Name      | Student Number | GitHub Username |
|-----------|----------------|-----------------|
| Alok More | 25876864       | @minecounter    |

If you contribute to this project, please add your name to this table!
