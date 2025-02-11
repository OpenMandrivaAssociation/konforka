%define	major 0
%define libname %mklibname %{name}
%define develname %mklibname %{name} -d

Summary:	Convenience library for common KIN project code
Name:		konforka
Version:	0.0.1
Release:	0.20221024.1
Group:		System/Libraries
License:	MIT
URL:		https://kin.klever.net/konforka/
Source0:	konforka-20221024.tar.xz
Patch0:		konforka-linkage_fix.diff
Patch1:		konforka-gcc43.diff
BuildRequires:	autoconf automake libtool
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libpqxx)
BuildRequires:	doxygen
BuildRequires:	libxslt-proc
BuildRequires:	postgresql-devel

%description
Convenience library for common KIN project code.

konforka library is a convenience library which is supposed to soak in some
code common to our projects. It is not likely that you want to try this out
unless you need it as a dependency for other project. This is why you
should not expect a lengthier description here.

%package -n	%{libname}
Summary:	Convenience library for common KIN project code
Group:          System/Libraries

%description -n	%{libname}
Convenience library for common KIN project code.

konforka library is a convenience library which is supposed to soak in some
code common to our projects. It is not likely that you want to try this out
unless you need it as a dependency for other project. This is why you
should not expect a lengthier description here.

%package -n	%{develname}
Summary:	Static library and header files for the konforka library
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	%{mklibname %{name} 0}-devel = %{version}
Obsoletes:	%{mklibname %{name} 0}-devel

%description -n	%{develname}
Convenience library for common KIN project code.

konforka library is a convenience library which is supposed to soak in some
code common to our projects. It is not likely that you want to try this out
unless you need it as a dependency for other project. This is why you
should not expect a lengthier description here.

This package contains the static konforka library and its header files.

%prep
%autosetup -p0 -n %{name}
autoreconf -fi
%configure

%build
%make_build

%install
%make_install

# cleanups
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname}
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
