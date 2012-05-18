android-addr2line
=================

Wrapper around Android's addr2line to make your life easier

1. Fill in the path to the addr2line binary, it's in the Android NDK folder (e.g. /opt/android-ndk-r7c/toolchains/arm-linux-androideabi-4.4.3/prebuilt/linux-x86/bin/arm-linux-androideabi-addr2line)
2. Fill in the path to your native library (the .so file)
3. chmod +x the script

Now whenever you have a native stack trace, just run it, paste the stack trace, hit CTRL-D, and you're done.
