%define upstream_name    Perl6-Perldoc-To-Ansi
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	ANSI-colored text renderer for Perl6::Perldoc
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl6/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Perl6::Perldoc)
BuildArch:	noarch

%description
This module is almost identical to the Text renderer, except that many
constructs are highlighted with ANSI terminal codes. See the
Perl6::Perldoc::To::Text manpage for more information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 655614
- rebuild for updated spec-helper

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 572225
- update to 0.11

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 399261
- forgot to commit new tarball
- update to 0.10

* Wed Jul 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 396303
- update to 0.07

* Fri Jul 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 394294
- import perl-Perl6-Perldoc-To-Ansi


* Fri Jul 10 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
