import argparse

file_path = r'/Users/tonynekola/Desktop/Screen Shot 2023-01-19 at 0.25.21.png'


def parse_commandline_args():
    # Initialize parser
    parser = argparse.ArgumentParser(description='Print files')

    # Add arguments
    parser.add_argument('-file', '-f', help='path to file you would like print')

    return parser.parse_args()




def print_on_unix(file_to_print):
    print('printing of Unix system')
    import cups
    
    # Connect to the CUPS server
    conn = cups.Connection()

    # Find the printer
    printers = conn.getPrinters()
    printer_name = 'hp_printer'
    printer = printers[printer_name]

    # Print the file
    job_id = conn.printFile(printer_name, file_to_print, 'My Document', {})
    print('Print job submitted with ID:', job_id)

def print_on_windows(file_to_print):
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



def main():
    # Parse arguments
    args = parse_commandline_args()

    file_path = r'/Users/tonynekola/Desktop/report-2022-09-26_18-11-13.html'
    file_path = args.file

    print_on_unix(file_path)

if '__name__' == '__main__':
    print('Stating Print')
    main()
print('Stam')
