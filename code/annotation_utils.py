import cv2
from ultralytics.utils.plotting import colors

def draw_tracking_info(annotator, object_id, box_coords, class_name, track_history):
    """
    Рисует информацию о трекинге на кадре.

    Args:
        annotator (Annotator): Объект для аннотации изображения.
        object_id (int): Идентификатор объекта.
        box_coords (list): Координаты бокса объекта.
        class_name (str): Имя класса объекта.
        track_history (dict): Словарь с информацией об объектах.
    """
    color = colors(object_id, True)

    annotator.box_label(box=box_coords, 
                        color=color, 
                        label=f'id: {object_id}, class: {class_name}', 
                        txt_color=annotator.get_txt_color(color))
    for j in range(1, len(track_history[object_id])):
        cv2.line(annotator.im, 
                 track_history[object_id][j - 1],
                 track_history[object_id][j], 
                 color=color, 
                 thickness=2)