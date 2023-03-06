import os
import argparse
from midi2audio import FluidSynth

parser = argparse.ArgumentParser(description='soundfont')
parser.add_argument(
    '--sf',
    type=str,
    default='./sf/Arachno SoundFont - Version 1.0.sf2',
    help='Select a sound font.'
)
args = parser.parse_args()


def mkdir(outpath='./output'):
    if not os.path.exists(outpath):
        os.makedirs(outpath)


def render(midi_dir, audio_dir, sf):
    fs = FluidSynth(sound_font=sf)
    for _, _, filenames in os.walk(midi_dir):
        for filename in filenames:
            input = midi_dir + '/' + filename
            fontname = sf.replace("\\", "/").split('/')[-1][:-4]
            output = audio_dir + '/' + filename[:-4] + '(' + fontname + ').wav'
            mkdir(audio_dir)
            fs.midi_to_audio(input, output)


if __name__ == "__main__":
    render(midi_dir='./input', audio_dir='./output', sf=args.sf)
