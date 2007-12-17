Summary:	Biabam Is A Bash Attachment Mailer
Name:		biabam
License:	GPL
Version:	0.9.7
Release:	%mkrel 2
Group:		Networking/Mail
URL:		http://mmj.dk/biabam/
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
%defattr(-,root,root)
%doc COPYING README
%attr(0755,root,root) %{_bindir}/biabam

