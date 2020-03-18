#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Text-Reform
Version  : 1.20
Release  : 21
URL      : http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/Text-Reform-1.20.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/C/CH/CHORNY/Text-Reform-1.20.tar.gz
Summary  : Manual text wrapping and reformatting
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Text-Reform-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Text::Reform version 1.20
NAME
Text::Reform - Manual text wrapping and reformating

%package dev
Summary: dev components for the perl-Text-Reform package.
Group: Development
Provides: perl-Text-Reform-devel = %{version}-%{release}
Requires: perl-Text-Reform = %{version}-%{release}

%description dev
dev components for the perl-Text-Reform package.


%package perl
Summary: perl components for the perl-Text-Reform package.
Group: Default
Requires: perl-Text-Reform = %{version}-%{release}

%description perl
perl components for the perl-Text-Reform package.


%prep
%setup -q -n Text-Reform-1.20
cd %{_builddir}/Text-Reform-1.20

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Text::Reform.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/Text/Reform.pm
