import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import importlib
import api_numpy

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AI Job Datasets")
        self.configure(bg="black")
        self.resizable(False, False)

        self._build_styles()
        self._build_ui()

    def _build_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

    def _build_ui(self):
        outer = tk.Frame(self, bg="black", padx=32, pady=28)
        outer.pack()

        tk.Label(outer, text="AI Job Datasets", font=("Segoe UI", 16, "bold"),
                 bg="black", fg="white").pack(anchor="w", pady=(0, 20))

        self.ai_job_dataset = self._file_picker(outer, "Select ai_job_dataset")
        self.ai_job_dataset1 = self._file_picker(outer, "Select ai_job_dataset1")

        # ── Status bar ──
        self.status = tk.StringVar(value="Browse for two CSV files then export.")
        # Pack status widget to the left and align text to the left with justify="left".
        tk.Label(outer, textvariable=self.status, font=("Segoe UI", 9),
                 bg="black", fg="white", justify="left").pack(anchor="w", pady=(12, 0))

        # ── Export button — runs transformations and saves to this script's folder ──
        tk.Button(outer, text="Export CSV", command=self._export,
                  bg="green", fg="black", activebackground="white", activeforeground="black", font=("Segoe UI", 11, "bold"),
                  relief="flat", padx=16, pady=8, cursor="hand2").pack(anchor="e", pady=(16, 0))

    def _file_picker(self, parent, label):
        frame = tk.Frame(parent, bg="black", pady=6)
        frame.pack(fill="x")

        tk.Label(frame, text=label, bg="black", fg="white",
                 font=("Segoe UI", 9)).pack(anchor="w")

        picker_row = tk.Frame(frame, bg="black")
        picker_row.pack(anchor="w")

        # Pack side="left to align widgets to the left. Align text to the left with anchor="w".
        # Set height to picker_row height in both widgets.
        # To do that, pack outline to fill="y". Then pack children to fill="both, expand=True.

        path_outline = tk.Frame(picker_row, bg="white", padx=1, pady=1)
        path_outline.pack(side="left", fill="y")

        path_row = tk.Frame(path_outline, bg="black")
        path_row.pack(fill="both", expand=True)

        path_var = tk.StringVar(value="No file selected")
        tk.Label(path_row, textvariable=path_var, bg="black", fg="white",
                 font=("Segoe UI", 9), width=50, anchor="w",
                 padx=8).pack()

        button_outline = tk.Frame(picker_row, bg="white", padx=1, pady=1)
        # Create gap between path and button with padx
        button_outline.pack(side="left", fill="y", padx=(6, 0))

        tk.Button(button_outline, text="Browse", command=lambda: self._browse(path_var),
                  bg="black", fg="white", activebackground="white", activeforeground="black", font=("Segoe UI", 9),
                  relief="flat", padx=10, cursor="hand2").pack(fill="both", expand=True)

        return path_var

    def _browse(self, path_var):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if path:
            path_var.set(path)

    def _export(self):
        ai_job_dataset, ai_job_dataset1 = self.ai_job_dataset.get(), self.ai_job_dataset1.get()
        if ai_job_dataset == "No file selected" or ai_job_dataset1 == "No file selected":
            messagebox.showwarning("Missing files", "Please select both CSV files.")
            return

        # Export to output folder
        os.makedirs("output", exist_ok=True)
        export_path_parts = [os.path.dirname(os.path.abspath(__file__)), "output", "numpy_ai_job_datasets.csv"]

        try:
            self.status.set("Transforming...")
            self.update()
            importlib.reload(api_numpy)
            dataframe = api_numpy.apply_transformations(ai_job_dataset, ai_job_dataset1)
            dataframe.to_csv(os.path.join(*export_path_parts), index=False)
            self.status.set(f"Completed!\nExported {len(dataframe):,} rows to {os.path.join(*export_path_parts[-2:])}")
        except PermissionError:
            messagebox.showerror("File in use", f"Please close {os.path.basename(export_path)} before exporting.")
            self.status.set("Export failed - file is open.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status.set("Export failed.")

if __name__ == "__main__":
    App().mainloop()
