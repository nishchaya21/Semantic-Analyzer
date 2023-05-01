import ast

def analyze_python_program(program):
    """
    Analyze a Python program and return a list of semantic errors.

    :param program: str, the Python program to analyze
    :return: list of str, the semantic errors found in the program
    """
    errors = []

    # Parse the Python program
    try:
        parsed_program = ast.parse(program)
    except SyntaxError as e:
        errors.append(f"Syntax error: {e}")
        return errors

    # Traverse the AST and check for semantic errors
    for node in ast.walk(parsed_program):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                if node.func.attr == 'append':
                    if isinstance(node.func.value, ast.Name) and node.func.value.id == 'list':
                        errors.append(f"Using 'list.append' is not recommended, use the '+' operator instead. Line {node.lineno}")
            elif isinstance(node.func, ast.Name):
                if node.func.id == 'print':
                    errors.append(f"Using 'print' is not recommended, use logging instead. Line {node.lineno}")

    return errors

program = """
import cmath

a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-bcmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

logging('The solution are {0} and {1}'.format(sol1,sol2))

"""

errors = analyze_python_program(program)

if errors:
    print("The following semantic errors were found:")
    for error in errors:
        print(error)
else:
    print("No semantic errors were found.")