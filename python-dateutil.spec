#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCD54FCE3D964BEFB (paul@ganssle.io)
#
Name     : python-dateutil
Version  : 2.8.1
Release  : 70
URL      : https://github.com/dateutil/dateutil/releases/download/2.8.1/python-dateutil-2.8.1.tar.gz
Source0  : https://github.com/dateutil/dateutil/releases/download/2.8.1/python-dateutil-2.8.1.tar.gz
Source1  : https://github.com/dateutil/dateutil/releases/download/2.8.1/python-dateutil-2.8.1.tar.gz.asc
Summary  : Provides powerful extensions to the standard datetime module
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: python-dateutil-license = %{version}-%{release}
Requires: python-dateutil-python = %{version}-%{release}
Requires: python-dateutil-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : freezegun
BuildRequires : pytest
BuildRequires : setuptools
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
Provides: pypi(python_dateutil)
Requires: pypi(six)

%description python3
python3 components for the python-dateutil package.


%prep
%setup -q -n python-dateutil-2.8.1
cd %{_builddir}/python-dateutil-2.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583505869
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-dateutil
cp %{_builddir}/python-dateutil-2.8.1/LICENSE %{buildroot}/usr/share/package-licenses/python-dateutil/f3b34c666d9f93071f6dbeeea6f8daefc2258e90
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-dateutil/f3b34c666d9f93071f6dbeeea6f8daefc2258e90

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
