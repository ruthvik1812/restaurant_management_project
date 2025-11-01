# home/utils/validation_utils.py

import logging
from email_validator import validate_email, EmailNotValidError

# Configure logging (optional, good for debugging)
logger = logging.getLogger(__name__)

def is_valid_email(email: str) -> bool:
    """
    Validate an email address using the `email_validator` package.
    Returns True if valid, False otherwise.
    """
    try:
        # Validate and normalize the email
        validate_email(email)
        return True
    except EmailNotValidError as e:
        # Log the error for debugging
        logger.warning(f"Invalid email '{email}': {e}")
        return False
