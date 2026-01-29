[app]
title = ജ്യോതിഷമഞ്ജരി
package.name = jyotishamanjari
package.domain = org.jyotish
source.dir = .
version = 1.0

# Requirements
requirements = python3,flask,pywebview

# Android settings
android.api = 31
android.minapi = 21
android.ndk = 23b
android.sdk = 31

# Permissions
android.permissions = INTERNET

# Orientation
orientation = portrait

# Icon (optional)
# icon.filename = icon.png

# Include files
source.include_exts = py,png,jpg,html,json

# Log level
log_level = 2

# Presplash (optional)
# presplash.filename = presplash.png

# Build options
android.accept_sdk_license = True
p4a.branch = develop
android.arch = arm64-v8a, armeabi-v7a
