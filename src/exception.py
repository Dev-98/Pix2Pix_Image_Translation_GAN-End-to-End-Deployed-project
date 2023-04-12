import sys #to manipulate different part of python runtime environment 

def error_message_detail(error,error_detail:sys):

    # Extracting the error/exception message form every aspect of your system
    _,_n,exc_tb= error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error encountered in the python script name [{file_name}] line number: [{exc_tb.tb_lineno}] error message [{str(error)}]"

    return error_message

class CustomException(Exception):

    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)


    def __str__(self) :
        return self.error_message