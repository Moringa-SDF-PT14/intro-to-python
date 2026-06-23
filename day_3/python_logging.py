import logging

# configure logs for your app
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app_metrics.log"),
        logging.StreamHandler(),
    ]
)

def large_log(fxn_log):
    for i in [0]*100:
        fxn_log()
    pass

def process_payment(amount):
    if amount <= 0:
        large_log( lambda: logging.error(f"Invalid payment attempt for amount: {amount}") )
        return False
    
    large_log(lambda: logging.info(f"Successfully paid ${amount}"))
    return True

process_payment(10)
process_payment(-1)
