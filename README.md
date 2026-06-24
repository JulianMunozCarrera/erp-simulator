# ERP Simulator

A small Python project that simulates EEG event-related potentials (ERPs) to show why
researchers average across many trials to pull a brain signal out of noise.

I built this while learning Python, and partly to better understand the kind of data
worked with in the Linguistic Neurodiversity Lab at Carleton, where I'm helping out on
an EEG study. The data here is completely synthetic — I generate it myself — so it's a
teaching tool, not real research data.

## The idea

When you record EEG, the brain's actual response to an event (like reading a word) is
tiny and buried under a lot of unrelated electrical noise. A single trial looks almost
like pure noise. The trick researchers use is to repeat the same kind of event many
times and average all the recordings together. The real response shows up in the same
place every time, so it survives averaging, while the random noise mostly cancels out.

This project fakes that whole process so you can see it happen.

Two specific responses are simulated:

- **N400** — a negative dip that, in real EEG, appears around 400 ms after a word that
  doesn't fit the meaning of a sentence (e.g. "I take my coffee with cream and socks").
- **P600** — a positive bump that appears around 600 ms after a grammatical error
  (e.g. "The cat eat the food").

The names come from the direction (N = negative, P = positive) and roughly when they
happen in milliseconds.

## What the code does

1. `generate_trial(condition)` — builds one fake trial: 1000 points of random noise with
   a bump added in the right time window depending on the condition.
2. `generate_trials(condition, n_trials)` — calls the above many times and stacks the
   results into a `(n_trials, 1000)` array.
3. The script then generates 50 trials each for N400 and P600, averages across trials
   (`np.mean(data, axis=0)`), and plots the two clean averages together.

The averaged plot is saved as `erp_plot.png`.

## Running it

```bash
pip3 install numpy matplotlib
python3 erp_simulator.py
```

Close each plot window that pops up to let the script continue.

## What I took away from it

The main thing this made concrete for me was *why* trial averaging works — that the
signal is consistent across trials and the noise isn't, so averaging keeps one and kills
the other. Seeing the single noisy trial next to the clean 50-trial average made that
click in a way reading about it didn't.

## Built with

- Python
- NumPy
- matplotlib
