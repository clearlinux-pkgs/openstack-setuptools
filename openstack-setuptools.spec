#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : openstack-setuptools
Version  : 42.0.1
Release  : 146
URL      : https://files.pythonhosted.org/packages/ce/1d/96320b9784b04943c924a9f1c6fa49124a1542039ce098a5f9a369227bad/setuptools-42.0.1.zip
Source0  : https://files.pythonhosted.org/packages/ce/1d/96320b9784b04943c924a9f1c6fa49124a1542039ce098a5f9a369227bad/setuptools-42.0.1.zip
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
:target: https://pypi.org/project/setuptools

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
%setup -q -n setuptools-42.0.1
cd %{_builddir}/setuptools-42.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574718278
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
python3.6 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1574718278
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/openstack-setuptools
cp %{_builddir}/setuptools-42.0.1/LICENSE %{buildroot}/usr/share/package-licenses/openstack-setuptools/a5234543d56e03c950c0080826b53a0cb97671af
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
