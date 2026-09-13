[app]

# (str) Title of your application
title = MiniGame

# (str) Package name
package.name = minigame

# (str) Package domain
package.domain = org.gozdnijoza

# (str) Source code where main.py lives
source.dir = .

# (str) Main filename
source.main = main.py

# (str) Application version
version = 1.0

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


# -------------------------
# Android configuration
# -------------------------

# Accept Android SDK licenses automatically
android.accept_sdk_license = True

# Nastavite ciljni API na 34 (zahteva Google Play)
android.api = 34

# Nastavite minimalni API na vsaj 21 ali 24 (odpravi napako prevajalnika)
android.minapi = 24

# Nastavite NDK API prav tako na vsaj 24
android.ndk_api = 24

# Architecture
android.archs = arm64-v8a

# Android app permissions
android.permissions = INTERNET


[buildozer]

# (str) Log level
log_level = 2

# (str) Warning for root
warn_on_root = 1
