Name:           gstreamer1-libav
Version:        1.18.4
Release:        1
Summary:        GStreamer plugin, a set of codecs plugins based on the ffmpeg library.
License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/
Source0:        https://gstreamer.freedesktop.org/src/gst-libav/gst-libav-%{version}.tar.xz

BuildRequires:  gcc-c++ meson gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  orc-devel bzip2-devel zlib-devel ffmpeg-devel

Requires:	gstreamer1 >= %{version} gstreamer1-plugins-base >= %{version} ffmpeg

%description
This module contains a GStreamer plugin for using the encoders, decoders, muxers,
and demuxers provided by FFmpeg. It is called gst-libav for historical reasons.

a set of codecs plugins based on the ffmpeg library. This is where you can find audio
and video decoders and encoders for a wide variety of formats including H.264, AAC, etc.

%prep
%autosetup -p1 -n gst-libav-%{version}

%build
%meson -D doc=disabled

%meson_build

%install
%meson_install


%files
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING
%{_libdir}/gstreamer-1.0/libgstlibav.so

%changelog
* Wed Sep 29 2021 weijin deng <weijin.deng@turbolinux.com.cn> - 1.18.4-1
- Package gstreamer1-libav init with 1.18.4
