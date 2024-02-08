from pathlib import Path
import pprint
import time
from typing import List

from constants import FINAL_DESTINATION_ROOT, ORIGINAL_LOCATION_PATH
from common.handlers.file_parser import FileParser
from common.handlers.file_handler import FileHandler
from src.stream_merger import StreamMerger
from src.segment_mover import SegmentMover
from src.segment_organizer import SegmentOrganizer
from src.ffmpeg_handling.ffmpeg_api import FFMPEGAPI
from common.time_format import TimeFormat
from common.time_utils import TimeUtils
from src.video_handler import VideoHandler


class ModelProcessor:
	"""
	A class that handles the processing of each model (folder).
	"""

	def __init__(self) -> None:
		_api: FFMPEGAPI = FFMPEGAPI()
		_video_handler: VideoHandler = VideoHandler()
		_file_parser: FileParser = FileParser()
		_file_handler: FileHandler = FileHandler()

		self._time_utils: TimeUtils = TimeUtils()
		self._segment_mover: SegmentMover = SegmentMover(_video_handler)
		self._segment_organizer: SegmentOrganizer = SegmentOrganizer(_file_parser, _video_handler, _file_handler)
		self._stream_merger: StreamMerger = StreamMerger(_api, _video_handler, _file_parser, self._move_to_loose_segments)

	def _move_to_loose_segments(self, segments: List[Path], loose_segment_directory_path: Path):
		for segment in segments:
			self._segment_mover.move(segment, loose_segment_directory_path)

	def _print_time_passed(self, start_time: float, end_time: float, model_name: str):
		elapsed_time = end_time - start_time
		formatted = self._time_utils.format_time(elapsed_time, TimeFormat.Dynamic)

		print(" ")
		print(f"It took {formatted} to merge all possible segments for model {model_name}.")    
		print(" ")
		print("=====================================")
		print(" ")

	def merge_model_streams(self, model_name: str, make_sprite_sheet: bool, burn_timestamps_in_sheet: bool, delete_original_files: bool):
		start_time = time.time()
		
		segment_directory: Path = Path(ORIGINAL_LOCATION_PATH, model_name)
		organized_segments: List[Path] = self._segment_organizer.organize(segment_directory)

		if len(organized_segments) < 1:
			end_time = time.time()
			self._print_time_passed(start_time, end_time, model_name)
			return

		pprint.pp(organized_segments)

		# exit()

		for stream in organized_segments:
			if len(stream) > 1:
				self._stream_merger.merge_stream(stream, model_name, make_sprite_sheet, burn_timestamps_in_sheet, delete_original_files)
			else:
				self._move_to_loose_segments(stream, Path(FINAL_DESTINATION_ROOT, model_name, "Loose Segments"))

		end_time = time.time()
		self._print_time_passed(start_time, end_time, model_name)
