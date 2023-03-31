Name:		texlive-present
Version:	50048
Release:	2
Summary:	Presentations with Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/present
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/present.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/present.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/plain/present
%doc %{_texmfdistdir}/doc/plain/present

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
