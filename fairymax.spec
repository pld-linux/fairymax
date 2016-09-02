Summary:	AI for playing user-defined Chess variants
Summary(pl.UTF-8):	AI do grania w zdefiniowane przez użytkownika warianty szachów
Name:		fairymax
Version:	4.8V
Release:	1
License:	Free
Group:		Applications/Games
# 4.8S from web page
#Source0:	http://hgm.nubati.net/fairymax.tar.gz
# newer one from git
Source0:	http://hgm.nubati.net/cgi-bin/gitweb.cgi?p=fairymax.git;a=snapshot;h=refs/tags/%{version};sf=tgz;dummy=/%{name}-%{version}.tar.gz
# Source0-md5:	c91855dc5ea5b38735fe8899794c1686
URL:		http://home.hccnet.nl/h.g.muller/CVfairy.html
BuildRequires:	perl-tools-pod
Requires:	xboard >= 4.6.0
Provides:	chess_backend
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir		%{_prefix}/games

%description
Fairy-Max is an AI, also called 'engine', for playing Chess variants.

%description -l pl.UTF-8
Fairy-Max to AI (sztuczna inteligencja), zwana także "silnikiem" do
gry w różne warianty szachów.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/games

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so fairymax.6' >$RPM_BUILD_ROOT%{_mandir}/man6/maxqi.6
echo '.so fairymax.6' >$RPM_BUILD_ROOT%{_mandir}/man6/shamax.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CVfairy.html README changelog copyright
%attr(755,root,root) %{_bindir}/fairymax
%attr(755,root,root) %{_bindir}/maxqi
%attr(755,root,root) %{_bindir}/shamax
%{_datadir}/games/fairymax
%{_datadir}/games/plugins/logos/fairymax.png
%{_datadir}/games/plugins/logos/maxqi.png
%{_datadir}/games/plugins/logos/shamax.png
%{_datadir}/games/plugins/xboard/fairymax.eng
%{_datadir}/games/plugins/xboard/maxqi.eng
%{_datadir}/games/plugins/xboard/shamax.eng
%{_mandir}/man6/fairymax.6*
%{_mandir}/man6/maxqi.6*
%{_mandir}/man6/shamax.6*
