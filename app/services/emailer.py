from enum import Enum
from typing import Optional


class EmailFormatEnum(str, Enum):
    first_last = "first_last"                      # aryanraj
    first_period_last = "first_period_last"        # aryan.raj
    first_initial_last = "first_initial_last"      # araj
    first_initial_period_last = "first_initial_period_last"  # a.raj
    first_last_initial = "first_last_initial"      # aryanr
    first_period_last_initial = "first_period_last_initial"  # aryan.r
    first_initial_last_initial = "first_initial_last_initial"  # ar
    last_first = "last_first"                      # rajaryan
    last_first_initial = "last_first_initial"      # raja


def create_email(chunk: dict, company_name: str, custom_address: Optional[str] = None, email_format: str = "first_last") -> str:
    first = chunk.get("first_name", "").lower()
    middle = chunk.get("middle_name", "").lower()
    last = chunk.get("last_name", "").lower()

    # Extract initials
    f_i = first[0] if first else ""
    m_i = middle[0] if middle else ""
    l_i = last[0] if last else ""

    local_part = ""

    match email_format:
        case EmailFormatEnum.first_last:
            local_part = f"{first}{last}"
        case EmailFormatEnum.first_period_last:
            local_part = f"{first}.{last}"
        case EmailFormatEnum.first_initial_last:
            local_part = f"{f_i}{last}"
        case EmailFormatEnum.first_initial_period_last:
            local_part = f"{f_i}.{last}"
        case EmailFormatEnum.first_last_initial:
            local_part = f"{first}{l_i}"
        case EmailFormatEnum.first_period_last_initial:
            local_part = f"{first}.{l_i}"
        case EmailFormatEnum.first_initial_last_initial:
            local_part = f"{f_i}{l_i}" if f_i and l_i else f"{f_i or l_i}"
        case EmailFormatEnum.last_first:
            local_part = f"{last}{first}"
        case EmailFormatEnum.last_first_initial:
            local_part = f"{last}{f_i}"
        case _:
            local_part = f"{first}.{last}"  # fallback to common format

    domain = custom_address if custom_address else company_name.replace(" ", "").lower() + ".com"
    email = f"{local_part}@{domain}"
    return email
