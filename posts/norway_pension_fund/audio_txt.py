import mlx_whisper
from whisper.utils import get_writer
speech_file="output.mp3"
# Using mlx-community/whisper-large-v3-turbo model
result = mlx_whisper.transcribe(speech_file, 
                                path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
                                word_timestamps=True
                                )

srt_writer = get_writer("srt",'.')
srt_writer(result,'text.srt')

srt_writer = get_writer("txt",'.')
srt_writer(result,'text.txt')




