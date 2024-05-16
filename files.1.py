import os

if os.environ.get("PROGRAMFILES(X86)") is None:  # 32-bit Python
    program_files_path = os.environ.get("PROGRAMFILES")
else:
    program_files_path = os.environ.get("PROGRAMFILES(X86)")

print(program_files_path)
