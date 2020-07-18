import datetime
import csv
import json

from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage
from time import time

# Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость)
# Создать doc шаблон, где будут использованы данные параметры
# Автоматически сгенерировать отчет о машине в формате doc

launch = time()


def get_context(brand, model, consumption, color, transmission, price):
    return {
        'auto': brand,
        'model_auto': model,
        'fuel_consumption': consumption,
        'color_auto': color,
        'transmission_auto': transmission,
        'price_auto': price,
    }


def from_template(brand, model, consumption, color, transmission, price, template, signature):
    template = DocxTemplate(template)
    context = get_context(brand, model, consumption, color, transmission, price)

    img_size = Cm(15)
    view = InlineImage(template, signature, img_size)

    context['view'] = view
    template.render(context)

    template.save(brand + '_' + str(datetime.datetime.now().date()) + '_report.docx')


def generate_report(brand, model, consumption, color, transmission, price):
    template = 'report.docx'
    signature = 'view.png'
    document = from_template(brand, model, consumption, color, transmission, price, template, signature)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


generate_report('Audi', 'Q8', 7.8, 'Black', 'Automatic', 6800000)

finish = time()
generation_time = finish - launch
print('Время генерации отчета в формате doc:', toFixed(generation_time, 4))

# Создать csv файл с данными о машине

launch = time()

car_data = [['auto', 'model', 'fuel_consumption', 'color', 'transmission', 'price'],
            ['Audi', 'Q8', 7.8, 'Black', 'Automatic', 6800000]]

with open('auto.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(car_data)

finish = time()
generation_time = finish - launch
print('Время генерации отчета в формате csv:', toFixed(generation_time, 5))

# Создать json файл с данными о машине

launch = time()

characteristics = {'auto': 'Audi', 'model': 'Q8', 'fuel_consumption': 7.8, 'color': 'Black',
                   'transmission': 'Automatic', 'price': 6800000}

with open('auto.json', 'w') as f:
    json.dump(characteristics, f)

finish = time()
generation_time = finish - launch
print('Время генерации отчета в формате json:', toFixed(generation_time, 5))

