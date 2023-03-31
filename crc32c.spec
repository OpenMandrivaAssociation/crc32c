%define major 1
%define libname %mklibname crc32c
%define devname %mklibname crc32c -d

Name: crc32c
Version: 1.1.3
Release: 0.20230104.2
Source0: https://github.com/google/crc32c/archive/refs/heads/main.tar.gz
Summary: CRC32c library with support for CPU specific acceleration instructions
URL: https://github.com/google/crc32c
License: GPL
Group: System/Libraries
BuildRequires: cmake ninja

%description
CRC32c library with support for CPU specific acceleration instructions

%package -n %{libname}
Summary: CRC32c library with support for CPU specific acceleration instructions
Group: System/Libraries

%description -n %{libname}
CRC32c library with support for CPU specific acceleration instructions

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1 -n %{name}-main
%cmake \
	-DCRC32C_BUILD_BENCHMARKS:BOOL=OFF \
	-DCRC32C_BUILD_TESTS:BOOL=OFF \
	-DCRC32C_USE_GLOG:BOOL=OFF \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/Crc32c
