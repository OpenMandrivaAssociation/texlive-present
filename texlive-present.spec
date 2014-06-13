# revision 25953
# category Package
# catalog-ctan /macros/plain/contrib/present
# catalog-date 2012-04-12 21:32:25 +0200
# catalog-license lppl
# catalog-version 2.2
Name:		texlive-present
Version:	2.2
Release:	6
Summary:	Presentations with Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/present
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/present.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/present.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package offers a collection of simple macros for preparing
presentations in Plain TeX. Slide colour and text colour may be
set, links between parts of the presentation, to other files,
and to web addresses may be inserted. Images may be included
easily, and code is available to provide transition effects
between slides or frames. The structure of the macros is not
overly complex, so that users should find it easy to adapt the
macros to their specific needs.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/present/present.tex
%doc %{_texmfdistdir}/doc/plain/present/HowToTalkTeX.pdf
%doc %{_texmfdistdir}/doc/plain/present/HowToTalkTeX.tex
%doc %{_texmfdistdir}/doc/plain/present/Pfeil1.pdf
%doc %{_texmfdistdir}/doc/plain/present/Pfeil2.pdf
%doc %{_texmfdistdir}/doc/plain/present/Pfeil3.pdf
%doc %{_texmfdistdir}/doc/plain/present/Pfeil4.pdf
%doc %{_texmfdistdir}/doc/plain/present/README
%doc %{_texmfdistdir}/doc/plain/present/Sagnac.pdf
%doc %{_texmfdistdir}/doc/plain/present/Stern.png
%doc %{_texmfdistdir}/doc/plain/present/background.png
%doc %{_texmfdistdir}/doc/plain/present/present-transitions.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 805039
- Update to latest release.

* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 787731
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755062
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719296
- texlive-present
- texlive-present
- texlive-present
- texlive-present

