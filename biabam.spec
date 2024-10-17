Summary:	Bash Attachment Mailer
Name:		biabam
License:	GPL
Version:	0.9.7
Release:	9
Group:		Networking/Mail
URL:		https://mmj.dk/biabam/
Source0:	http://mmj.dk/biabam/%{name}-%{version}.tar.bz2
Requires:	sendmail-command
Requires:	sharutils
BuildArch:	noarch

%description
Biabam Is A Bash Attachment Mailer. In other words, BIABAM is a
tool that is used for mailing attachments from the commandline. It
is similar to using Mutt to send attachments on the commandline,
but without the overhead of a complete email client.

%prep

%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 biabam %{buildroot}%{_bindir}/biabam

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%doc COPYING README
%attr(0755,root,root) %{_bindir}/biabam



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-7mdv2011.0
+ Revision: 616750
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.9.7-6mdv2010.0
+ Revision: 424612
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-5mdv2009.0
+ Revision: 243214
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9.7-3mdv2008.1
+ Revision: 170774
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Jul 26 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.9.7-2mdk
- Fix smtpdaemon

* Sun May 29 2005 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-1mdk
- initial Mandriva package

