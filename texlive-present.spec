# revision 20080
# category Package
# catalog-ctan /macros/plain/contrib/present
# catalog-date 2010-09-12 18:39:28 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-present
Version:	1.0
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package offers a collection of simple macros for preparing
presentations in Plain TeX. Slide colour and text colour may be
set, links between parts of the presentation, to other files,
and to web addresses may be inserted. Images may be included
easily. The structure of the macros is not overly complex, so
that users should find it easy to adapt the macros to their
specific needs.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
