Name:		texlive-bxwareki
Version:	51286
Release:	1
Summary:	Convert dates from Gregorian to Japanese calender
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bxwareki
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxwareki.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bxwareki.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package provides commands to convert from the
Gregorian calendar (e. g. 2018/8/28) to the Japanese rendering
of the Japanese calendar (e. g. Heisei 30 nen 8 gatsu 28 nichi;
actually with kanji characters). You can choose whether the
numbers are written in Western numerals or kanji numerals. Note
that the package only deals with dates in the year 1873 or
later, where the Japanese calendar is really a Gregorian
calendar with a different notation of years.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/bxwareki
%doc %{_texmfdistdir}/doc/latex/bxwareki

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
