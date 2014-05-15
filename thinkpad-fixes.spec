Name:		thinkpad-fixes	
Version:	0.2
Release:	1%{?dist}
Summary:	Various configuration fixes for running Fedora on a Thinkpad X1 Carbon
Group:		System Environment/Base
License:	GPLv2
URL:		http://github.com/matthicksj/thinkpad-fixes
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gcc
BuildRequires: glib2-devel

%description
This package provides various configuration fixes for things like the backlight
and brightness changing when running Fedora on a Thinkpad X1 Carbon.

Building this requires Gnome 3.12 which is available for Fedora 20 from:
https://copr.fedoraproject.org/coprs/rhughes/f20-gnome-3-12/

%prep
%setup -q -n %{name}-%{version}
gcc -I/usr/include/glib-2.0 -I/usr/lib64/glib-2.0/include/ ./ThinkLight.c -o backlight -lglib-2.0

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp backlight %{buildroot}%{_bindir}
cp brightness %{buildroot}%{_bindir}

mkdir -p %{_sysconfdir}/yum.repos.d/
cp f21-gnome.repo %{_sysconfdir}/yum.repos.d/

# Load the ec_sys module on boot for the backlight fix to work
mkdir -p %{_sysconfdir}/sysconfig/modules/
cp ec_sys.modules %{_sysconfdir}/sysconfig/modules/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%attr(755, root, root) %{_bindir}/backlight
%attr(755, root, root) %{_bindir}/brightness
%attr(755, root, root) %{_sysconfdir}/sysconfig/modules/ec_sys.modules
%{_sysconfdir}/yum.repos.d/f21-gnome.repo

%changelog
* Thu May 15 2014 Matt Hicks <matthicksj@gmail.com> 0.2-1
- new package built with tito

