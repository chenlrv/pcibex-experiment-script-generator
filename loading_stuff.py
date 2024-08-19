def load_scripts():
    with open('RSVP_fixed_point.txt', 'r') as f:
        rsvp_fixed_script = f.read()
    with open('SPR_moving_window.txt', 'r') as f:
        spr_moving_script = f.read()
    with open('rsvp_moving_window.txt', 'r') as f:
        rsvp_moving_window = f.read()
    scripts = [spr_moving_script, rsvp_fixed_script, rsvp_moving_window]

    return scripts


def load_stimuli(experimental_stimuli, practice_stimuli):
    import pandas as pd

    with open(experimental_stimuli) as f:
        experimental_trials = pd.read_csv(f)
    with open(practice_stimuli) as f:
        practice_trials = pd.read_csv(f)
    stimuli = [experimental_trials, practice_trials]

    return stimuli


experimental_stimuli = 'demo_items.csv'
practice_stimuli = 'practice_stimuli.csv'
word_duration = 300
break_duration = 100
presentation_manner = 'moving'
rsvp_demo_dict = {'paradigm': 'rsvp', 'experimental_stimuli': experimental_stimuli, 'practice_stimuli':practice_stimuli,
                  'word duration': word_duration, 'break duration': break_duration,
                  'presentation manner': presentation_manner}

a=1