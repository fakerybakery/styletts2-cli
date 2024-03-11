[Original Repo](https://github.com/yl4579/StyleTTS2) - **CLI Tool** - [Streaming API](https://github.com/neuralVox/styletts2)

# Usage

## Join Audio CLI

```bash
python join.py audio1.wav audio2.mp3 audio3.mp4 audio4.ogg output.mp3
```

## Inference CLI

Docs:
```
StyleTTS 2 CLI Inference
Usage: cli.py [OPTIONS] TEXT OUTPUT

Options:
  -a, --audio-sample PATH  [required]
  -p, --pth-path PATH      [required]
  -f, --file BOOLEAN       Read from input text from file  [default: False]
  --help                   Show this message and exit.
```

Inference:
```bash
python cli.py "Hello, this is a test" -a 1.wav -p model.pth
```

Inference from a file:
```bash
python cli.py file.txt -a 1.wav -p model.pth -f
```

## License

GPL due to Phonemizer (soon to be permissively licensed as soon as I find a permissively-licensed Phonemizer replacement)
