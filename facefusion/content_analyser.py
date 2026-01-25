from functools import lru_cache
from typing import Tuple

from facefusion import inference_manager
from facefusion.types import DownloadScope, DownloadSet, Fps, InferencePool, ModelSet, VisionFrame


@lru_cache()
def create_static_model_set(download_scope : DownloadScope) -> ModelSet:
	# NSFW models removed
	return {}


def get_inference_pool() -> InferencePool:
	# NSFW detection disabled - no models to load
	return {}


def clear_inference_pool() -> None:
	# NSFW detection disabled - no models to clear
	inference_manager.clear_inference_pool(__name__, [])


def collect_model_downloads() -> Tuple[DownloadSet, DownloadSet]:
	# NSFW detection disabled - no models to download
	return {}, {}


def pre_check() -> bool:
	# NSFW detection disabled - no models to check
	return True


def analyse_stream(vision_frame : VisionFrame, video_fps : Fps) -> bool:
	# NSFW detection disabled
	return False


def analyse_frame(vision_frame : VisionFrame) -> bool:
	# NSFW detection disabled
	return False


@lru_cache()
def analyse_image(image_path : str) -> bool:
	# NSFW detection disabled
	return False


@lru_cache()
def analyse_video(video_path : str, trim_frame_start : int, trim_frame_end : int) -> bool:
	# NSFW detection disabled
	return False
