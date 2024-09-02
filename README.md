<h1 align="left">Детекция и трекинг мусора на ленте конвейера</a></h1>

![click here](demo.gif)

* [Ссылка на отчет](https://github.com/FedorSafonov/computer-vision-for-conveyor-belt/blob/report.md/report.md)
* [Ссылка на презентацию](https://github.com/FedorSafonov/computer-vision-for-conveyor-belt/tree/presentation)

<h2 style="font-size: 20px;">Описание</h2>
В данном проекте команда дата-саентистов выполняет заказ для российской IT-компания "Renue" по разработке решения для отслеживания и последующей сортировки пластикового мусора на конвейерной ленте.
</br>Данная задача выполняется с помощью технологий компьютерного зрения.

<h2 style="font-size: 20px;">Цель</h2>
Целью проекта является разработать модель компьютерного зрения, которая будет далее применяться сортирующим роботом на мусороперерабатывающем заводе.
</br>Причем время работы модели над одним кадром не должно превышать 100 милисекунд.
</br>За основу модели взята предобученная YOLOv10 c ее весами и присоединен трекинг BotSORT. 
</br>В качестве метрики используется MOTA (Multiple Object Tracking Accuracy).

<h2 style="font-size: 20px;">Исходные данные</h2>
Заказчиком предоставлена предобученная модель Ultralyticks для детекции пластиковых бутылок, а также датасет (изображения + разметка) в нескольких форматах: MOT, COCO, CVAT.
</br>Даны также образцы видеозаписи работы конвейера.

<h2 style="font-size: 20px;">Результаты</h2>
В результате построена модель, которая выполняет свою работу с точностью (MOTA=0.794) и скоростью 35 мс.
</br>А также проведена исcледовательская работа и с другими моделями компьютерного зрения.

<h2 style="font-size: 20px;">Инструкция по использованию модели</h2>

**Для запуска трекинга используйте следующую bash-команду:**
```python
python track.py --config_filename config.yaml
```

</br>**Пример файла конфигурации `config.yaml`:**
```python
paths:
root: Хакатон-Сортировка ТБО
yolo_model: Models/ultralytics/yolov10x_v2_4_best.pt
input_video: Videos/input.mp4
output_video: Videos/output.mp4
output_annotations: Datasets/annotations.json
tracker: bytetrack
save_video: False
save_annotations: True
```

</br>**Параметры конфигурации:**
```
paths.root - корневая директория для всех путей.
paths.yolo
_
model - путь к модели YOLO.
paths.input
video - путь к входному видеофайлу.
paths.output
_
video - путь для сохранения выходного видео.
paths.output
_
annotations - путь для сохранения аннотаций.
tracker - тип используемого трекера (поддерживаются `botsort` и `bytetrack`).
save
_
video - флаг для сохранения выходного видео (`True` или `False`).
save
_
annotations - флаг для сохранения аннотаций (`True` или `False`).
```


<h2 style="font-size: 20px;">Структура репозитория:</h2>

```
**code** - содержит основной код для запуска и инференса модели.
**presentation** - cодержит презентацию проекта в формате .pptx.
```

<h2 style="font-size: 20px;">Разработчики</h2>

* [Фёдор Сафонов](https://) - тимлид 
* [Илья Гурин](https://github.com/IlyaLion) 
* [Дмитрий Ерыганов](https://github.com/Dnevvs)  
* [Дина Гребенкина](https://github.com/DinaGreb) 
* [Алексей Исаков](https://github.com/IT-DS-Alex) 
* [Екатерина Богданович](https://github.com/Kate_B_DS) 

## Стек технологий
+ *OpenCV*
+ *Ultralytics*
+ *PyTorch*
+ *numpy*

