# These and other macros are documented in dhd/droid-hal-device.inc
%define device onclite
%define vendor xiaomi
%define vendor_pretty Xiaomi
%define device_pretty Redmi 7 (onclite)
%define installable_zip 1
%define droid_target_aarch64 1
# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1
%define makefstab_skip_entries /dev/cpuctl
%define straggler_files \
/bugreports \
/d \
/cache \
/sdcard \
/vendor \
/dsp \
/firmware \
%{nil}
%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}
 %define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}
%include rpm/dhd/droid-hal-device.inc
