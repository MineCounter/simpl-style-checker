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
   git clone git@github.com:MineCounter/simpl-style-checker.git
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

I recommend piping to an output file for better readability and scrolling!

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

By participating in this project, you agree to abide by the following Code of Conduct:

1. **Competence**: Only contribute to areas where you have sufficient knowledge and expertise. If you're unsure about a particular aspect of the project, ask for guidance before making changes.

2. **Responsibility**: Take responsibility for your contributions. Test your changes thoroughly before submitting a pull request. If you introduce a bug, be prepared to fix it.

3. **Respect**: Respect the existing codebase and coding standards. Do not make arbitrary changes to established patterns or styles without discussion and consensus.

4. **Communication**: Clearly communicate your intentions and reasoning behind significant changes. Use descriptive commit messages and pull request descriptions.

5. **Collaboration**: Be open to feedback and constructive criticism. Be willing to iterate on your contributions based on review comments.

6. **Documentation**: Update relevant documentation when making changes that affect the project's usage or setup.

7. **No Malicious Code**: Do not intentionally introduce bugs, security vulnerabilities, or malicious code.

8. **Ask for Help**: If you're stuck or unsure about something, ask for help. It's better to seek assistance than to make uninformed changes.

9. **Respect Intellectual Property**: Ensure you have the right to contribute any code you submit. Do not copy code from other sources without proper attribution and licensing.

10. **Maintain Project Integrity**: Do not attempt to make changes that fundamentally alter the project's purpose or scope without prior discussion with the project maintainer.

Remember: If you don't fully understand the implications of your changes, it's best to refrain from making them. Instead, open an issue to discuss your ideas or questions with the project maintainers and other contributors.

Failure to comply with this Code of Conduct may result in your contributions being rejected or your submission in the project being restricted.

## Contributors

We appreciate all contributions. Here's a list of the current contributors to the project:

| Name      | Student Number | GitHub Username |
|-----------|----------------|-----------------|
| Alok More | 25876864       | @minecounter    |

If you contribute to this project, please add your name to this table!
