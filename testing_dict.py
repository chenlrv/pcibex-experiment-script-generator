from loading_stuff import *

my_dict = {'paradigm': 'RSVP', 'display_config': 'Centered', 'word_presentation_duration': 300,
           'inter_word_break_duration': 100, 'context_choice': 'No', 'trials_until_break': 0,
           'context_sentence_interval': 100,'question_type': 'yes/no', 'completion_text': 'תודה על ההשתתפות!', 'break_screen_text':
           'זה הזמן לקחת הפסקה קצרה. לחזרה, יש ללחוץ על מקש הרווח', 'practice_end_text':
               'שלב האימון הסתיים. להמשך לניסוי, יש ללחוץ על מקש הרווח.'}


b = write_script(my_dict)

