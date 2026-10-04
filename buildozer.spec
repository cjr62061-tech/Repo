[app]
title = Random Ball
package.name = randomball
package.domain = com.bhai.randomball
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,pygame
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

# android ke liye
[app:android]
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True