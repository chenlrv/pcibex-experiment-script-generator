from loading_stuff import *

my_dict = {
    "paradigm": "SPR",
    "display_config": 'Moving window',
    "files": {
        "practice_file": "practice_file.csv",
        "experiment_file": "experiment_file.csv"
    },
    "sections": {
        "context": "Yes",
        "context_sentence_interval": 1500,
        "completion_screen_text": "Thank you for participating!",
        "practice_end_text": "You have completed the practice session.",
        "break_screen_text": "Take a short break.",
        "trials_before_breaks": 20,
        "answers": "Custom",
    }
}

b = write_script(my_dict)

