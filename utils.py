
import glob


def get_excel_sheet_path():
    excel_sheets = glob.glob(f"./*.xlsx")
    if len(excel_sheets) == 0:
        raise FileNotFoundError("Arquivo de excel inexistente!")
    return excel_sheets[0]


def filter_files_format(files, file_formats):
    return list(filter(lambda file: True if file.split(".")[::-1][0] in file_formats else False, files))



