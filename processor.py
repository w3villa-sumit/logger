from logger import log
import uuid

def process_input(user_input, request_id):
    try:
        if user_input is None or str(user_input).strip() == "" or not str(user_input).isdigit():
            raise ValueError("Invalid input. Must be a number.")

        number = int(user_input)
        log("INFO", request_id, user_input, message="Input processed successfully")
        return number

    except Exception as e:
        log("ERROR", request_id, user_input, error=str(e))
        print("Oops! That wasn’t a valid number. Please try again.")
