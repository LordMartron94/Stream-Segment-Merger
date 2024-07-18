import os

# ==== FOR THE DEVS ====
# Leave as is, unless you really know what you are doing!

DEBUGGING: bool = False
PROJECT_ROOT: str = os.path.dirname(os.path.abspath(__file__))
CACHE_PATH: str = os.path.join(PROJECT_ROOT, "CACHE")

# ===== CONFIG =====

SHOW_MERGE_COMMANDS = True  # Output merge progress and command :)
MIN_SEGMENT_AGE_FOR_MERGE = 24  # Minimal age of a segment before it is processed into merging (in hours).
				   # This setting can help to prevent streams merging while not all segments are in the directory yet.
				   # Set to 0 to disable.
MIN_SEGMENT_AGE_FOR_POST_PROCESS = 16  # Minimal age of a video before it is deemed old enough to post-process in hours (remux, rename, move to postprocessed, etc.).
									   # Set to 0 to disable.

MODEL_SORTING_ALGORITHM = "${oldest}"  # The algorithm with which the processor determines in what order to process models.
									   # Very useful to make sure that every model gets processed in time, no matter the number of models.
									   # Default: ${oldest}, others: ${alphabetical}, ${alphabetical_reversed}

# ---- PATHS ----
DATA_STREAM_PATH: str = "Y:/Media Library/Porn/Porn Utilities/The Adult Flow Processor/linux/CACHE/data_stream.txt"

ORIGINAL_LOCATION_PATH_RAW: str = "Z:/3. Personal/__Media/Porn Cache/1. Recording"
ORIGINAL_LOCATION_PATH: str = "Z:/3. Personal/__Media/Porn Cache/2. Recordings Triage"
# FINAL_DESTINATION_ROOT: str = "/mnt/nas/5TB WD External/Media Library/Porn/Utility Tests/"  # Test version, leave commented!
FINAL_DESTINATION_ROOT: str = "V:/Media Library/Porn/VIDEO"

FINAL_DIRECTORY_STRUCTURE: str = "Streaming (Cam4, Stripchat, etc.)/${model_name}/${year}/${month}/${day}"
MERGE_NAME_TEMPLATE: str = "${model_name}, START ${start_date}, END ${end_date}"
LOOSE_SEGMENT_TEMPLATE: str = "${model_name}, START ${start_date}, END ${end_date}"  # Template for loose segments (those that are deemed their own stream and are not merged). 
																					 # Leave empty to disable renaming.

# ---- VIDEO HANDLING ----
MERGED_VIDEO_EXTENSION: str = ".mp4"
MAX_DIFFERENCE_BETWEEN_SEGMENTS = 400  # Difference between segments in seconds before a segment is decided to be a loose segment (a stream on its own).

SHEET = True  # Whether to create a contact sheet for merged files.
BURN = True  # Whether to burn the timestamps into the contact sheet.
DELETE = True  # Whether to delete the original segments after merging the file.
REGEN_SHEETS = True  # Whether to regenerate contact sheets for moved videos.

DELETE_CORRUPT_VIDEOS = True  # Whether to delete videos that are deemed corrupt by ffmpeg.
