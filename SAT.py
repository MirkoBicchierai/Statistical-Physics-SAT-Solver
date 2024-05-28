def simplify_formula(formula, variable, value):
    new_formula = []
    for clause in formula:
        if value:  # variable is set to True
            if variable in clause:
                continue  # Clause is satisfied, remove it
            new_clause = [lit for lit in clause if lit != -variable]
        else:  # variable is set to False
            if -variable in clause:
                continue  # Clause is satisfied, remove it
            new_clause = [lit for lit in clause if lit != variable]

        if not new_clause and new_clause != clause:
            return None  # Clause becomes empty after simplification, unsatisfiable
        new_formula.append(new_clause)

    return new_formula


def backtrack(formula, variables, labeling, debug):
    if debug:
        print(f"Backtracking with formula: {formula}, variables: {variables}, labeling: {labeling}")

    if not formula:
        return labeling  # Satisfiable
    if any(not clause for clause in formula):
        return None  # Unsatisfiable

    # Choose an unassigned variable (heuristic can be improved)
    variable = variables[0]
    remaining_variables = variables[1:]

    # Try assigning True to the variable
    new_labeling = labeling.copy()
    new_labeling[variable] = True
    simplified_formula = simplify_formula(formula, variable, True)
    if debug:
        print(f"Trying variable {variable} = True, simplified formula: {simplified_formula}")
    if simplified_formula is not None:
        result = backtrack(simplified_formula, remaining_variables, new_labeling, debug)
        if result is not None:
            return result

    # Try assigning False to the variable
    new_labeling[variable] = False
    simplified_formula = simplify_formula(formula, variable, False)
    if debug:
        print(f"Trying variable {variable} = False, simplified formula: {simplified_formula}")
    if simplified_formula is not None:
        result = backtrack(simplified_formula, remaining_variables, new_labeling, debug)
        if result is not None:
            return result

    return None  # Unsatisfiable


def is_satisfiable(c, n, debug):
    variables = list(range(1, n + 1))
    labeling = {}
    return backtrack(c, variables, labeling, debug)
