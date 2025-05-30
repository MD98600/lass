#Que 4
# Assembly code lines
assembly_code = [
    "START 100",
    "READ A",
    "READ B",
    "MOVER AREG, ='50'",
    "MOVER BREG, ='60'",
    "ADD AREG, BREG",
    "LOOP MOVER CREG, A",
    "ADD CREG, ='10'",
    "COMP CREG, B",
    "BC LT, LOOP",
    "NEXT SUB AREG, ='10'",
    "COMP AREG, B",
    "BC GT, NEXT",
    "STOP",
    "A DS 1",
    "B DS 1",
    "END"
]

# Initialize  Literal table, and location counter
literal_table = {}
loc_counter = 0  # Starting location counter from the START directive

# Pass 1: Process instructions and storage (but don't assign addresses to literals yet)
literals = []  # To store the literals temporarily

for line in assembly_code:
    parts = line.strip().split()

    if not parts:
        continue

    # Process literals (identified by '=' sign) and add them to literals list
    for part in parts:
        if part.startswith("='"):
            literals.append(part)

    # Handle START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])  # Set location counter from START
    # Handle DS (Define Storage) directive
    elif len(parts) > 1 and parts[1] == "DS":
        loc_counter += int(parts[2])  # Allocate space for DS
    else:
        loc_counter += 1  # Instructions take 1 address space

# After END directive, assign addresses to literals
for literal in literals:
    if literal not in literal_table:
        literal_table[literal] = loc_counter
        loc_counter += 1  # Increment location counter for each literal

# Output the Literal table
print("Literal Table:")
print("{:<10} {:<10}".format("Literal", "Address"))
for literal, address in literal_table.items():
    print("{:<10} {:<10}".format(literal, address))




#Que 5
# Assembly code lines
assembly_code = [
    "START 200",
    "READ X",
    "READ Y",
    "MOVER AREG, ='5'",
    "MOVER BREG, ='6'",
    "ADD AREG, BREG",
    "LOOP MOVER CREG, X",
    "ADD CREG, ='1'",
    "COMP CREG, Y",
    "BC LT, LOOP",
    "NEXT SUB AREG, ='1'",
    "COMP AREG, Y",
    "BC GT, NEXT",
    "STOP",
    "X DS 1",
    "Y DS 1",
    "END"
]

# Initialize Symbol table, Literal table, and location counter
symbol_table = {}
literal_table = {}
loc_counter = 0  # Will be set by START directive

# Pass 1: Process instructions and storage (but don't assign addresses to literals yet)
literals = []  # To store the literals temporarily

for line in assembly_code:
    parts = line.strip().split()

    if not parts:
        continue

    # Process literals (identified by '=' sign) and add them to literals list
    for part in parts:
        if part.startswith("='"):
            literals.append(part)

    # Handle START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])  # Set location counter from START
    # Handle DS (Define Storage) directive
    elif len(parts) > 1 and parts[1] == "DS":
        loc_counter += int(parts[2])  # Allocate space for DS
    else:
        loc_counter += 1  # Instructions take 1 address space

# After END directive, assign addresses to literals
for literal in literals:
    if literal not in literal_table:
        literal_table[literal] = loc_counter
        loc_counter += 1  # Increment location counter for each literal

# Output the Literal table
print("Literal Table:")
print("{:<10} {:<10}".format("Literal", "Address"))
for literal, address in literal_table.items():
    print("{:<10} {:<10}".format(literal, address))






#que 6
# Assembly code lines
assembly_code = [
    "START 300",
    "READ M",
    "READ N",
    "MOVER AREG, ='51'",
    "MOVER BREG, ='61'",
    "ADD AREG, BREG",
    "LOOP MOVER CREG, M",
    "ADD CREG, ='11'",
    "COMP CREG, N",
    "BC LT, LOOP",
    "NEXT SUB AREG, ='11'",
    "COMP AREG, N",
    "BC GT, NEXT",
    "STOP",
    "M DS 1",
    "N DS 1",
    "END"
]

# Initialize Literal Table and Location Counter
literal_table = {}
loc_counter = 0
literals = []

# First Pass: Gather literals and simulate LOC counter
for line in assembly_code:
    parts = line.strip().split()

    if not parts:
        continue

    # Detect literals and collect them
    for part in parts:
        if part.startswith("='") :
            literals.append(part)

    # START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])
    # DS (Define Storage)
    elif len(parts) > 1 and parts[1] == "DS":
        loc_counter += int(parts[2])
    else:
        loc_counter += 1  # each instruction occupies 1 memory word

# After END, assign addresses to literals
for literal in literals:
    if literal not in literal_table:
        literal_table[literal] = loc_counter
        loc_counter += 1

# Output the Literal Table
print("Literal Table:")
print("{:<10} {:<10}".format("Literal", "Address"))
for literal, address in literal_table.items():
    print("{:<10} {:<10}".format(literal, address))
