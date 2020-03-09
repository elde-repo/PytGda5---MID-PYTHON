from files_handler.files_handler import FilesHandler


class CreateLogic:
    def controll(self, document_name, cols, vals):
        fh = FilesHandler()
        fh.create_file_and_write(f"{document_name}.ddo", ','.join(cols))
