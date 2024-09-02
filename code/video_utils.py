import cv2
import time
from ultralytics.utils import ops
from ultralytics.utils.plotting import Annotator

from annotation_utils import draw_tracking_info

def initialize_video_writer(cap, output_path):
    """
    Инициализирует объект для записи видео.

    Args:
        cap (cv2.VideoCapture): Объект для захвата видео.
        output_path (str): Путь для сохранения видео.

    Returns:
        cv2.VideoWriter: Объект для записи видео.
    """
    w, h = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    return cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

def process_frame(frame, model, config, tracking_history, annotations, frame_index):
    """Обрабатывает один кадр видео, выполняет трекинг объектов и добавляет аннотации.

    Args:
        frame (np.ndarray): Видеокадр.
        model (YOLO): Модель YOLO для трекинга объектов.
        config (dict): Конфигурационные параметры.
        tracking_history (defaultdict): История трекинга объектов.
        annotations (defaultdict): Аннотации для сохранения.
        frame_index (int): Индекс текущего кадра.

    Returns:
        Annotator: Объект Annotator для дальнейшей работы с аннотациями на кадре.
        int: Время обработки кадра в миллисекундах.
    """
    start_time = time.time()
    annotator = Annotator(frame, line_width=2) if config.save_video else None

    tracking_results = model.track(frame, half=True, verbose=False, persist=True, 
                                   tracker=f'{config.tracker}.yaml')[0]
    
    if tracking_results.boxes.id is not None:
        bounding_boxes = tracking_results.boxes.xyxy
        object_ids = tracking_results.boxes.id.int().cpu().tolist()
        class_ids = tracking_results.boxes.cls.int().cpu().tolist()

        for bbox, object_id, class_id in zip(bounding_boxes, object_ids, class_ids):
            center_x, center_y, *_ = ops.xyxy2xywh(bbox).int().tolist()
            tracking_history[object_id].append((center_x, center_y))

            if config.save_annotations:
                annotations[frame_index].append({
                    'object_id': object_id,
                    'bbox_xyxy': bbox.tolist(),
                    'class_id': class_id
                })

            if config.save_video:
                draw_tracking_info(annotator, object_id, bbox, tracking_results.names[class_id], tracking_history)

    processing_time_ms = int(1000 * (time.time() - start_time))
    return annotator, processing_time_ms