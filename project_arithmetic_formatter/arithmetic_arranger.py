def arithmetic_arranger(problems, display_answers=False):
    # Check at most 5 problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Create formatted versions of problems
    l_1 = []
    l_2 = []
    l_3 = []
    l_4 = []
    for p in problems:
        # Split problem into numbers and operator
        n_1, op, n_2 = p.split()
        # Check operator is + or -
        if not op in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        # Check numbers numeric
        if not (n_1.isnumeric() and n_2.isnumeric()):
            return "Error: Numbers must only contain digits."
        # Check numbers at most 4 digits
        if not (len(n_1) <= 4 and len(n_2) <= 4):
            return "Error: Numbers cannot be more than four digits."

        # Calculate operation results
        if op == "+":
            r = int(n_1) + int(n_2)
        elif op == "-":
            r = int(n_1) - int(n_2)

        # Find width of formatted problem
        w = max(len(n_1), len(n_2)) + 2
        # Format numbers as lines in the problem
        n_1 = n_1.rjust(w)
        n_2 = op + n_2.rjust(w - 1)
        r = str(r).rjust(w)
        # Create dash line
        dl = "-" * w

        # Append each line to list
        l_1.append(n_1)
        l_2.append(n_2)
        l_3.append(dl)
        l_4.append(r)

    # Join everything into arranged problems
    space = "    "
    arranged_problems = (
        space.join(l_1) + "\n" + space.join(l_2) + "\n" + space.join(l_3)
    )

    # Add answers conditional on input
    if display_answers:
        arranged_problems = arranged_problems + "\n" + space.join(l_4)

    return arranged_problems
