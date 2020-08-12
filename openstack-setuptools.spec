#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstack-setuptools
Version  : 49.3.2
Release  : 169
URL      : https://files.pythonhosted.org/packages/ed/72/046e8d3ad9da774dee020f88964b159ab24697c001c776e76a85450d699d/setuptools-49.3.2.zip
Source0  : https://files.pythonhosted.org/packages/ed/72/046e8d3ad9da774dee020f88964b159ab24697c001c776e76a85450d699d/setuptools-49.3.2.zip
Summary  : Easily download, build, install, upgrade, and uninstall Python packages
Group    : Development/Tools
License  : MIT
Requires: openstack-setuptools-bin = %{version}-%{release}
Requires: openstack-setuptools-license = %{version}-%{release}
Requires: openstack-setuptools-python = %{version}-%{release}
Requires: openstack-setuptools-python3 = %{version}-%{release}
Requires: certifi
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-distutils36
BuildRequires : certifi
BuildRequires : setuptools

%description
.. image:: https://img.shields.io/pypi/v/setuptools.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/setuptools.svg
:target: `PyPI link`_

%package bin
Summary: bin components for the openstack-setuptools package.
Group: Binaries
Requires: openstack-setuptools-license = %{version}-%{release}

%description bin
bin components for the openstack-setuptools package.


%package license
Summary: license components for the openstack-setuptools package.
Group: Default

%description license
license components for the openstack-setuptools package.


%package python
Summary: python components for the openstack-setuptools package.
Group: Default
Requires: openstack-setuptools-python3 = %{version}-%{release}

%description python
python components for the openstack-setuptools package.


%package python3
Summary: python3 components for the openstack-setuptools package.
Group: Default
Requires: python3-core

%description python3
python3 components for the openstack-setuptools package.


%prep
%setup -q -n setuptools-49.3.2
cd %{_builddir}/setuptools-49.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1597276192
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
python3.6 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1597276192
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openstack-setuptools
cp %{_builddir}/setuptools-49.3.2/LICENSE %{buildroot}/usr/share/package-licenses/openstack-setuptools/a5234543d56e03c950c0080826b53a0cb97671af
python3.6 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/bin/easy_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/easy_install-3.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/openstack-setuptools/a5234543d56e03c950c0080826b53a0cb97671af

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
