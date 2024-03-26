%define module	dbusmock

Name:		python-%{module}
Version:	0.31.1
Release:	1
Summary:	Mock D-Bus objects
Group:		Development/Python
License:	LGPLv3+
URL:		https://pypi.python.org/pypi/python-dbusmock
# http://pypi.io/packages/source/p/%%{name}/%%{name}-%%{version}.tar.gz
Source0:	https://github.com/martinpitt/python-dbusmock/releases/download/%{version}/dist.%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	dbus-x11
BuildRequires:	upower

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(nose)
BuildRequires:  python-dbus
BuildRequires:	pkgconfig(dbus-python)	
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(pip)

Requires:	dbus-x11
Requires:	python-dbus
Requires:	python3dist(pygobject)
%{?python_provide:%python_provide python-%{module}}

%description
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to
D-Bus services such as upower, systemd, ConsoleKit, gnome-session or
others, and it is hard (or impossible without root privileges) to set
the state of the real services to what you expect in your tests.

#------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
# Remove bundled egg-info
rm -rf python_%{module}.egg-info

%build
%py_build

%install
%py_install

%files
%doc README.md COPYING
%{python_sitelib}/%{module}/
%{python_sitelib}/python_dbusmock-%{version}.dist-info
