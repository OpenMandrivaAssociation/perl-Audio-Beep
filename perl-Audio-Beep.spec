%define upstream_name    Audio-Beep
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Audio::Beep player module using the B<beep> program
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Audio/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Test::More)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
no description found

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
echo | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.110.0-3mdv2011.0
+ Revision: 680480
- mass rebuild

* Mon Jul 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 551272
- rebuild

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.0
+ Revision: 381297
- import perl-Audio-Beep


* Sat May 30 2009 cpan2dist 0.11-1mdv
- initial mdv release, generated with cpan2dist

