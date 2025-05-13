#que 7
# Assembly code lines
assembly_code = [
    "START 100",
    "READ A",
    "MOVER AREG, ='1'",
    "MOVEM AREG, B",
    "MOVER BREG, ='6'",
    "ADD AREG, BREG",
    "COMP AREG, A",
    "BC GT, LAST",
    "LTORG",
    "NEXT SUB AREG, ='1'",
    "MOVER CREG, B",
    "ADD CREG, ='8'",
    "MOVEM CREG, B",
    "PRINT B",
    "LAST STOP",
    "A DS 1",
    "B DS 1",
    "END"
]

# Initialize tables and location counter
literal_table = []
pool_table = []
loc_counter = 0
unassigned_literals = []

# Pass 1: Process the code and handle literals
for line in assembly_code:
    parts = line.strip().split()

    if not parts:
        continue

    # START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # Scan for literals (always allow duplicates)
    for part in parts:
        if part.startswith("='"):
            unassigned_literals.append(part)

    # LTORG or END assigns addresses to literals
    if parts[0] in ["LTORG", "END"]:
        if unassigned_literals:
            pool_table.append(len(literal_table) + 1)  # 1-based indexing
            for lit in unassigned_literals:
                literal_table.append({
                    'literal': lit,
                    'address': loc_counter
                })
                loc_counter += 1
            unassigned_literals = []

    # Handle DS declarations
    elif len(parts) > 1 and parts[1] == "DS":
        try:
            loc_counter += int(parts[2])
        except:
            loc_counter += 1
    else:
        loc_counter += 1

# Output the Literal Table
print("\nLiteral Table:")
print("{:<10} {:<10}".format("Literal", "Address"))
for item in literal_table:
    print("{:<10} {:<10}".format(item['literal'], item['address']))

# Output the Pool Table
print("\nPool Table:")
print("{:<15}".format("Pool Start Index"))
for index in pool_table:
    print("{:<15}".format(index))



#que 8
# Assembly code lines
assembly_code = [
    "START 200",
    "READ X",
    "MOVER AREG, ='10'",
    "MOVEM AREG, Y",
    "MOVER BREG, ='60'",
    "ADD AREG, BREG",
    "COMP AREG, X",
    "BC GT, LAST",
    "LTORG",
    "NEXT SUB AREG, ='10'",
    "MOVER CREG, Y",
    "ADD CREG, ='80'",
    "MOVEM CREG, Y",
    "PRINT B",
    "LAST STOP",
    "X DS 1",
    "Y DS 1",
    "END"
]

# Initialize tables and location counter
literal_table = []
pool_table = []
loc_counter = 0
unassigned_literals = []

# Pass 1: Process the code and handle literals
for line in assembly_code:
    parts = line.strip().split()

    if not parts:
        continue

    # START directive
    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # Scan for literals (always allow duplicates)
    for part in parts:
        if part.startswith("='"):
            unassigned_literals.append(part)

    # LTORG or END assigns addresses to literals
    if parts[0] in ["LTORG", "END"]:
        if unassigned_literals:
            pool_table.append(len(literal_table) + 1)  # 1-based indexing
            for lit in unassigned_literals:
                literal_table.append({
                    'literal': lit,
                    'address': loc_counter
                })
                loc_counter += 1
            unassigned_literals = []

    # Handle DS declarations
    elif len(parts) > 1 and parts[1] == "DS":
        try:
            loc_counter += int(parts[2])
        except:
            loc_counter += 1
    else:
        loc_counter += 1

# Output the Literal Table
print("\nLiteral Table:")
print("{:<10} {:<10}".format("Literal", "Address"))
for item in literal_table:
    print("{:<10} {:<10}".format(item['literal'], item['address']))

# Output the Pool Table
print("\nPool Table:")
print("{:<15}".format("Pool Start Index"))
for index in pool_table:
    print("{:<15}".format(index))



#que 9
# Assembly code lines
assembly_code = [
    "START 300",
    "READ M",
    "MOVER AREG, ='11'",
    "MOVEM AREG, N",
    "MOVER BREG, ='61'",
    "ADD AREG, BREG",
    "COMP AREG, M",
    "BC GT, LAST",
    "LTORG",
    "NEXT SUB AREG, ='11'",
    "MOVER CREG, N",
    "ADD CREG, ='81'",
    "MOVEM CREG, N",
    "PRINT Y",
    "LAST STOP",
    "M DS 1",
    "N DS 1",
    "END"
]

# Initialize location counter, literal table, and pool table
loc_counter = 0
literal_table = []
pool_table = []
unassigned_literals = []

# First pass: parse and collect literals
for line in assembly_code:
    parts = line.strip().split()

    if not parts:
        continue

    if parts[0] == "START":
        loc_counter = int(parts[1])
        continue

    # Collect literals (duplicates allowed)
    for part in parts:
        if part.startswith("='"):
            unassigned_literals.append(part)

    # Handle LTORG or END to assign addresses to collected literals
    if parts[0] in ["LTORG", "END"]:
        if unassigned_literals:
            pool_table.append(len(literal_table) + 1)  # pool table uses 1-based indexing
            for lit in unassigned_literals:
                literal_table.append({
                    'literal': lit,
                    'address': loc_counter
                })
                loc_counter += 1
            unassigned_literals = []

    # DS directive
    elif len(parts) > 1 and parts[1] == "DS":
        try:
            loc_counter += int(parts[2])
        except:
            loc_counter += 1
    else:
        loc_counter += 1  # Default instruction size is 1

# Output the Literal Table
print("\nLiteral Table:")
print("{:<10} {:<10}".format("Literal", "Address"))
for item in literal_table:
    print("{:<10} {:<10}".format(item['literal'], item['address']))

# Output the Pool Table
print("\nPool Table:")
print("{:<15}".format("Pool Start Index"))
for index in pool_table:
    print("{:<15}".format(index))
