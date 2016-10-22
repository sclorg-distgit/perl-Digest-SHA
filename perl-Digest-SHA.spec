%{?scl:%scl_package perl-Digest-SHA}

Name:           %{?scl_prefix}perl-Digest-SHA
Epoch:          1
Version:        5.95
Release:        367%{?dist}
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Digest-SHA/
Source0:        http://www.cpan.org/authors/id/M/MS/MSHELOR/Digest-SHA-%{version}.tar.gz
# Since 5.80, upstream overrides CFLAGS because they think it improves
# performance. Revert it.
Patch0:         Digest-SHA-5.93-Reset-CFLAGS.patch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Getopt::Std)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(vars)
# Run-time
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Fcntl)
# Getopt::Long not used at tests
BuildRequires:  %{?scl_prefix}perl(integer)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Optional run-time
BuildRequires:  %{?scl_prefix}perl(Digest::base)
# Tests
BuildRequires:  %{?scl_prefix}perl(FileHandle)
# Optional tests
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Test::More)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
BuildRequires:  %{?scl_prefix}perl(Test::Pod::Coverage) >= 0.08
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(Carp)
# Optional but recommended
Requires:       %{?scl_prefix}perl(Digest::base)

%{?perl_default_filter}

%description
Digest::SHA is a complete implementation of the NIST Secure Hash Standard. It
gives Perl programmers a convenient way to calculate SHA-1, SHA-224, SHA-256,
SHA-384, SHA-512, SHA-512/224, and SHA-512/256 message digests. The module can
handle all types of input, including partial-byte data.

%prep
%setup -q -n Digest-SHA-%{version}
%patch0 -p1
chmod -x examples/*
%{?scl:scl enable %{scl} '}perl -MExtUtils::MakeMaker -e %{?scl:'"}'%{?scl:"'}ExtUtils::MM_Unix->fixin(q{examples/dups})%{?scl:'"}'%{?scl:"'}%{?scl:'}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE=%{?scl:'"}'%{?scl:"'}%{optflags}%{?scl:'"}'%{?scl:"'} && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR='%{buildroot}'%{?scl:'}
find '%{buildroot}' -type f -name .packlist -exec rm -f {} +
find '%{buildroot}' -type f -name '*.bs' -size 0 -exec rm -f {} +
%{_fixperms} '%{buildroot}'/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc Changes examples README
%{_bindir}/*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Digest*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 1:5.95-367
- SCL

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.95-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.95-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.95-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.95-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.95-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.95-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.95-2
- Perl 5.22 rebuild

* Fri Jan 30 2015 Petr Pisar <ppisar@redhat.com> - 1:5.95-1
- 5.95 bump

* Wed Oct 29 2014 Petr Pisar <ppisar@redhat.com> - 1:5.93-2
- Do not build-require version module

* Mon Oct 27 2014 Petr Pisar <ppisar@redhat.com> - 1:5.93-1
- 5.93 bump

* Mon Sep 08 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.92-5
- Perl 5.20 re-rebuild of bootstrapped packages

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.92-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Petr Pisar <ppisar@redhat.com> - 1:5.92-1
- 5.92 bump

* Mon May 26 2014 Petr Pisar <ppisar@redhat.com> - 1:5.91-1
- 5.91 bump

* Fri May 09 2014 Petr Pisar <ppisar@redhat.com> - 1:5.90-1
- 5.90 bump

* Fri Apr 25 2014 Petr Pisar <ppisar@redhat.com> - 1:5.89-1
- 5.89 bump

* Tue Mar 18 2014 Petr Pisar <ppisar@redhat.com> - 1:5.88-1
- 5.88 bump

* Wed Feb 19 2014 Petr Pisar <ppisar@redhat.com> - 1:5.87-1
- 5.87 bump

* Mon Feb 03 2014 Petr Pisar <ppisar@redhat.com> - 1:5.86-1
- 5.86 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 1:5.85-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.85-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 1:5.85-2
- Perl 5.18 rebuild

* Fri Jun 28 2013 Petr Pisar <ppisar@redhat.com> - 1:5.85-1
- 5.85 bump

* Mon Mar 11 2013 Petr Pisar <ppisar@redhat.com> - 1:5.84-1
- 5.84 bump

* Tue Mar 05 2013 Petr Pisar <ppisar@redhat.com> - 1:5.83-1
- 5.83 bump

* Mon Jan 28 2013 Petr Pisar <ppisar@redhat.com> - 1:5.82-1
- 5.82 bump

* Tue Jan 15 2013 Petr Pisar <ppisar@redhat.com> - 1:5.81-1
- 5.81 bump

* Tue Dec 11 2012 Petr Pisar <ppisar@redhat.com> - 1:5.80-1
- 5.80 bump

* Fri Nov 30 2012 Petr Pisar <ppisar@redhat.com> - 1:5.74-2
- Restore epoch value broken in 5.73 bump

* Mon Nov 26 2012 Petr Pisar <ppisar@redhat.com> - 0:5.74-1
- 5.74 bump

* Thu Nov 01 2012 Petr Pisar <ppisar@redhat.com> - 0:5.73-2
- 5.73 bump

* Wed Sep 26 2012 Petr Pisar <ppisar@redhat.com> - 1:5.72-1
- 5.72 bump

* Mon Aug 13 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1:5.71-240
- bump release to override sub-package from perl.spec 

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.71-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 1:5.71-4
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 1:5.71-3
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com> - 1:5.71-2
- Omit optional POD tests on bootstrap

* Wed Mar 14 2012 Petr Pisar <ppisar@redhat.com> - 1:5.71-1
- 5.71 bump

* Tue Feb 14 2012 Petr Pisar <ppisar@redhat.com> 1:5.70-1
- Specfile autogenerated by cpanspec 1.78.
