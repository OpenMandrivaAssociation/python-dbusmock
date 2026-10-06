%define module	dbusmock
%define oname python_dbusmock

Name:		python-dbusmock
Version:	0.38.1
Release:	2
Summary:	Mock D-Bus objects
Group:		Development/Python
License:	LGPLv3+
URL:		https://pypi.python.org/pypi/python-dbusmock
# http://pypi.io/packages/source/p/%%{name}/%%{name}-%%{version}.tar.gz
Source0:	https://github.com/martinpitt/python-dbusmock/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	dbus-x11
BuildRequires:	upower
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	python%{pyver}dist(dbus-python)
BuildRequires:	python%{pyver}dist(pygobject)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

Requires:	dbus-x11
Requires:	python%{pyver}dist(dbus-python)
Requires:	python%{pyver}dist(pygobject)
%{?python_provide:%python_provide python-%{module}}

%description
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to
D-Bus services such as upower, systemd, ConsoleKit, gnome-session or
others, and it is hard (or impossible without root privileges) to set
the state of the real services to what you expect in your tests.

#------------------------------------------------

%prep -a
# Remove bundled egg-info
rm -rf python_%{module}.egg-info

%build -p
# Package cannot find its own version, use override to provide it
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc README.md
%license COPYING
%{python_sitelib}/%{module}/
%{python_sitelib}/%{oname}-%{version}.dist-info
