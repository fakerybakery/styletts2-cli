print("StyleTTS 2 CLI Inference")

with open('../sentences.txt', 'r') as file:
    sentences = file.read().strip().splitlines()
print("Importing modules...")
import msinference
from pydub import AudioSegment
from txtsplit import txtsplit
from tqdm import tqdm
import numpy as np
import scipy
from nltk.tokenize import word_tokenize
msinference.init(pth_path)
print("Computing Style")
s_ref = msinference.compute_style(audio_sample)
print("Done Computing Style")

ps = msinference.global_phonemizer.phonemize([text])
ps = word_tokenize(ps[0])
ps = ' '.join(ps)
ps = ps.replace('``', '"')
ps = ps.replace("''", '"')

sentences = txtsplit(ps)
wavs = []
s_prev = None
for text in sentences:
    if text.strip() == "": continue
    # wav, s_prev = msinference.LFinference(text, s_prev, s_ref, alpha = 0.5, beta = 0.9, t = 0.7, diffusion_steps=10, embedding_scale=2.5)
    wav, s_prev = msinference.LFinference(text, s_prev, s_ref, alpha=0.5, beta=0.9, diffusion_steps=10)
    wavs.append(wav)

scipy.io.wavfile.write(output, 24000, np.concatenate(wavs))