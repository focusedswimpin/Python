from PySimpleGUI import Window, Text, InputText, FilesBrowse, FolderBrowse, Button, WINDOW_CLOSED, Column
from zipCreator import make_archive

sourceText = Text('Select files to compress: ')
sourceInputText = InputText(key='sourceInputText')
sourceButton = FilesBrowse('Select files', key='sourceButton')

destinationText = Text('Select destination folder: ')
destinationInputText = InputText(key='destinationInputText')
destinationButton = FolderBrowse('Select directory', key='destinationButton')

compressButton = Button('Compress')

successMessageText = Text(key='successMessageText', text_color='green')

textColumn = Column([[sourceText], [destinationText]])
inputTextColumn = Column([[sourceInputText], [destinationInputText]])
buttonColumn = Column([[sourceButton], [destinationButton]])

window = Window(
    'Compress to zip files',
    layout=[
        [textColumn, inputTextColumn, buttonColumn],
        [compressButton, successMessageText]
    ],
    font=('Helvetica', 20)
)

while True:
    event, values = window.read()
    print('event', event)
    print('values', values)

    if event == WINDOW_CLOSED:
        break

    sourceFilePaths = values['sourceInputText'].split(';')
    destinationFilePaths = values['destinationInputText']

    make_archive(sourceFilePaths, destinationFilePaths)

    window['successMessageText'].update(value='Successfully compressed files!')

window.close()
