from datetime import datetime
from openpyxl import Workbook
from .models import Suggestions


def create_excel(suggestions):
    wb = Workbook()
    ws = wb.active

    for column, field in enumerate(Suggestions._meta.fields, start=1):
        ws.cell(row=1, column=column).value = field.name

    for suggestion in suggestions.values_list():
        sug = []
        for value in suggestion:
            if isinstance(value, datetime):
                value = value.replace(tzinfo=None)
            sug.append(value)
        ws.append(sug)

    return wb
