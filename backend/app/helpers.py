import re
from typing import Optional, Tuple, Union


def parse_exact_range(range_str: str) -> Optional[Tuple[int, int]]:
    """Handles exact range formats like '1000-2000'."""
    match = re.fullmatch(r"(\d+)-(\d+)", range_str)
    return (int(match.group(1)), int(match.group(2))) if match else None


def parse_single_value(range_str: str) -> Optional[Tuple[int, int]]:
    """Handles single number inputs like '200' or '$1500'."""
    match = re.fullmatch(r"(\d+)", range_str)
    return (int(match.group(1)), int(match.group(1))) if match else None


def parse_less_than(range_str: str) -> Optional[Tuple[None, int]]:
    """Handles '<2000' inputs."""
    match = re.fullmatch(r"<(\d+)", range_str)
    return (None, int(match.group(1))) if match else None


def parse_greater_than(range_str: str) -> Optional[Tuple[int, None]]:
    """Handles '>500' inputs."""
    match = re.fullmatch(r">(\d+)", range_str)
    return (int(match.group(1)), None) if match else None


def parse_range_or_value(
    range_str: Optional[Union[str, int]]
) -> Optional[Tuple[Optional[int], Optional[int]]]:
    """
    Parses a price range input (int or str) into a tuple (min, max).

    Handles:
    - Integers: `200` → (200, 200)
    - Standard ranges: `"£1000-£2000"` → (1000, 2000)
    - Single numbers: `"200"` → (200, 200)
    - Less than: `"<$2000"` → (None, 2000)
    - Greater than: `">$500"` → (500, None)

    Returns:
    - `(min, max)`: Tuple of integers where min or max can be `None`.
    - `None` if parsing fails.
    """
    if isinstance(range_str, int):
        return (range_str, range_str)  # If it's an integer, treat it as min=max

    if not isinstance(range_str, str) or not range_str.strip():
        return None  # Invalid input

    # Clean input: Remove currency symbols & non-numeric characters (except '<', '>', '-')
    cleaned_str: str = re.sub(r"[^\d\-\<\>]", "", range_str.strip())

    # Try each parsing function
    return (
        parse_exact_range(cleaned_str)
        or parse_single_value(cleaned_str)
        or parse_less_than(cleaned_str)
        or parse_greater_than(cleaned_str)
        or None  # If nothing matches
    )
