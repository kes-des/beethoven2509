from.validator import validator_data
def process_data(data):
    if(not validator_data(data)):
        return f'Processed Data:{data}'
    return 'Invalid Data'