%define major		0
%define libname		%mklibname lrzip %{major}
%define develname	%mklibname lrzip -d

Name:		lrzip
Summary:	Long Range ZIP or Lzma RZIP
Version:	0.611
Release:	1
License:	GPLv2+
Group:		Archiving/Compression
URL:		http://ck.kolivas.org/apps/lrzip/
Source0:	http://ck.kolivas.org/apps/lrzip/%{name}-%{version}.tar.bz2
BuildRequires:	liblzo2-devel
BuildRequires:	bzip2-devel
BuildRequires:	zlib-devel
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

#------------------------------------------------------------------------------

%package -n %{libname}
Summary:	lrzip shared library
Group:		System/Libraries

%description -n %{libname}
This package contains lrzip shared library.

%files -n %{libname}
%{_libdir}/liblrzip.so.%{major}*

#------------------------------------------------------------------------------

%package -n %{develname}
Summary:	lrzip shared library
Group:		Development/C

%description -n %{develname}
This package contains dfevelopment files for lrzip library.

%files -n %{develname}
%{_libdir}/liblrzip.so
%{_libdir}/pkgconfig/lrzip.pc

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%configure --disable-static
%make

%check
make check

%install
%makeinstall_std
%__rm -rf %{buildroot}/%{_libdir}/*.la
