
%global project_folder %{name}-%{version}-src
%global archive_folder build

Name:           sblim-cim-client2
Version:        2.2.1
Release:        3%{?dist}
Summary:        Java CIM Client library

Group:          Development/Libraries
License:        EPL
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}-src.zip

BuildArch:      noarch

BuildRequires:  java-devel >= 1.4
BuildRequires:  jpackage-utils >= 0:1.5.32
BuildRequires:  ant >= 0:1.6

Requires:       java >= 1.4
Requires:       jpackage-utils >= 0:1.5.32

%description
The purpose of this package is to provide a CIM Client Class Library for Java
applications. It complies to the DMTF standard CIM Operations over HTTP and
intends to be compatible with JCP JSR48 once it becomes available. To learn
more about DMTF visit http://www.dmtf.org.
More infos about the Java Community Process and JSR48 can be found at
http://www.jcp.org and http://www.jcp.org/en/jsr/detail?id=48.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation
Requires:       sblim-cim-client2 = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Manual and sample code for %{name}
Group:          Documentation
Requires:       sblim-cim-client2 = %{version}-%{release}

%description manual
Manual and sample code for %{name}.


%prep
%setup -q -n %{project_folder}

dos2unixConversion() {
        fileName=$1
        %{__sed} -i 's/\r//g' "$fileName"
}

dosFiles2unix() {
        fileList=$1
        for fileName in $fileList; do
                dos2unixConversion $fileName
        done
}

dosFiles2unix 'ChangeLog NEWS README COPYING sblim-cim-client2.properties sblim-slp-client2.properties'
dosFiles2unix 'smpl/org/sblim/slp/example/*'
dosFiles2unix 'smpl/org/sblim/cimclient/samples/*'

%build
export ANT_OPTS="-Xmx256m"
ant \
        -Dbuild.compiler=modern \
        -DManifest.version=%{version}\
        package java-doc


%install
# --- documentation ---
dstDocDir=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -d $dstDocDir
install --mode=644 ChangeLog COPYING README NEWS $dstDocDir
# --- samples (also into _docdir) ---
cp -pr  smpl/org $dstDocDir
# --- config files ---
confDir=$RPM_BUILD_ROOT%{_sysconfdir}/java
install -d $confDir
install --mode=664 sblim-cim-client2.properties sblim-slp-client2.properties $confDir
# --- jar ---
install -d $RPM_BUILD_ROOT%{_javadir}
install %{archive_folder}/lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
(
  cd $RPM_BUILD_ROOT%{_javadir} &&
    ln -sf %{name}-%{version}.jar %{name}.jar;
)
# --- javadoc ---
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr %{archive_folder}/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}


%files
%dir %{_datadir}/doc/%{name}-%{version}
%config(noreplace) %{_sysconfdir}/java/sblim-cim-client2.properties
%config(noreplace) %{_sysconfdir}/java/sblim-slp-client2.properties
%doc %{_docdir}/%{name}-%{version}/COPYING
%doc %{_docdir}/%{name}-%{version}/README
%doc %{_docdir}/%{name}-%{version}/ChangeLog
%doc %{_docdir}/%{name}-%{version}/NEWS
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar

%files javadoc
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}/COPYING
%doc %{_docdir}/%{name}-%{version}/org


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.2.1-3
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.1-1
- Update to sblim-cim-client2-2.2.1

* Mon Sep 17 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.2.0-1
- Update to sblim-cim-client2-2.2.0

* Tue Sep 04 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.12-3
- Fix issues found by fedora-review utility in the spec file

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 19 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.12-1
- Update to sblim-cim-client2-2.1.12

* Wed Jan 04 2012 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.11-1
- Update to sblim-cim-client2-2.1.11

* Mon Sep 26 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.10-1
- Update to sblim-cim-client2-2.1.10

* Wed Aug 17 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.9-2
- Rebuild due to the trailing slash bug of rpm

* Wed Jul 20 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.9-1
- Update to sblim-cim-client2-2.1.9

* Wed May 25 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.8-1
- Update to sblim-cim-client2-2.1.8

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb  8 2011 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.7-1
- Update to sblim-cim-client2-2.1.7

* Wed Jun  2 2010 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.1.3-1
- Update to sblim-cim-client2-2.1.3

* Tue Oct  6 2009 Vitezslav Crhonek <vcrhonek@redhat.com> - 2.0.9.2-1
- Initial support
