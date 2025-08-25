from processor import process_input
import uuid

if __name__ == "__main__":
    test_inputs = ["123", "abc", "", None, "42x"]

    for i, input_value in enumerate(test_inputs, start=1):
        request_id = f"REQ-{uuid.uuid4()}"
        process_input(input_value, request_id)
