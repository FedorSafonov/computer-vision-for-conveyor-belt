<h1 align="left">Компьютерное зрение для фасовки пластикового мусора</a></h1>

* Полный отчёт по проекту можно посмотреть в [report.md](https://)
* [Ссылка на веб приложение](https://)

<h2 style="font-size: 20px;">Описание</h2>
Задача определения, классификации и отслеживание конкретных объектов (будь то люди в общественных местах, мигрирующие животные, дорожная обстановка, или прикассовый контроль в магазинах и др.), является одной из самых интересных и, одновременно, сложных задач в области современного компьютерного зрения. Одна из них, а именно детекция с трекингом, будет решена в данном проекте.



<h2 style="font-size: 20px;">Цель</h2>
IT-компания "Renue" из Екатеринбурга разрабатывает кастомную модель для отслеживания (детекция + трекинг) пластикового мусора на конвейере с дальнейшей передачей информации сортирующему роботу.
</br>Причем время работы модели над одним кадром не должно превышать 100 милисекунд.
</br>За основу собственной модели взята предобученная YOLOv10 c ее весами. 
</br>В качестве метрики используется MOTA (Multiple Object Tracking Accuracy).

<h2 style="font-size: 20px;">Исходные данные</h2>
Заказчиком предоставлены видео движущегося по конвейру мусора в формате .mp4, а также кадрирование на .img.

<h2 style="font-size: 20px;">Результаты</h2>
+  Данные размечены и преобразованы в нужный формат.
+  Детекции объектов (рамки bboxes) заменена сегментацией ("маска") для более точного выделения контура объектов.
+ 
+ 
+ 
+



## Используемые библиотеки
+ *OpenCV*
+ *ultralytics*
+ *pandas*
+ *YOLOv10*
+ *PyTorch*
+ *matplotlib*
+ *numpy*

