Summary:        Network performance tool with modelling and replay support
Name:           uperf
Version:        1.0.5
Release:        2%{?dist}
License:        GPLv3
Group:          Applications/Internet
URL:            http://www.uperf.org/
Source0:        http://downloads.sourceforge.net/uperf/uperf-%{version}.tar.gz
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel
%description
Network performance tool that supports modelling and replay of various
networking patterns.

%prep
%setup -q -n %{name}-%{version}
find src -type f -print0 | xargs --null chmod 0644
find workloads -type f -print0 | xargs --null chmod 0644
chmod 0644 AUTHORS ChangeLog COPYING README

%build
%configure           \
    --enable-cpc     \
    --enable-netstat \
    --enable-udp     \
    --enable-sctp    \
    --enable-ssl
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Move stuff to own subdir
install -d -m 0755 %{buildroot}%{_datadir}/%{name}
install -p -m 0644 %{buildroot}%{_datadir}/*.xml %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_datadir}/*.xml %{buildroot}%{_datadir}/doc

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/uperf
%{_datadir}/uperf

%changelog
* Mon Feb 06 2017 Eduardo Minguez <edu@redhat.com> - 1.0.5-2
- Added RHEL stuff

* Sun Nov 20 2016 Terje Rosten <terje.rosten@ntnu.no> - 1.0.5-1
- 1.0.5

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 03 2012 Terje Rosten <terje.rosten@ntnu.no> - 1.0.4-1
- 1.0.4

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 18 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.0.3-0.3.beta
- move workloads files

* Thu Mar 18 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.0.3-0.2.beta
- don't ship pem files

* Mon Feb  1 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.0.3-0.1.beta
- initial build

