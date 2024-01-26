import click
import os
from pydub import AudioSegment

@click.command()
@click.argument('input_files', nargs=-1, type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def join_audio(input_files, output_file):
    """
    Join multiple audio files.

    Example:
    python join.py audio1.wav audio2.wav audio3.wav out.wav
    """

    # Check if at least two input files are provided
    if len(input_files) < 2:
        click.echo("Error: Provide at least two input audio files to join.")
        return
    if os.path.exists(output_file):
        click.echo("Error: Output file exists.")
        return

    # Load audio segments from input files
    audio_segments = [AudioSegment.from_file(file) for file in input_files]

    # Concatenate audio segments
    joined_audio = sum(audio_segments)

    # Export the joined audio to the output file
    joined_audio.export(output_file, format="wav")

    click.echo(f"Audio files joined successfully. Output saved to {output_file}")

if __name__ == '__main__':
    join_audio()
