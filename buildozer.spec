[app]

# (str) Title of your application
title = BTP Pro Kinshasa

# (str) Package name
package.name = btpprokinshasa

# (str) Package domain (needed for android/ios packaging)
package.domain = org.btp

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all files)
source.include_exts = py,png,jpg,kv,atlas,txt

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (leave empty to include none)
source.exclude_exts = spec

# (list) List of directory to exclude (leave empty to include none)
source.exclude_dirs = tests, bin, venv

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,reportlab

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = NO, 1 = FALSE, 2 = YES)
warn_on_root = 1
android.accept_sdk_license = True
android.api = 33
android.min_api = 21
android.sdk = 33

