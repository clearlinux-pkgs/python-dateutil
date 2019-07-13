#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCD54FCE3D964BEFB (paul@ganssle.io)
#
Name     : python-dateutil
Version  : 2.7.5
Release  : 56
URL      : https://github.com/dateutil/dateutil/releases/download/2.7.5/python-dateutil-2.7.5.tar.gz
Source0  : https://github.com/dateutil/dateutil/releases/download/2.7.5/python-dateutil-2.7.5.tar.gz
Source99 : https://github.com/dateutil/dateutil/releases/download/2.7.5/python-dateutil-2.7.5.tar.gz.asc
Summary  : Provides powerful extensions to the standard datetime module
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: python-dateutil-license = %{version}-%{release}
Requires: python-dateutil-python = %{version}-%{release}
Requires: python-dateutil-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : deprecated-setuptools_scm-legacypython
BuildRequires : freezegun
BuildRequires : pytest
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : setuptools_scm
BuildRequires : six
BuildRequires : tzdata

%description
dateutil - powerful extensions to datetime
==========================================

%package license
Summary: license components for the python-dateutil package.
Group: Default

%description license
license components for the python-dateutil package.


%package python
Summary: python components for the python-dateutil package.
Group: Default
Requires: python-dateutil-python3 = %{version}-%{release}

%description python
python components for the python-dateutil package.


%package python3
Summary: python3 components for the python-dateutil package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-dateutil package.


%prep
%setup -q -n python-dateutil-2.7.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554343827
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-dateutil
cp LICENSE %{buildroot}/usr/share/package-licenses/python-dateutil/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-dateutil/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
