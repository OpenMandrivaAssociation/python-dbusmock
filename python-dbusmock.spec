%define module	dbusmock

Name:		python-%{module}
Version:	0.19
Release:	%mkrel 1
Summary:	Mock D-Bus objects
Group:		Development/Python
License:	LGPLv3+
URL:		http://pypi.python.org/pypi/python-dbusmock
# http://pypi.io/packages/source/p/%%{name}/%%{name}-%%{version}.tar.gz
Source0:	https://github.com/martinpitt/python-dbusmock/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	dbus-x11
BuildRequires:	upower

BuildRequires:	pkgconfig(python3)
BuildRequires:	pythonegg(3)(setuptools)
BuildRequires:	pythonegg(3)(nose)
BuildRequires:	pythonegg(3)(dbus-python)
BuildRequires:	pythonegg(3)(pygobject)

%description
With this program/Python library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to
D-Bus services such as upower, systemd, ConsoleKit, gnome-session or
others, and it is hard (or impossible without root privileges) to set
the state of the real services to what you expect in your tests.

%package -n	python3-%{module}
Summary:	Mock D-Bus objects (in Python3)
Group:		Development/Python
Requires:	dbus-x11
Requires:	pythonegg(3)(dbus-python)
Requires:	pythonegg(3)(pygobject)
%{?python_provide:%python_provide python3-%{module}}

%description -n	python3-%{module}
With this program/Python3 library you can easily create mock objects on
D-Bus. This is useful for writing tests for software which talks to
D-Bus services such as upower, systemd, ConsoleKit, gnome-session or
others, and it is hard (or impossible without root privileges) to set
the state of the real services to what you expect in your tests.

This is the Python 3 version of the package.

#------------------------------------------------

%prep
%setup -q

# Remove bundled egg-info
rm -rf python_%{module}.egg-info

%build
%py3_build

%install
%py3_install

%check
%define enable_tests_python3 0
%if %{enable_tests_python3}
%{__python3} setup.py test
%endif

%files -n python3-%{module}
%doc README.rst COPYING
%{python3_sitelib}/%{module}/
%{python3_sitelib}/python_%{module}-%{version}-py%{python3_version}.egg-info
