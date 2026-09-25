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

# (list) Source files to exclude (leave empty to include none)
source.exclude_exts = spec

# (list) List of directory to exclude (leave empty to include none)
source.exclude_dirs = tests, bin, venv

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, INTERNET

# (int) Android API à cibler
android.api = 33

# (int) Android API minimum supporté
android.minapi = 24

# (bool) Accepter automatiquement la licence SDK
android.accept_sdk_license = True

# (str) Branche python-for-android
p4a.branch = develop

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
