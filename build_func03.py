def main(n):
    """A integer type variable 'n' is given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func03

    Args:
        n (float): float

    Returns:
        float: the value of the expression
    """
    n=3.5
    result= pow(3*(n+1)**2)
    return float(result)