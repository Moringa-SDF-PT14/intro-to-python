def clean_email(email):
    """
    Extracts unnecessary data from email
    Example: ABc@gmail.com => abc@gmail.com
    """
    return email.strip().lower()