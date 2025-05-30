#que 15
# Assembly input with macros
import re
assembly_code = [
    "LOAD F",
    "STORE E",
    "MACRO SRS",
    "LOAD s",
    "SUB t",
    "MEND",
    "STORE k",
    "MACRO ADD3 XYZ",
    "LOAD U",
    "STORE XYZ",
    "MEND",
    "Add m",
    "MACRO ADD1 Si, Sii, Siii",
    "LOAD Sii",
    "ADD3 1",
    "ADD3 11",
    "STORE Si",
    "STORE Siii",
    "MEND",
    "SRS",
    "ADD1 C1, C2, C3",
    "ADD3 q",
    "END"
]

# Pass 1: Store macro definitions
macros = {}
intermediate_code = []
macro_def = []
macro_name = ""
inside_macro = False

for line in assembly_code:
    parts = line.strip().split()
    if not parts:
        continue
    if parts[0] == "MACRO":
        macro_name = parts[1]
        macro_def = []
        inside_macro = True
    elif parts[0] == "MEND":
        macros[macro_name] = macro_def
        inside_macro = False
    elif inside_macro:
        macro_def.append(line.strip())
    else:
        intermediate_code.append(line.strip())

# Helper: Expand macro calls recursively with proper parameter substitution
def expand_macro(line):
    parts = line.strip().split()
    if not parts:
        return [line]

    name = parts[0]

    if name in macros:
        macro_body = macros[name]
        if name == "ADD3":
            param = parts[1]
            return [stmt.replace("XYZ", param) for stmt in macro_body]
        elif name == "ADD1":
            si, sii, siii = parts[1], parts[2], parts[3]
            expanded = []
            for stmt in macro_body:
                replaced = stmt
                replaced = re.sub(r'\bSiii\b', siii, replaced)
                replaced = re.sub(r'\bSii\b', sii, replaced)
                replaced = re.sub(r'\bSi\b', si, replaced)
                if replaced.split()[0] in macros:
                    expanded.extend(expand_macro(replaced))
                else:
                    expanded.append(replaced)
            return expanded
        elif name == "SRS":
            return macro_body
    return [line]


# Pass 2: Expand macros in intermediate code
final_code = []
for line in intermediate_code:
    expanded = expand_macro(line)
    final_code.extend(expanded)

# Clean commas if any (optional)
final_code = [line.rstrip(',') for line in final_code]

# Output
print("Intermediate Code:")
for line in final_code:
    print(line)





#que 16
import re

# Input assembly code with macros
assembly_code = [
    "LOAD J",
    "STORE M",
    "MACRO EST",
    "LOAD e",
    "ADD d",
    "MEND",
    "LOAD S",
    "MACRO SUB4 ABC",
    "LOAD U",
    "STORE ABC",
    "MEND",
    "LOAD P",
    "ADD V",
    "MACRO ADD7 P4, P5, P6",
    "LOAD P5",
    "SUB4 XYZ",
    "SUB 8",
    "SUB 2",
    "STORE P4",
    "STORE P6",
    "MEND",
    "EST",
    "ADD7 C4, C5, C6",
    "SUB4 z",
    "END"
]

# Pass 1: Store macro definitions
macros = {}
intermediate_code = []
macro_def = []
macro_name = ""
inside_macro = False

for line in assembly_code:
    parts = line.strip().split()
    if not parts:
        continue
    if parts[0] == "MACRO":
        macro_name = parts[1]
        macro_def = []
        inside_macro = True
    elif parts[0] == "MEND":
        macros[macro_name] = macro_def
        inside_macro = False
    elif inside_macro:
        macro_def.append(line.strip())
    else:
        intermediate_code.append(line.strip())

# Helper: Expand macro calls with proper substitution
def expand_macro(line):
    parts = line.strip().split()
    if not parts:
        return [line]

    name = parts[0]

    if name in macros:
        macro_body = macros[name]

        if name == "EST":
            return macro_body

        elif name == "SUB4":
            abc = parts[1]
            return [stmt.replace("ABC", abc) for stmt in macro_body]

        elif name == "ADD7":
            p4, p5, p6 = parts[1], parts[2], parts[3]
            expanded = []
            for stmt in macro_body:
                stmt = re.sub(r'\bP4\b', p4, stmt)
                stmt = re.sub(r'\bP5\b', p5, stmt)
                stmt = re.sub(r'\bP6\b', p6, stmt)
                # handle inner macro SUB4 XYZ
                if stmt.startswith("SUB4"):
                    xyz_param = stmt.split()[1]
                    stmt = stmt.replace("XYZ", p5)  # use P5 value in place of XYZ
                    expanded.extend(expand_macro(stmt))
                else:
                    expanded.append(stmt)
            return expanded

    return [line]

# Pass 2: Expand macros
final_code = []
for line in intermediate_code:
    expanded = expand_macro(line)
    final_code.extend(expanded)

# Clean up (optional)
final_code = [line.rstrip(',') for line in final_code]

# Output
print("Intermediate Code:")
for line in final_code:
    print(line)
