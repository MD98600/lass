
#que 17
assembly_code = [
    "LOAD A",
    "STORE B",
    "MACRO ABC",
    "LOAD p",
    "SUB q",
    "MEND",
    "MACRO ADD1 ARG",
    "LOAD X",
    "STORE ARG",
    "MEND",
    "MACRO ADD5 A1, A2, A3",
    "STORE A2",
    "ADD1 5",
    "ADD1 10",
    "LOAD A1",
    "LOAD A3",
    "MEND",
    "ABC",
    "ADD5 D1, D2, D3",
    "END"
]

mdt = []
inside_macro = False
arg_map = {}
macro_name = ""
line_number = 1  # For numbering instructions (excluding macro name comment)

for line in assembly_code:
    stripped = line.strip()

    if not stripped:
        continue

    if stripped.startswith("MACRO"):
        inside_macro = True
        macro_header = stripped.split()
        macro_name = macro_header[1]
        args = []

        # Extract parameters if available
        if len(macro_header) > 2:
            args = [arg.strip() for arg in ' '.join(macro_header[2:]).split(',')]
        elif ',' in macro_name:  # Handle cases like MACRO ADD5 A1, A2, A3
            macro_name, *args = macro_name.split(',')
            macro_name = macro_name.strip()
            args = [arg.strip() for arg in args]

        arg_map = {arg: f"#" + str(i + 1) for i, arg in enumerate(args)}
        mdt.append(f"; {macro_name}")  # Comment without line number

    elif stripped == "MEND":
        mdt.append(f"{line_number}\tMEND")
        line_number += 1
        inside_macro = False
        arg_map = {}
    elif inside_macro:
        parts = stripped.split()
        replaced_parts = []
        for part in parts:
            if part in arg_map:
                replaced_parts.append(arg_map[part])
            else:
                replaced_parts.append(part)
        new_line = " ".join(replaced_parts)
        mdt.append(f"{line_number}\t{new_line}")
        line_number += 1

# Output MDT
print("Macro Definition Table (MDT):\n")
for line in mdt:
    print(line)




#que 18
# Input assembly code
assembly_code = [
    "STORE P",
    "LOAD Q",
    "MACRO PCG",
    "LOAD m",
    "ADD n",
    "MEND",
    "MOV S",
    "MACRO ADDi PAR",
    "LOAD A",
    "STORE PAR",
    "MEND",
    "DIV B",
    "MACRO ADDii V1, V2, V3",
    "STORE V2",
    "ADDi 12",
    "ADDi 7",
    "LOAD V1",
    "LOAD V3",
    "MEND",
    "PCG",
    "ADDii Q1, Q2, Q3",
    "END"
]

mdt = []  # Macro Definition Table
inside_macro = False  # Flag to track if we're inside a macro definition
arg_map = {}  # Map to hold argument replacements
macro_name = ""  # Store current macro name
line_number = 1  # Line numbering for MDT

# Process each line of assembly code
for line in assembly_code:
    stripped = line.strip()  # Remove leading/trailing whitespaces

    if not stripped:
        continue

    if stripped.startswith("MACRO"):
        # Begin a new macro definition
        inside_macro = True
        macro_header = stripped.split()
        macro_name = macro_header[1]  # Get the macro name
        args = []

        # Extract arguments if available
        if len(macro_header) > 2:
            args = [arg.strip() for arg in ' '.join(macro_header[2:]).split(',')]
        arg_map = {arg: f"#" + str(i + 1) for i, arg in enumerate(args)}  # Map arguments to #1, #2, etc.
        mdt.append(f"; {macro_name}")  # Comment line for macro name

    elif stripped == "MEND":
        # End of macro definition
        mdt.append(f"{line_number}\tMEND")
        line_number += 1
        inside_macro = False  # Exit macro definition
        arg_map = {}  # Clear argument map
    elif inside_macro:
        # Inside a macro definition, handle argument replacements
        parts = stripped.split()
        replaced_parts = []
        for part in parts:
            if part in arg_map:
                replaced_parts.append(arg_map[part])  # Replace with positional parameter
            else:
                replaced_parts.append(part)  # Leave other parts unchanged
        new_line = " ".join(replaced_parts)
        mdt.append(f"{line_number}\t{new_line}")
        line_number += 1

# Output MDT
print("Macro Definition Table (MDT):\n")
for line in mdt:
    print(line)
