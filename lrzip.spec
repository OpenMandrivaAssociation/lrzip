%define major 0
%define libname %mklibname lrzip %{major}
%define devname %mklibname lrzip -d

Summary:	Long Range ZIP or Lzma RZIP
Name:		lrzip
Version:	0.651
Release:	1
License:	GPLv2+
Group:		Archiving/Compression
Url:		https://ck.kolivas.org/apps/lrzip/
Source0:	http://ck.kolivas.org/apps/lrzip/%{name}-%{version}.tar.xz
BuildRequires:	bzip2-devel
BuildRequires:  pkgconfig(liblz4)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	lzo-devel
Requires:	tar

%description
This is a compression program optimized for large files. The larger the file
and the more memory you have, the better the compression advantage this will
provide, especially once the files are larger than 100MB. The advantage can
be chosen to be either size (much smaller than bzip2) or speed (much faster
than bzip2).

%files
%{_bindir}/lr*
%doc %{_docdir}/%{name}
%{_mandir}/man?/*.*

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	lrzip shared library
Group:		System/Libraries

%description -n %{libname}
This package contains lrzip shared library.

%files -n %{libname}
#{_libdir}/liblrzip.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	lrzip shared library
Group:		Development/C
Requires:	%{name}

%description -n %{devname}
This package contains dfevelopment files for lrzip library.

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/liblrzip.so
%{_libdir}/pkgconfig/lrzip.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
make check
