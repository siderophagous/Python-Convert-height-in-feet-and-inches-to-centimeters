# Constants
FT = 30.48  # cm
IN = 2.54   # cm


def convert_in_to_cm(x: float) -> float:
    """
    Converts x variable (represents data in inches) to centimeters.
    Returns a float.
    """
    return x * IN


def convert_ft_to_cm(x: float) -> float:
    """
    Converts x variable (represents data in feet) to centimeters.
    Returns a float.
    """
    return x * FT


# if file is run from a command-line:
if __name__ == "__main__":
    in_to_cm = convert_in_to_cm(5)  # expected result is 12.7 cm
    ft_to_cm = convert_ft_to_cm(12)  # expected result is 365.76

    print(f"{in_to_cm} cm")
    print(f"{ft_to_cm} cm")
