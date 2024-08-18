import re
import sys
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform colored output
init()
error_count = 0;

def check_style(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    in_comment = False
    for line_num, line in enumerate(lines, 1):
        # Check if we're in a multi-line comment
        if '/*' in line:
            in_comment = True
        if '*/' in line:
            in_comment = False
            continue
        if in_comment:
            continue

        # Remove strings and single-line comments for certain checks
        code_line = remove_strings_and_comments(line)

        check_brace_placement(line, code_line, line_num, lines)
        check_function_brace(line, code_line, line_num, lines)
        check_else_placement(line, code_line, line_num)
        check_case_alignment(line, code_line, line_num, lines)
        check_function_spacing(line, code_line, line_num)
        check_if_for_while_spacing(line, code_line, line_num)
        check_sizeof_spacing(line, code_line, line_num)
        check_general_spacing(line, code_line, line_num, lines)
        check_switch_spacing(line, code_line, line_num)
        check_parentheses_spacing(line, code_line, line_num)
        check_additive_operator_spacing(line, code_line, line_num)
        check_multiplicative_operator_spacing(line, code_line, line_num)
        check_preprocessor_directives(line, line_num)
        check_line_endings(line, line_num)
        check_function_separation(line, code_line, line_num, lines)
        #check_indentation(line, line_num)
        check_line_length(line, line_num)

    check_global_rules(lines)
    if error_count == 0:
        print(f"{Fore.GREEN}No style errors found.{Style.RESET_ALL}")
    else:
        print(f"{Fore.CYAN}Total style errors found: {error_count}{Style.RESET_ALL}")

def remove_strings_and_comments(line):
    # Remove string literals
    line = re.sub(r'"([^"\\]|\\.)*"', '', line)
    line = re.sub(r"'([^'\\]|\\.)*'", '', line)
    # Remove single-line comments
    line = re.sub(r'//.*$', '', line)
    return line

def is_function_declaration(line, lines=None, line_num=None):
    if lines and line_num:
        # This is the old version for checking across multiple lines
        if line_num < len(lines):
            return re.search(r'^\w+\s+\w+\s*\([^)]*\)\s*$', line) and lines[line_num].strip() == '{'
    else:
        # This is the new version for checking a single line
        return re.search(r'^\s*\w+\s+\w+\s*\([^)]*\)\s*$', line)
    return False

def check_brace_placement(line, code_line, line_num, lines):
    # Check for valid brace placements
    if re.search(r'(if|for|while|else)\s*(\([^)]*\))?\s*{', code_line):
        # Check if there's exactly one space before the opening brace
        if not re.search(r'(if|for|while|else)\s*(\([^)]*\))? {', code_line):
            print_error(line_num, 1, "There should be exactly one space before the opening brace", line)
        return  # This is correct placement for if, for, while, and else statements

    # Check for other constructs that might have braces (like function definitions)
    if re.search(r'\)\s*{', code_line) and not re.search(r'^\s*{', code_line):
        if not is_function_declaration(lines[line_num-2], lines, line_num-1):
            if not re.search(r'\) {', code_line):
                print_error(line_num, 1, "There should be exactly one space before the opening brace", line)

def is_in_array_or_struct_init(lines, line_num):
    if line_num > 1:
        prev_lines = lines[max(0, line_num-5):line_num-1]  # Check up to 5 lines before
        for line in reversed(prev_lines):
            if re.search(r'=\s*{', line):  # Found the start of an initialization
                return True
            if re.search(r'^\s*{', line):  # Found a line starting with {
                return True
            if re.search(r'}\s*;', line):  # Found the end of an initialization
                return False
    return False

def check_function_brace(line, code_line, line_num, lines):
    if line_num > 1 and re.search(r'^\s*{', code_line):
        if is_in_array_or_struct_init(lines, line_num):
            return  # This is part of an array or struct initialization, not a function body
        
        prev_line = remove_strings_and_comments(lines[line_num-2])
        if is_function_declaration(prev_line):
            return  # This is a correct function body brace placement
        
        if re.search(r'\)\s*$', prev_line):
            print_error(line_num, 2, "For function bodies, the opening brace must go on a new line", line)

def check_else_placement(line, code_line, line_num):
    # Check for 'else' placement, but ignore 'else if'
    if re.search(r'}\s*else\b(?!\s*if)', code_line):
        if not re.search(r'}\s*else\s*{', code_line):
            print_error(line_num, 3, "else (and its opening brace, if applicable) must be on the same line as the closing brace", line)

def check_case_alignment(line, code_line, line_num, lines):
    if re.search(r'^\s*case', code_line):
        switch_indent = None
        for prev_line in reversed(lines[:line_num-1]):
            if 'switch' in remove_strings_and_comments(prev_line):
                switch_indent = len(prev_line) - len(prev_line.lstrip())
                break
        if switch_indent is not None:
            case_indent = len(line) - len(line.lstrip())
            if case_indent != switch_indent and case_indent != switch_indent + 4:
                print_error(line_num, 4, "case statements must either align with switch or have one extra level of indentation", line)

def check_function_spacing(line, code_line, line_num):
    if re.search(r'\w+\s+\(', code_line) and is_function_declaration(line, [], line_num):
        print_error(line_num, 5, "No spaces between function name and opening parenthesis in function declarations", line)

def check_if_for_while_spacing(line, code_line, line_num):
    if re.search(r'\b(if|for|while)\(', code_line):
        print_error(line_num, 6, "Space required between if/for/while and opening parenthesis", line)

def check_sizeof_spacing(line, code_line, line_num):
    if re.search(r'sizeof\s+\(', code_line) or re.search(r'sizeof\([^)]+\s+', code_line):
        print_error(line_num, 7, "sizeof must be treated as a function call with no spaces", line)

def is_in_table_or_static_init(lines, line_num):
    if line_num > 1:
        prev_line = remove_strings_and_comments(lines[line_num - 2])
        return re.search(r'=\s*{?\s*$', prev_line) or re.search(r'^\s*{', prev_line)
    return False

def check_general_spacing(line, code_line, line_num, lines):
    # Check if we're in a table or static initialization
    in_table_or_static = is_in_table_or_static_init(lines, line_num)
    
    if not in_table_or_static:
        # Check for space after comma
        if re.search(r',\S', code_line):
            print_error(line_num, 8, "Space required after comma", line)
        
        # Check for space after semicolon
        if re.search(r';\S', code_line):
            print_error(line_num, 8, "Space required after semicolon", line)

def check_switch_spacing(line, code_line, line_num):
    if re.search(r'switch\(', code_line):
        print_error(line_num, 9, "Space required between switch and opening parenthesis", line)

def check_parentheses_spacing(line, code_line, line_num):
    # Check for spaces after opening parenthesis
    if re.search(r'\(\s{2,}', code_line):
        print_error(line_num, 10, "No more than one space after opening parenthesis", line)
    
    # Check for spaces before closing parenthesis
    if re.search(r'\s{2,}\)', code_line):
        print_error(line_num, 10, "No spaces immediately before closing parenthesis", line)

def check_additive_operator_spacing(line, code_line, line_num):
    # Ignore -> operator
    code_line = re.sub(r'->', '', code_line)
    if re.search(r'[^\s+-][+-][^\s+-]', code_line) and not re.search(r'\[.*[+-].*\]', code_line):
        print_error(line_num, 11, "Spaces required around additive operators outside of array indices", line)

def check_multiplicative_operator_spacing(line, code_line, line_num):
    if re.search(r'[^\s*/][*/][^\s*/]', code_line) and not re.search(r'\*/', code_line):
        print_error(line_num, 12, "Spaces required around multiplicative operators", line)

def check_preprocessor_directives(line, line_num):
    if re.search(r'^\s+#', line):
        print_error(line_num, 13, "Preprocessor directives must be flush with the left margin", line)

def check_line_endings(line, line_num):
    if line.rstrip() != line.rstrip('\n'):
        print_error(line_num, 14, "Lines must not end with space characters", line)

def check_function_separation(line, code_line, line_num, lines):
    if is_function_declaration(line, lines, line_num):
        if line_num > 1 and lines[line_num-2].strip() != '':
            print_error(line_num, 15, "Function definitions must be separated by at least one blank line", line)

def check_indentation(line, line_num):
    indent = len(line) - len(line.lstrip())
    if indent % 4 != 0:
        print_error(line_num, 16, "Indentation must be made with tab characters", line)

def check_line_length(line, line_num):
    if len(line.rstrip()) > 80:
        print_error(line_num, 17, "Line exceeds 80 characters", line)

def check_global_rules(lines):
    check_brace_style(lines)

def check_brace_style(lines):
    brace_style = "unknown"
    for line_num, line in enumerate(lines, 1):
        code_line = remove_strings_and_comments(line)
        if re.search(r'(if|for|while)\s*\([^)]*\)\s*{', code_line):
            if brace_style == "unknown":
                brace_style = "same_line"
            elif brace_style != "same_line":
                print_error(line_num, 18, "Inconsistent brace style for control structures. Use 'One True Brace' style throughout", line)
        elif re.search(r'(if|for|while)\s*\([^)]*\)\s*$', code_line) and line_num < len(lines) and lines[line_num].strip() == '{':
            if brace_style == "unknown":
                brace_style = "next_line"
            elif brace_style != "next_line":
                print_error(line_num, 18, "Inconsistent brace style for control structures. Use 'One True Brace' style throughout", line)

def print_error(line_num, rule_num, message, line):
    global error_count
    error_count += 1
    print(f"{Fore.RED}Line {line_num} - Rule {rule_num}: {message}{Style.RESET_ALL}")
    print(f"{line.rstrip()}")
    print(f"{Fore.YELLOW}{'^' * len(line.rstrip())}{Style.RESET_ALL}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python style_checker.py <filename>")
        sys.exit(1)
    
    check_style(sys.argv[1])