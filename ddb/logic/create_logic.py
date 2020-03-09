from files_handler.files_handler import FilesHandler
from logic.query_logic import QueryLogic
from typing import List


class CreateLogic(QueryLogic):                                              # dziedziczy po klasie QueryLogic
    def control(self, document_name, cols: List[str], values: List[str]):   # typo fixed
        fh = FilesHandler()
        fh.create_file_and_write(f"{document_name}.ddo", ','.join(cols))
