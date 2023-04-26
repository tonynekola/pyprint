import argparse
import platform
import mimetypes
import subprocess
import os
import time
import fitz
#file_path = r'/Users/tonynekola/Desktop/Screen Shot 2023-01-19 at 0.25.21.png'


def parse_commandline_args():
    # Initialize parser
    parser = argparse.ArgumentParser(description='Print files')

    # Add arguments
    parser.add_argument('-file', '-f', help='path to file you would like print')
    parser.add_argument('-printer', '-p', help='name of the printer')

    return parser.parse_args()


def print_on_unix(printer_name,file_to_print):
    print('Printing of Unix system')
    import cups
    
    # Set print options (optional)
    options = {
        "PageSize": "A4",
        "Duplex": "DuplexNoTumble",
    }
    # Connect to the CUPS server
    conn = cups.Connection()

    # Find the printer
    printers = conn.getPrinters()


    printer = printers.get(printer_name,None)

    if printer is None:
        print('selected printer was not found!')
        return 0

    # Print the file
    # job_id = conn.printFile(printer_name, file_to_print, 'My Document', options)
    file_type, encoding = mimetypes.guess_type(file_to_print)
    # print(file_type)
    # print(encoding)
    # print(printer)
    
    if 'wordprocess' in file_type or '.docx' in file_to_print:
        print('file type not supported')
        return 1
        # pdf_file_path = os.path.splitext(file_to_print)[0] + ".html"
        # converter = subprocess.run(["textutil", "-convert", "html",file_to_print,'-output',pdf_file_path], capture_output=True, text=True)
        # time.sleep(3)
        # with open(pdf_file_path, 'r') as file:
        #     html_data = file.read()

        # ps_data = conn.convertFile(printer_name, html_data, 'texttops')
        # job_id = conn.printFile(printer_name, ps_data, "My Document", options)

    elif file_type == 'application/pdf':
        # print the PDF file directly
        job_id = conn.printFile(printer_name, file_to_print, "My Document",{})
    else:
        # set the contentType argument appropriately for text files
        job_id = conn.printFile(printer_name, file_to_print, "".encode('utf-8'),options)


    print('Print job submitted with ID:', job_id)

def print_on_windows(file_to_print):
    print('Printing of Windows system')

    import win32print

    # Open the file for printing
    with open(file_to_print, "rb") as f:
        # Get the default printer name
        default_printer = win32print.GetDefaultPrinter()

        # Open the printer
        printer_handle = win32print.OpenPrinter(default_printer)

        # Start a print job
        job_info = win32print.StartDocPrinter(printer_handle, 1, ("print job", None, "RAW"))
        win32print.StartPagePrinter(printer_handle)

        # Send the file contents to the printer
        file_contents = f.read()
        win32print.WritePrinter(printer_handle, file_contents)

        # End the print job
        win32print.EndPagePrinter(printer_handle)
        win32print.EndDocPrinter(printer_handle)
        win32print.ClosePrinter(printer_handle)


def print_file(printer_name,path_to_file):
    print(printer_name)
    print(path_to_file)
    if platform.system() == "Windows":
        print_on_windows(printer_name,path_to_file)
    else:
        print_on_unix(printer_name,path_to_file)

def main():
    # Parse arguments
    args = parse_commandline_args()
    
    file_path = args.file
    printer = args.printer

    if file_path is None or len(file_path) == 0:
        print('Specify file to print')
        return 0
    if printer is None or len(printer) == 0:
        print('Specify printer to use')
        return 0

    print(f'Printing file {file_path}')
    print_file(printer,file_path)
    print(f'File sent to printer.')

if '__name__' == '__main__':
    main()
