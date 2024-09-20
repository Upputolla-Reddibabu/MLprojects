import logging
import sys

# Setup logging configuration to see messages in console
logging.basicConfig(level=logging.ERROR)

# Custom exception handling in Python
def error_msg_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_msg = 'Error occurred in script: [{0}] at line number [{1}] with message: [{2}]'.format(
        file_name, line_number, str(error)
    )
    return error_msg

class CustomException(Exception):
    def __init__(self, error_msg, error_detail: sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_details(error_msg, error_detail=error_detail)

    def __str__(self) -> str:
        return self.error_msg

# if __name__ == "__main__":
#     try:
#         a = 1 / 0  # This will raise a ZeroDivisionError
#     except Exception as e:
#         logging.error('Division by zero error occurred.')
#         print("An error occurred")
        # raise CustomException(e, sys)  


# ctrl + k + c  -> to comment multiple lines in vscode
# ctrl + k + u
