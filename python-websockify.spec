%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define pkgname websockify

Name:           python-%{pkgname}
Version:        0.6.0
Release:        CROC1%{?dist}
Summary:        WSGI based adapter for the Websockets protocol

License:        LGPLv3
URL:            https://github.com/kanaka/websockify
Source0:        %{pkgname}-%{version}.tar.gz
Source1:        https://github.com/kanaka/websockify/archive/v%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       numpy
Requires:       python-setuptools

%description
Python WSGI based adapter for the Websockets protocol

%prep
%setup -q -n %{pkgname}-%{version}

# TODO: Have the following handle multi line entries
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py

%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

rm -Rf %{buildroot}/usr/share/websockify
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 444 docs/websockify.1 %{buildroot}%{_mandir}/man1/

find $RPM_BUILD_ROOT/ -name '*.egg-info' -exec rm -rf -- '{}' '+'


%files
%doc LICENSE.txt CHANGES.txt README.md docs
%{_mandir}/man1/websockify.1*
%{python_sitelib}/websockify/*
%{_bindir}/websockify


%changelog
* Mon Sep 22 2014 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.6.0-CROC1
- Specific CROC Cloud build

* Thu Sep 18 2014 Mikhail Ushanov <gm.mephisto@gmail.com> - 0.6.0-1
- Update to release 0.6.0
- Add requires to 'numpy'

* Thu Sep 10 2013 Nikola Đipanov <ndipanov@redhat.com> - 0.5.1-1
- Update to release 0.5.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 20 2013 Pádraig Brady <P@draigBrady.com> - 0.4.1-1
- Update to release 0.4.1

* Tue Mar 12 2013 Pádraig Brady <P@draigBrady.com> - 0.2.0-4
- Add runtime dependency on setuptools

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 31 2012 Pádraig Brady <P@draigBrady.com> - 0.2.0-2
- Remove hard dependency on numpy

* Mon Oct 22 2012 Nikola Đipanov <ndipanov@redhat.com> - 0.2.0-1
- Moving to the upstream version 0.2.0

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 6 2012 Adam Young <ayoung@redhat.com> - 0.1.0-4
- Added Description
- Added Manpage

* Fri May 11 2012 Matthias Runge <mrunge@matthias-runge.de> - 0.1.0-2
- spec cleanup

* Thu May 10 2012 Adam Young <ayoung@redhat.com> - 0.1.0-1
- Initial RPM release.
