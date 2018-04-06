#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCD54FCE3D964BEFB (paul@ganssle.io)
#
Name     : python-dateutil
Version  : 2.6.1
Release  : 28
URL      : https://github.com/dateutil/dateutil/releases/download/2.6.1/python-dateutil-2.6.1.tar.gz
Source0  : https://github.com/dateutil/dateutil/releases/download/2.6.1/python-dateutil-2.6.1.tar.gz
Source99 : https://github.com/dateutil/dateutil/releases/download/2.6.1/python-dateutil-2.6.1.tar.gz.asc
Summary  : Extensions to the standard Python datetime module
Group    : Development/Tools
License  : BSD-3-Clause
Requires: python-dateutil-legacypython
Requires: python-dateutil-python3
Requires: python-dateutil-python
Requires: six
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : setuptools-python
BuildRequires : six
BuildRequires : tzdata

%description
The dateutil module provides powerful extensions to the
        datetime module available in the Python standard library.

%package legacypython
Summary: legacypython components for the python-dateutil package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the python-dateutil package.


%package python
Summary: python components for the python-dateutil package.
Group: Default
Requires: python-dateutil-python3

%description python
python components for the python-dateutil package.


%package python3
Summary: python3 components for the python-dateutil package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-dateutil package.


%prep
%setup -q -n python-dateutil-2.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523041123
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1523041123
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
