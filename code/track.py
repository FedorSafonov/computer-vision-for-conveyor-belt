import argparse
import cv2
from collections import defaultdict
import json
import numpy as np
import os
import time
from tqdm import tqdm
from ultralytics import YOLO
from ultralytics.utils import ops
from ultralytics.utils.plotting import Annotator

from config import get_config
from video_utils import initialize_video_writer, process_frame


def parse_arguments():
    """Парсит аргументы командной строки для получения имени файла конфигурации."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_filename', 
                        help='Путь к файлу конфигурации',
                        default='config.yaml')
    return parser.parse_args()

def process_video(video_capture, model, config):
    """Обрабатывает видео кадр за кадром, выполняя трекинг объектов и сохраняя результаты.

    Args:
        video_capture (cv2.VideoCapture): Захват видеофайла.
        model (YOLO): Загруженная модель YOLO.
        config (dict): Конфигурационные параметры.
    """
    annotations = defaultdict(list)
    tracking_history = defaultdict(list)
    frame_processing_times = []

    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    
    for frame_index in tqdm(range(total_frames)):
        ret, frame = video_capture.read()
        if not ret:
            print("Видео завершено или кадр не был считан.")
            break

        annotator, frame_processing_time = process_frame(frame, model, config, tracking_history, annotations, frame_index)

        if frame_index > 0 and config.save_video:
            frame_processing_times.append(frame_processing_time)
            process_performance_metrics(annotator, frame_processing_times)

        if config.save_video:
            config.video_writer.write(frame)

    if config.save_annotations:
        annotations_file_path = os.path.join(config.paths.root, config.paths.output_annotations)
        with open(annotations_file_path, 'w') as annotations_file:
            json.dump(annotations, annotations_file)

def process_performance_metrics(annotator, frame_processing_times):
    """Выводит на кадр информацию о производительности обработки.

    Args:
        annotator (Annotator): Объект для нанесения аннотаций на кадр.
        frame_processing_times (list): Список времен обработки кадров.
    """
    annotator.text((30, 30), text=f"Frame processing time:         {int(frame_processing_times[-1]):3d} ms")
    annotator.text((30, 60), text=f"Frame processing time (max):  {int(np.max(frame_processing_times)):3d} ms")
    annotator.text((30, 90), text=f"Frame processing time (mean): {int(np.mean(frame_processing_times)):3d} ms")
    annotator.text((30, 120), text=f"Frame processing time (std):   {int(np.std(frame_processing_times)):3d} ms")


def main():
    """Основная функция программы."""
    args = parse_arguments()
    config = get_config(args.config_filename)

    yolo_model_path = os.path.join(config.paths.root, config.paths.yolo_model)
    model = YOLO(yolo_model_path)

    input_video_path = os.path.join(config.paths.root, config.paths.input_video)
    video_capture = cv2.VideoCapture(input_video_path)

    if config.save_video:
        output_video_path = os.path.join(config.paths.root, config.paths.output_video)
        config.video_writer = initialize_video_writer(video_capture, output_video_path)

    process_video(video_capture, model, config)

if __name__ == '__main__':
    main()