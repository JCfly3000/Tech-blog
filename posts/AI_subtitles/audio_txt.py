import mlx_whisper
import argparse
from whisper.utils import get_writer


# Create the parser
parser = argparse.ArgumentParser(description="A simple example using argparse")


parser.add_argument('-n', '--name', type=str, help='Your name', required=True)

# Parse the arguments
args = parser.parse_args()

# Access the arguments
print(f"Hello, {args.name}!")




speech_file= args.name
# Using mlx-community/whisper-large-v3-turbo model
result = mlx_whisper.transcribe(speech_file, 
                                path_or_hf_repo="mlx-community/whisper-large-v3-turbo",
                                word_timestamps=True
                                )

srt_writer = get_writer("srt",'.')
srt_writer(result,'text.srt')

srt_writer = get_writer("txt",'.')
srt_writer(result,'text.txt')




