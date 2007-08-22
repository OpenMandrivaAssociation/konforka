%define rev r243

%define	major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	Convenience library for common KIN project code
Name:		konforka
Version:	0.0.1
Release:	%mkrel 0.%{rev}.4
Group:		System/Libraries
License:	MIT
URL:		http://kin.klever.net/konforka/
Source0:	%{name}-%{version}-%{rev}.tar.bz2
BuildRequires:	autoconf2.5
BuildRequires:	automake1.8
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	pqxx-devel
BuildRequires:	doxygen
BuildRequires:	libxslt-proc
BuildRequires:	postgresql-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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

%setup -q -n %{name}

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoheader; automake -a; autoconf --force

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
