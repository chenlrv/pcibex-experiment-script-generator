import tkinter as tk
import json
import os
import string
from tkinter import StringVar, font, filedialog, messagebox

class PcibexScriptGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PcIBEX Experiment Script Generator")
        self.root.geometry("600x480")
        self.root.resizable(False, False) 
   
        self.large_font = font.Font(family="Helvetica", size=16)
        self.medium_font = font.Font(family="Helvetica", size=13)
        self.button_font = font.Font(family="Helvetica", size=14, weight="bold")

        self.paradigm = StringVar(value="none_selected")
        self.practice_file = None
        self.experiment_file = None
        self.display_config = StringVar(value="none_selected")
        self.context = StringVar(value="none_selected")
        self.context_sentence_interval = tk.StringVar()

        self.completion_screen_text = tk.StringVar()
        self.practice_end_text = tk.StringVar()
        self.break_screen_text = tk.StringVar()
        self.trials_before_breaks = tk.StringVar()
        self.answers = StringVar(value="none_selected")
        self.inter_word_break_duration = tk.StringVar(value="")
        self.presentation_duration = tk.StringVar(value="")
        self.configurations = {}

        self.create_first_screen()

    def create_first_screen(self):
        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack()
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Welcome to PcIBEX Experiment Script Generator", 
                           font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)

        label2 = tk.Label(frame, text="Choose a paradigm:", font=self.large_font, anchor='w')
        label2.pack(anchor='w', padx=30, pady=(10, 0))

        rb_frame = tk.Frame(frame)
        rb_frame.pack(anchor='w', padx=20, pady=(10, 30))
        rb1 = tk.Radiobutton(rb_frame, text="SPR", variable=self.paradigm, value="SPR", font=self.medium_font, command=self.enable_next_button)
        rb2 = tk.Radiobutton(rb_frame, text="RSVP", variable=self.paradigm, value="RSVP", font=self.medium_font, command=self.enable_next_button)
        rb1.pack(anchor='w', pady=10, padx=20)
        rb2.pack(anchor='w', pady=10, padx=20)

        self.next_button = tk.Button(self.root, text="Next", command=self.create_files_upload_screen, state=tk.DISABLED, font=self.button_font, bg="lightblue", activebackground="lightgreen")
        self.next_button.pack(side='bottom', pady=60, anchor='center')


    def create_files_upload_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack()
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Upload Files", 
                        font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)


        label2 = tk.Label(frame, text="Browse Practice and Experiment files (CSV) to upload:", font=self.large_font, anchor='w')
        label2.pack(anchor='w', padx=20, pady=(10, 0))

        # Practice File Upload
        practice_frame = tk.Frame(self.root)
        practice_frame.pack(fill='x', padx=20, pady=10)
        tk.Label(practice_frame, text="Upload Practice File (CSV):", font=self.medium_font, anchor='w').grid(row=0, column=0, padx=(20, 10), pady=5, sticky='w')
        self.practice_file_path = tk.StringVar()
        tk.Entry(practice_frame, textvariable=self.practice_file_path, font=self.medium_font, width=20).grid(row=0, column=1, padx=10, pady=5, sticky='w')
        tk.Button(practice_frame, text="Browse", command=self.browse_practice_file, font=self.button_font, bg="lightblue", activebackground="lightgreen").grid(row=0, column=2, padx=10, pady=5, sticky='w')

        # Experiment File Upload
        experiment_frame = tk.Frame(self.root)
        experiment_frame.pack(fill='x', padx=20, pady=10)
        tk.Label(experiment_frame, text="Upload Experiment File (CSV):", font=self.medium_font, anchor='w').grid(row=0, column=0, padx=(20, 10), pady=5, sticky='w')
        self.experiment_file_path = tk.StringVar()
        tk.Entry(experiment_frame, textvariable=self.experiment_file_path, font=self.medium_font, width=18).grid(row=0, column=1, padx=10, pady=5, sticky='w')
        tk.Button(experiment_frame, text="Browse", command=self.browse_experiment_file, font=self.button_font, bg="lightblue", activebackground="lightgreen").grid(row=0, column=2, padx=10, pady=5, sticky='w')

        self.next_button = tk.Button(self.root, text="Next", command=self.create_display_screen, state=tk.DISABLED, font=self.button_font, bg="lightblue", activebackground="lightgreen")
        self.next_button.pack(side='bottom', pady=60, anchor='center')


    def create_display_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack()
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Display Configuration", 
                        font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)

        label2 = tk.Label(frame, text="Choose display configuration:", font=self.large_font, anchor='w')
        label2.pack(anchor='w', padx=30, pady=(10, 0))

        rb_frame = tk.Frame(frame)
        rb_frame.pack(anchor='w', padx=20, pady=(10, 30))
        rb1 = tk.Radiobutton(rb_frame, text="Moving Window", variable=self.display_config, value="Moving Window", font=self.medium_font, command=self.enable_next_button)
        rb2 = tk.Radiobutton(rb_frame, text="Center", variable=self.display_config, value="Center", font=self.medium_font, command=self.enable_next_button)
        rb1.pack(anchor='w', pady=10, padx=20)
        rb2.pack(anchor='w', pady=10, padx=20)

        next_screen = self.create_context_screen if self.paradigm.get() == "SPR" else self.create_duration_configuration_screen
        self.next_button = tk.Button(self.root, text="Next", command=next_screen, state=tk.DISABLED, font=self.button_font, bg="lightblue", activebackground="lightgreen")
        self.next_button.pack(side='bottom', pady=60, anchor='center')

    def create_context_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.geometry("600x600")
        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack(pady=20)
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Experiment Configuration", font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)

        tk.Label(frame, text="Context:", font=self.medium_font, anchor='w').grid(row=0, column=0, padx=(20, 10), pady=5, sticky='w')
        context_yes = tk.Radiobutton(frame, text="Yes", variable=self.context, value="yes", font=self.medium_font, command=self.toggle_context_interval)
        context_no = tk.Radiobutton(frame, text="No", variable=self.context, value="no", font=self.medium_font, command=self.toggle_context_interval)
        context_yes.grid(row=0, column=1, padx=10, pady=5, sticky='w')
        context_no.grid(row=0, column=2, padx=10, pady=5, sticky='w')

        self.context_interval_label = tk.Label(frame, text="Context Sentence Interval (ms):", font=self.medium_font, anchor='w')
        self.context_interval_entry = tk.Entry(frame, textvariable=self.context_sentence_interval, font=self.medium_font, width=20)
        self.context_sentence_interval.trace_add("write", self.check_fields)

        tk.Label(frame, text="Completion Screen Text:", font=self.medium_font, anchor='w').grid(row=2, column=0, padx=(20, 10), pady=5, sticky='w')
        tk.Entry(frame, textvariable=self.completion_screen_text, font=self.medium_font, width=30).grid(row=2, column=1, columnspan=2, padx=10, pady=5, sticky='w')
        self.completion_screen_text.trace_add("write", self.check_fields)

        tk.Label(frame, text="Practice End Text:", font=self.medium_font, anchor='w').grid(row=3, column=0, padx=(20, 10), pady=5, sticky='w')
        tk.Entry(frame, textvariable=self.practice_end_text, font=self.medium_font, width=30).grid(row=3, column=1, columnspan=2, padx=10, pady=5, sticky='w')
        self.practice_end_text.trace_add("write", self.check_fields)
        
        tk.Label(frame, text="Break Screen Text:", font=self.medium_font, anchor='w').grid(row=4, column=0, padx=(20, 10), pady=5, sticky='w')
        tk.Entry(frame, textvariable=self.break_screen_text, font=self.medium_font, width=30).grid(row=4, column=1, columnspan=2, padx=10, pady=5, sticky='w')
        self.break_screen_text.trace_add("write", self.check_fields)

        tk.Label(frame, text="Trials Before Breaks:", font=self.medium_font, anchor='w').grid(row=5, column=0, padx=(20, 10), pady=5, sticky='w')
        tk.Entry(frame, textvariable=self.trials_before_breaks, font=self.medium_font, width=20).grid(row=5, column=1, columnspan=2, padx=10, pady=5, sticky='w')
        self.trials_before_breaks.trace_add("write", self.check_fields)

        tk.Label(frame, text="Answers:", font=self.medium_font, anchor='w').grid(row=6, column=0, padx=(20, 10), pady=5, sticky='w')
        answers_yes_no = tk.Radiobutton(frame, text="Yes/No", variable=self.answers, value="yes/no", font=self.medium_font, command=self.check_fields)
        answers_custom = tk.Radiobutton(frame, text="Custom", variable=self.answers, value="custom", font=self.medium_font, command=self.check_fields)
        answers_yes_no.grid(row=6, column=1, padx=10, pady=5, sticky='w')
        answers_custom.grid(row=6, column=2, padx=10, pady=5, sticky='w')

        self.generate_button = tk.Button(self.root, text="Generate", state=tk.DISABLED, command=lambda: self.validate_and_proceed("context"), font=self.button_font, bg="lightblue", activebackground="lightgreen")
        self.generate_button.pack(side='bottom', pady=60, anchor='center')


    def create_duration_configuration_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        canvas = tk.Canvas(self.root, width=550, height=100)
        canvas.pack(pady=20)
        canvas.create_rectangle(10, 10, 540, 90, outline="black", fill="#1E90FF", width=2)
        canvas.create_text(275, 50, text="Duration Configuration", font=self.large_font, fill="black")

        frame = tk.Frame(self.root)
        frame.pack(fill='x', padx=20, pady=20)

        tk.Label(frame, text="Presentation Duration (ms):", font=self.medium_font, anchor='w').grid(row=0, column=0, padx=(20, 10), pady=5, sticky='w')
        tk.Entry(frame, textvariable=self.presentation_duration, font=self.medium_font, width=20).grid(row=0, column=1, padx=10, pady=5, sticky='w')
        self.presentation_duration.trace_add("write", self.check_duration_fields)

        tk.Label(frame, text="Inter-Word Break Duration (ms):", font=self.medium_font, anchor='w').grid(row=1, column=0, padx=(20, 10), pady=5, sticky='w')
        tk.Entry(frame, textvariable=self.inter_word_break_duration, font=self.medium_font, width=20).grid(row=1, column=1, padx=10, pady=5, sticky='w')
        self.inter_word_break_duration.trace_add("write", self.check_duration_fields)
        
        self.next_button = tk.Button(self.root, text="Next", command= lambda: self.validate_and_proceed("duration"), font=self.button_font, bg="lightblue", activebackground="lightgreen", state=tk.DISABLED)
        self.next_button.pack(side='bottom', pady=60, anchor='center')

    def check_duration_fields(self, *args):
        if self.presentation_duration.get() and self.inter_word_break_duration.get():
            self.next_button.config(state=tk.NORMAL)
        else:
            self.next_button.config(state=tk.DISABLED)

    def check_fields(self, *args):
        # Check if all required fields are filled and validate
        if (self.context.get() == "yes" and not self.context_sentence_interval.get()) or \
        not self.completion_screen_text.get() or \
        not self.practice_end_text.get() or \
        not self.break_screen_text.get() or \
        not self.trials_before_breaks.get() or \
        not (self.answers.get() == "yes/no" or self.answers.get() == 'custom'):
            self.generate_button.config(state=tk.DISABLED)
            return

        if self.context.get() == "yes":
            try:
                interval = int(self.context_sentence_interval.get())
                if interval <= 0:
                    raise ValueError("Interval must be greater than 0")
            except BaseException as e:
                messagebox.showerror("Invalid Input", "Context Sentence Interval must be a positive integer.")
                self.generate_button.config(state=tk.DISABLED)
                return

        try:
            trials = int(self.trials_before_breaks.get())
            if trials <= 0:
                raise ValueError("Trials must be greater than 0")
        except BaseException as e:
            messagebox.showerror("Invalid Input", "Trials Before Breaks must be a positive integer.")
            self.generate_button.config(state=tk.DISABLED)
            return

        # If all validations pass, enable the generate button
        self.generate_button.config(state=tk.NORMAL)


    def toggle_context_interval(self):
        if self.context.get() == "yes":
            self.context_interval_label.grid(row=1, column=0, padx=(20, 10), pady=5, sticky='w')
            self.context_interval_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky='w')
        else:
            self.context_interval_label.grid_forget()
            self.context_interval_entry.grid_forget()
        self.check_fields()
        

    def validate_and_proceed(self, screen):
        if screen == "context":
            try:
                trials_before_breaks = int(self.trials_before_breaks.get())
                if trials_before_breaks <= 0:
                    raise ValueError("Trials Before Breaks must be an integer greater than 0")

                if self.context.get() == "yes":
                    context_sentence_interval = int(self.context_sentence_interval.get())
                    if context_sentence_interval <= 0:
                        raise ValueError("Context Sentence Interval must be an integer greater than 0")

                # Proceed with the next steps if validation is successful
                self.generate_configuration()

            except ValueError as e:
                messagebox.showerror("Invalid Input", str(e))
        elif screen == "duration":
            self.next_button.config(state=tk.NORMAL)
            try:
                presentation_duration = int(self.presentation_duration.get())
                inter_word_break_duration = int(self.inter_word_break_duration.get())
    
                if presentation_duration <= 0 or inter_word_break_duration <= 0:
                    raise ValueError("All durations must be greater than 0")


                self.create_context_screen()
            except BaseException as e:
                messagebox.showerror("Invalid Input", "All durations must be integer greater than 0")         


    def generate_configuration(self):

        context_sentence_interval = {}
        duration_config = {}
        if self.context.get() == "yes":
            context_sentence_interval = {
                "context_sentence_interval": int(self.context_sentence_interval.get())
            }

        if self.paradigm.get() != "SPR":
            duration_config = {"duration_config":
                               {
                "presentation_duration": int(self.presentation_duration.get()),
                "inter_word_break_duration": int(self.inter_word_break_duration.get())
            }}

        config = {
            "paradigm": self.paradigm.get(),
            "files": {
                "practice_file": self.practice_file_path.get(),
                "experiment_file": self.experiment_file_path.get()
            },
            "sections": {
                "context": self.context.get(),
                **context_sentence_interval,
                "completion_screen_text": self.completion_screen_text.get(),
                "practice_end_text": self.practice_end_text.get(),
                "break_screen_text": self.break_screen_text.get(),
                "trials_before_breaks": (self.trials_before_breaks.get()),
                "answers": self.answers.get(),
            },
            "display_config": self.display_config.get(),
            **duration_config
        }

        config_json = json.dumps(config, indent=4, ensure_ascii=False)
        with open("config.json", "w", encoding='utf-8') as config_file:
                config_file.write(config_json)

    def enable_next_button(self):
        if self.paradigm.get() or self.display_config.get():
            self.next_button.config(state=tk.NORMAL)

    def browse_practice_file(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            if not self.is_english_filename(file_path):
                raise ValueError("Practice file name must contain only English letters, digits, dots, underscores, or hyphens")

            if file_path:
                self.practice_file_path.set(file_path)
                self.check_files_selected()
        except BaseException as e:
            messagebox.showerror("Invalid", str(e))

    def browse_experiment_file(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            if not self.is_english_filename(file_path):
                raise ValueError("Experiment file name must contain only English letters, digits, dots, underscores, or hyphens")

            if file_path:
                self.experiment_file_path.set(file_path)
                self.check_files_selected()
        except BaseException as e:
            messagebox.showerror("Invalid", str(e))       

    def is_english_filename(self, filename):
        return all(char in string.ascii_letters + string.digits + "._-" for char in os.path.basename(filename))

    def check_files_selected(self):
        if self.practice_file_path.get() and self.experiment_file_path.get():
            self.next_button.config(state=tk.NORMAL)
        else:
            self.next_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = PcibexScriptGeneratorApp(root)
    root.mainloop()
